import core.metrics_store as metrics


class MetricsService:

    @staticmethod
    def get_metrics():

        avg_response_time = 0

        if metrics.request_count > 0:

            avg_response_time = (
                metrics.total_response_time
                /
                metrics.request_count
            )

        return {
            "request_count":
                metrics.request_count,

            "avg_response_time_ms":
                round(
                    avg_response_time * 1000,
                    2
                ),

            "max_response_time_ms":
                round(
                    metrics.max_response_time * 1000,
                    2
                )
        }