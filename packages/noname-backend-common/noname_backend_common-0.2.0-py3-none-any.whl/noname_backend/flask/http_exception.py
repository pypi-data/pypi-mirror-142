class HttpException(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.message = message
        self.code = code

def bind(app):
    @app.errorhandler(HttpException)
    def http_exception(e):
        return {'message': e.message}, e.code
