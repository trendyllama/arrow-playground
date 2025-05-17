

class DataDownloader:

    _url: str | None
    _destination: str | None

    def __init__(self):
        self._url = None
        self._destination = None


    def set_url(self, url: str): ...

    def set_destination(self, destination: str): ...

    def download(self): ...

    def get_contents_as_dataframe(self): ...