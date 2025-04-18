import time
import logging

logger = logging.getLogger(__name__)


class VolCacheNode:
    def __init__(self, data: dict, timestamp: float):
        self.data: dict = data
        self.timestamp: float = timestamp


class VolCache:
    def __init__(self, expirationSeconds: int):
        self.internalCache: dict[str, VolCacheNode] = {}
        self.expirationSeconds: int = expirationSeconds
        logger.info(f"VolCache initialized with expiration: {expirationSeconds} seconds")

    def get(self, key: str) -> dict | None:
        if key in self.internalCache:
            cacheNode = self.internalCache[key]
            if time.time() - cacheNode.timestamp < self.expirationSeconds:
                logger.info(f"Cache hit for {key}")
                return cacheNode.data
            else:
                del self.internalCache[key]
                logger.info(f"Evicted {key} from cache")

        logger.info(f"Cache miss for {key}")
        return None

    def set(self, key: str, value: dict):
        self.internalCache[key] = VolCacheNode(value, time.time())
        logger.info(f"Added '{key}' to cache")
        return value
