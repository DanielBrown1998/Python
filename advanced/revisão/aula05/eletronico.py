from log import LogFileMixin, LOG_FILE


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def start(self):
        if not self._ligado:
            self._ligado = True

    def end(self):
        if self._ligado:
            self._ligado = False


class SmartPhone(Eletronico, LogFileMixin):

    def start(self):
        super().start()
        if self._ligado:
            super().log_success(f"{self._nome} iniciado com sucesso")

    def end(self):
        super().end()
        if not self._ligado:
            super().log_success(f"{self._nome} desligado com sucesso")
