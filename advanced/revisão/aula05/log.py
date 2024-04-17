# Abstrção
import abc
import datetime
import pathlib

LOG_FILE = pathlib.Path(__file__).parent / 'log.txt'


class Log(abc.ABC):
    @abc.abstractmethod
    def _log(self, msg: str):
        raise NotImplementedError(
            'Implemente o método log'
        )

    def log_error(self, msg: str):
        return self._log(msg)

    def log_success(self, msg: str):
        return self._log(msg)


class LogFileMixin(Log):
    def _log(self, msg):
        msg_fmt = f"{self.__class__.__name__}, {msg}"
        with open(LOG_FILE, 'a', encoding="utf-8") as log_file:
            log_file.write(f"{msg_fmt}\n")
        print(msg_fmt)
        return msg_fmt


if __name__ == '__main__':
    lf = LogFileMixin()
    lf.log_success(f"Success: {str(datetime.datetime.now())}")
    lf.log_error(f"Error: {str(datetime.datetime.now())}")
