from collections import Counter
from datetime import datetime


class AnalyticsService:

    @staticmethod
    def get_monthly_growth(contests):

        if not contests:
            return 0

        now = datetime.utcnow()

        monthly_contests = []

        for contest in contests:

            contest_date = datetime.utcfromtimestamp(
                contest["ratingUpdateTimeSeconds"]
            )

            if (
                contest_date.year == now.year
                and contest_date.month == now.month
            ):
                monthly_contests.append(contest)

        if not monthly_contests:
            return 0

        return (
            monthly_contests[-1]["newRating"]
            -
            monthly_contests[0]["oldRating"]
        )

    @staticmethod
    def get_yearly_growth(contests):

        if not contests:
            return 0

        now = datetime.utcnow()

        yearly_contests = []

        for contest in contests:

            contest_date = datetime.utcfromtimestamp(
                contest["ratingUpdateTimeSeconds"]
            )

            if contest_date.year == now.year:
                yearly_contests.append(contest)

        if not yearly_contests:
            return 0

        return (
            yearly_contests[-1]["newRating"]
            -
            yearly_contests[0]["oldRating"]
        )

    @staticmethod
    def get_contest_analytics(contests):

        if not contests:
            return {}

        rating_changes = [
            contest["newRating"] - contest["oldRating"]
            for contest in contests
        ]

        ratings = [
            contest["newRating"]
            for contest in contests
        ]

        ranks = [
            contest["rank"]
            for contest in contests
        ]

        return {
            "total_contests": len(contests),
            "current_rating": ratings[-1],
            "max_rating": max(ratings),
            "average_rating": round(
                sum(ratings) / len(ratings),
                2
            ),
            "rating_growth":
                ratings[-1] - contests[0]["oldRating"],
            "monthly_rating_growth":
                AnalyticsService.get_monthly_growth(
                    contests
                ),
            "yearly_rating_growth":
                AnalyticsService.get_yearly_growth(
                    contests
                ),
            "average_rating_change":
                round(
                    sum(rating_changes)
                    / len(rating_changes),
                    2
                ),
            "largest_rating_increase":
                max(rating_changes),
            "largest_rating_decrease":
                min(rating_changes),
            "best_rank": min(ranks),
            "worst_rank": max(ranks),
            "average_rank":
                round(
                    sum(ranks) / len(ranks),
                    2
                )
        }

    @staticmethod
    def get_problem_analytics(submissions):

        solved_problems = set()

        solved_ratings = []

        tag_counter = Counter()

        for sub in submissions:

            if sub.get("verdict") != "OK":
                continue

            problem = sub["problem"]

            key = (
                problem.get("contestId"),
                problem.get("index")
            )

            solved_problems.add(key)

            rating = problem.get("rating")

            if rating:
                solved_ratings.append(rating)

            for tag in problem.get("tags", []):
                tag_counter[tag] += 1

        difficulty_distribution = {
            "800-1200": 0,
            "1200-1600": 0,
            "1600-2000": 0,
            "2000-2400": 0,
            "2400+": 0
        }

        for rating in solved_ratings:

            if rating < 1200:
                difficulty_distribution["800-1200"] += 1

            elif rating < 1600:
                difficulty_distribution["1200-1600"] += 1

            elif rating < 2000:
                difficulty_distribution["1600-2000"] += 1

            elif rating < 2400:
                difficulty_distribution["2000-2400"] += 1

            else:
                difficulty_distribution["2400+"] += 1

        return {
            "total_solved":
                len(solved_problems),

            "hardest_problem":
                max(solved_ratings)
                if solved_ratings else 0,

            "average_difficulty":
                round(
                    sum(solved_ratings)
                    / len(solved_ratings),
                    2
                )
                if solved_ratings else 0,

            "difficulty_distribution":
                difficulty_distribution,

            "top_tags":
                dict(
                    tag_counter.most_common(10)
                )
        }

    @staticmethod
    def get_average_recent_contest_difficulty(
        submissions,
        contests
    ):

        if not contests:
            return 0

        recent_contests = contests[-5:]

        contest_ids = {
            contest["contestId"]
            for contest in recent_contests
        }

        ratings = []

        for sub in submissions:

            if sub.get("verdict") != "OK":
                continue

            author = sub.get(
                "author",
                {}
            )

            if (
                author.get("participantType")
                != "CONTESTANT"
            ):
                continue

            if (
                sub.get("contestId")
                not in contest_ids
            ):
                continue

            rating = (
                sub["problem"]
                .get("rating")
            )

            if rating:
                ratings.append(rating)

        if not ratings:
            return 0

        return round(
            sum(ratings) / len(ratings),
            2
        )
          
    @staticmethod
    def get_activity_analytics(submissions):

        verdict_counter = Counter()

        for sub in submissions:

            verdict = sub.get(
                "verdict",
                "UNKNOWN"
            )

            verdict_counter[verdict] += 1

        total = len(submissions)

        accepted = verdict_counter.get(
            "OK",
            0
        )

        success_rate = (
            round(
                accepted * 100 / total,
                2
            )
            if total else 0
        )

        return {
            "total_submissions": total,
            "accepted": accepted,
            "wrong_answer":
                verdict_counter.get(
                    "WRONG_ANSWER",
                    0
                ),
            "time_limit_exceeded":
                verdict_counter.get(
                    "TIME_LIMIT_EXCEEDED",
                    0
                ),
            "runtime_error":
                verdict_counter.get(
                    "RUNTIME_ERROR",
                    0
                ),
            "memory_limit_exceeded":
                verdict_counter.get(
                    "MEMORY_LIMIT_EXCEEDED",
                    0
                ),
            "skipped_submissions":
                verdict_counter.get(
                    "SKIPPED",
                    0
                ),
            "success_rate":
                success_rate
        }