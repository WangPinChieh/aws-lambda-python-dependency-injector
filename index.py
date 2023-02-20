import json
import requests
import os
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class ApiFetcher:
    def __init__(self, url: str) -> None:
        self.url = url
    def request(self):
        result = requests.get("https://w3schools.com/python/demopage.htm")
        return {
            'text': result.text,
            'url': self.url
        }


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    apiFetcher = providers.Singleton(ApiFetcher, config.env_url)


@inject
def lambda_handler(event, context, apiFetcher: ApiFetcher = Provide[Container.apiFetcher]):
    # TODO implement
    result = apiFetcher.request()
    # print(result['url'])
    return {
        'statusCode': 200,
        'body': result['text'],
        'url': result['url']
    }


container = Container()
container.config.env_url.from_env('ENV_URL')
container.wire(modules=[__name__])
