from containers import Container
from services import FetcherFactory
from dependency_injector.wiring import Provide, inject

@inject
def lambda_handler(event, context, instanceFacctory: FetcherFactory = Provide[Container.instance_factory]):
    # TODO implement
    apiFetcher = instanceFacctory.initiateInstance(event['name'])
    result = apiFetcher.request()
    print(result)
    return {
        'statusCode': 200,
        'body': result,
    }

container = Container()
container.wire(modules=[__name__])
# lambda_handler({'name': 'google'}, None)
