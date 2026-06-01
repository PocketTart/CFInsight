from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
import asyncio
from sqlalchemy.orm import Session

from core.database import get_db
from core.trie_store import trie
from core.trie_store import handle_frequency
from services.codeforces_service import CodeforcesService
from services.analytics_service import AnalyticsService
from services.suspicion_service import SuspicionService
from services.cache_service import CacheService
from services.ai_service import AIService

from repositories.user_repository import UserRepository
from repositories.report_repository import ReportRepository
from repositories.search_stats_repository import SearchStatsRepository
from repositories.cache_stats_repository import CacheStatsRepository

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

cf_service = CodeforcesService()

ai_service = AIService()


@router.get("/{handle}")
async def generate_report(
    handle: str,
    db: Session = Depends(get_db)
):

    handle = handle.strip().lower()
    SearchStatsRepository.increment_search(
        db,
        handle
    )
    
    
    
    user_cache = UserRepository.get_by_handle(db, handle)

    if user_cache:
        cached_report = ReportRepository.get_by_user_id(db, user_cache.id)

        if cached_report and not CacheService.is_expired(cached_report.generated_at):
            CacheStatsRepository.increment_hit(db)

            return {
                "source": "cache",
                **cached_report.report_json
            }

    # ---------------------------------------------------

    try:

        profile, contests, submissions = (
            await asyncio.gather(
                cf_service.get_profile(handle),
                cf_service.get_contests(handle),
                cf_service.get_submissions(handle)
            )
        )


        
        canonical_handle = profile["handle"]
        
        


        CacheStatsRepository.increment_miss(db)
        if canonical_handle not in handle_frequency:

            trie.insert(canonical_handle)

            handle_frequency[canonical_handle] = 1

        else:

            handle_frequency[canonical_handle] += 1


    except Exception:

        raise HTTPException(
            status_code=404,
            detail="Codeforces user not found"
        )
    existing_user = UserRepository.get_by_handle(
        db,
        canonical_handle
    )


    if not existing_user:

        user = UserRepository.create(
            db,
            profile
        )
        

    else:

        user = existing_user

    contest_analysis = (
        AnalyticsService
        .get_contest_analytics(contests)
    )

    problem_analysis = (
        AnalyticsService
        .get_problem_analytics(submissions)
    )

    activity_analysis = (
        AnalyticsService
        .get_activity_analytics(submissions)
    )

    average_recent_contest_difficulty = (
        AnalyticsService.get_average_recent_contest_difficulty(
            submissions,
            contests
        ) or 0
    )

    suspicion_analysis = (
        SuspicionService.calculate(
            current_rating=user.current_rating,
            average_recent_contest_difficulty=
                average_recent_contest_difficulty,
            skipped_submissions=
                activity_analysis[
                    "skipped_submissions"
                ],
            total_submissions=
                activity_analysis[
                    "total_submissions"
                ]
        )
    )

    ai_insights = (
    ai_service.generate_insights(
        {
            "handle": user.handle,
            "current_rating": user.current_rating,
            "max_rating": user.max_rating,
            "current_rank": user.current_rank,
            "max_rank": user.max_rank
        },
        contest_analysis,
        problem_analysis,
        activity_analysis,
        suspicion_analysis
    )
)

    full_report = {
        "profile": {
            "handle": user.handle,
            "current_rating": user.current_rating,
            "max_rating": user.max_rating,
            "current_rank": user.current_rank,
            "max_rank": user.max_rank
        },

        "contest_analysis": contest_analysis,
        "problem_analysis": problem_analysis,
        "activity_analysis": activity_analysis,
        "suspicion_analysis": suspicion_analysis,
        "ai_insights": ai_insights
    }

    ReportRepository.upsert_report(db, user.id, full_report)


    CacheService.cleanup(db)

    return {
        "source": "fresh",
        **full_report
    }