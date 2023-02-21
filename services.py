from abc import ABC, abstractmethod
import requests

class IApiFetcher(ABC):
    @abstractmethod
    def request(self) -> str:
        pass
class ApiFetcher(IApiFetcher):
    def request(self) -> str:
        result = requests.get("https://w3schools.com/python/demopage.htm")
        return result.text
class DifferentApiFetcher(IApiFetcher):
    def request(self) -> str:
        result = requests.get("https://www.google.com")
        return result.text
