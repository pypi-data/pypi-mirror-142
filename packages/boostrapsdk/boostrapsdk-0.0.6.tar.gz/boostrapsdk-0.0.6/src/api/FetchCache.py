import requests
import time


class FetchCache(object):
    cache = {}

    def __init__(self, **options):
        self.ttl_ms = options.get('ttl_ms')
        self.response = {}
        logger = options.get('logger', False)
        if logger:
            self.logger = logger
        else:
            self.logger = print

    def get(self, url: str):
        self.trim_cache()
        try:
            hit = FetchCache.cache[url]
            return hit[1]
        except KeyError:
            ms = int(time.time() * 1000.0)
            response = self.get_url_with_retry(url)
            FetchCache.cache[url] = [ms, response]
            return response

    def trim_cache(self):
        keys_to_delete = [];
        for url, items in FetchCache.cache.items():
            now = int(time.time() * 1000.0)
            should_purge = (items[0] + self.ttl_ms) < now
            if should_purge:
                keys_to_delete.append(url)
        for key in keys_to_delete:
            del FetchCache.cache[key]

    @staticmethod
    def get_url_with_retry(url: str):
        attempts = 0
        max_attempts = 3
        backoff_times = [10, 1000, 10000]
        while attempts < max_attempts:
            try:
                response = requests.get(url)
                return response
            except Exception as e:
                time.sleep(backoff_times[attempts])
                print(f'Request failed, retrying, {e}')
                attempts += 1

        raise Exception(f'Maximum attempts ({attempts}) made to the resource with no valid response')
