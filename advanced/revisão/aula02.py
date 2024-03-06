class Connection:

    def __init__(self, host_from='localhost'):
        self.host_from: str = host_from
        self._host_to: str | None = None

    @property
    def host(self):
        return self._host_to

    @host.setter
    def host(self, value):
        self._host_to = value


con = Connection()
con.host = '127.0.0.1'
print(con.host)
