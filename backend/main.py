from fastapi import FastAPI

from core.database import Base, engine,SessionLocal
# Models (must be imported before create_all)
from models.user import User
from models.report import Report
from models.search_stats import SearchStats
from middleware.timing import timing_middleware
from models.cache_stats import CacheStats
# Routers
from api.health import router as health_router
from api.report import router as report_router
from api.leaderboard import router as leaderboard_router
from api.suggest import router as suggest_router
from api.metrics import (router as metrics_router)

from api.cache_stats import router as cache_stats_router
from core.trie_store import trie
from core.trie_store import handle_frequency


from repositories.search_stats_repository import SearchStatsRepository
from repositories.user_repository import UserRepository
from fastapi.middleware.cors import CORSMiddleware

# Create tables
Base.metadata.create_all(bind=engine)

print("Registered tables:", Base.metadata.tables.keys())

app = FastAPI(
    title="CFInsight",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def load_trie():

    db = SessionLocal()

    try:

        stats = SearchStatsRepository.get_handle_frequencies(db)


        for handle,count in stats:
            trie.insert(handle)

            handle_frequency[handle] = count

    finally:

        db.close()


# Include routers
app.include_router(health_router)
app.include_router(report_router)
app.include_router(leaderboard_router)
app.include_router(cache_stats_router)
app.include_router(suggest_router)
app.include_router(metrics_router)
@app.get("/")
def root():
    return {
        "message": "CFInsight API Running"
    }



app.middleware("http")(timing_middleware)