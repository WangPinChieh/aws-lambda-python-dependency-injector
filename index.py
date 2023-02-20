import json
import requests
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class ApiFetcher:
    def request(self):
        result = requests.get("https://w3schools.com/python/demopage.htm")
        return result


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    apiFetcher = providers.Singleton(ApiFetcher)


@inject
def lambda_handler(event, context, apiFetcher: ApiFetcher = Provide[Container.apiFetcher]):
    # TODO implement
    result = apiFetcher.request()
    print(result.text)
    return {
        'statusCode': 200,
        'body': result.text
    }




container = Container()
container.wire(modules=[__name__])
