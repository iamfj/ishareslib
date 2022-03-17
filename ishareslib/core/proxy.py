class Proxy:
    def __init__(
        self,
        address: str,
        port: int,
        protocol: str = "http",
        username: str = None,
        password: str = None,
    ):
        self.address = address
        self.port = port
        self.protocol = protocol
        self.username = username
        self.password = password
