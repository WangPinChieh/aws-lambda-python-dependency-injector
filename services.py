from abc import ABC, abstractmethod
from dependency_injector import providers
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

class FetcherFactory:
    def __init__(self, instances: dict) -> None:
        print(instances)
        self.__instances = instances
    def initiateInstance(self, event: str) -> IApiFetcher:
        return self.__instances[event]()