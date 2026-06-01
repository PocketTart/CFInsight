from fastapi import APIRouter

from services.metrics_service import (
    MetricsService
)

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)


@router.get("/")
async def get_metrics():

    return (
        MetricsService.get_metrics()
    )