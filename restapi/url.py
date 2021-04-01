class URL:
    def __init__(self, path=""):
        self._root = "https://discord.com/api/v8"
        self._path = path
        self._query = {}

    def add_query_params(self, query_params):
        self._query.update(
            {k: v
             for k, v in query_params.items() if v is not None})

    def build(self):
        query = "?" + "&".join(
            ["{k}={v}".format(k=k, v=v)
             for k, v in self._query.items()]) if self._query else ""
        return self._root + self._path + query