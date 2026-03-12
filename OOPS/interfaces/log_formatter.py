from abc import ABC, abstractmethod

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass

class PlainFormatter(Formatter):
    def format(self, message: str) -> str:
        return message
    
class JSONformatter(Formatter):
      def format(self, message: str) -> str:
        return '{"log": "' + message + '"}'

class Logger:
    def __init__(self, formatter: Formatter):
        self._formatter = formatter

    def log(self, message: str) -> None:
        print(self._formatter.format(message))

if __name__ == "__main__":
    plain_logger = Logger(PlainFormatter())
    plain_logger.log("Server started on port 8080")

    json_logger = Logger(JSONformatter())
    json_logger.log("Server started on port 8080")