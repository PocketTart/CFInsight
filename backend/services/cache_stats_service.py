from repositories.cache_stats_repository import CacheStatsRepository


class CacheStatsService:

    @staticmethod
    def get_stats(db):

        stats = CacheStatsRepository.get_stats(db)

        total_requests = (
            stats.cache_hits +
            stats.cache_misses
        )

        hit_rate = 0.0

        if total_requests > 0:
            hit_rate = (
                stats.cache_hits / total_requests
            ) * 100

        return {
            "cache_hits": stats.cache_hits,
            "cache_misses": stats.cache_misses,
            "total_requests": total_requests,
            "hit_rate": round(hit_rate, 2),
            "last_updated": stats.last_updated
        }