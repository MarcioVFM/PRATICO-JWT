class HttpResquest:
    def __init__(self, 
                 body: dict = None, 
                 token_infos: dict = None, 
                 params: dict = None
                 ) -> None:
        self.body = body
        self.token_infos = token_infos
        self.params = params