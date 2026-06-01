import time
import logging

from fastapi import Request

import core.metrics_store as metrics

logger = logging.getLogger(__name__)


async def timing_middleware(
    request: Request,
    call_next
):

    start_time = time.time()

    print("Middleware Executed")

    response = await call_next(request)

    process_time = (
        time.time() - start_time
    )

    if request.url.path.startswith(
        "/report"
    ):

        metrics.request_count += 1

        metrics.total_response_time += (
            process_time
        )

        metrics.max_response_time = max(
            metrics.max_response_time,
            process_time
        )

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"completed in "
        f"{process_time:.3f}s"
    )

    response.headers[
        "X-Process-Time"
    ] = str(
        round(
            process_time,
            3
        )
    )

    return response