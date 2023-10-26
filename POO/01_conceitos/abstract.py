from abc import ABC, abstractmethod

class Log(ABC):

    @abstractmethod
    def _log(self, msg): ... #método abstrato

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")
