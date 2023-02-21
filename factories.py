
from services import IApiFetcher

class FetcherFactory:
    def __init__(self, instances: dict) -> None:
        print(instances)
        self.__instances = instances
    def initiateInstance(self, event: str) -> IApiFetcher:
        return self.__instances[event]()