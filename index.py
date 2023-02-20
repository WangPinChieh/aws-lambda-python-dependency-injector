import json
import requests
import os
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from abc import ABC, abstractmethod

class IApiFetcher(ABC):
    @abstractmethod
    def request(self):
        pass
class ApiFetcher(IApiFetcher):
    def request(self):
        result = requests.get("https://w3schools.com/python/demopage.htm")
        return result.text
class DifferentApiFetcher(IApiFetcher):
    def request(self):
        result = requests.get("https://www.google.com")
        return result.text

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    if config.event == 'w3schools':
        apiFetcher = providers.Singleton(ApiFetcher)
    else:
        apiFetcher = providers.Singleton(DifferentApiFetcher)


@inject
def lambda_handler(event, context, apiFetcher: IApiFetcher = Provide[Container.apiFetcher]):
    # TODO implement
    result = apiFetcher.request()
    # print(result['url'])
    return {
        'statusCode': 200,
        'body': result,
    }


container = Container()
container.config.event.from_env('ENV_EVENT')
container.wire(modules=[__name__])
