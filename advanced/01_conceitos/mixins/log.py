# ABSTRAÇÂO
# Herança -> é um
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg): # template method
        raise NotImplementedError(
            'Implemente o método log'
        )

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")


class LogFileMixin(Log):
    def _log(self, msg): # deve ser congruente ao método da superclasse
        msg_formated = f"{msg} ({self.__class__.__name__})"
        print("Salvando no log:", msg_formated)
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formated)
            file.write('\r\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


if __name__ == '__main__':
    lf = LogFileMixin()
    lf.log_error('Something here!')
    lf.log_success('Great!!!')

    lp = LogPrintMixin()
    lp.log_error('Something here!')
    lp.log_success('Great!!!')

    print(LOG_FILE)