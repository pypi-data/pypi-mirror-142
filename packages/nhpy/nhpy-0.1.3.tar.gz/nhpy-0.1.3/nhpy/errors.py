class HttpConnectionError(Exception):
    def __int__(self, status_code, message):
        self.message = f"Status Code: {status_code}\nMessage: {message}"
        super().__init__(self.message)
