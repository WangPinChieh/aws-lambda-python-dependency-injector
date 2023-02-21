from dependency_injector import containers, providers
from services import ApiFetcher, DifferentApiFetcher
from factories import FetcherFactory
class Container(containers.DeclarativeContainer):
    # print('in Container class')
    config = providers.Configuration()
    instances = {
        'w3schools': providers.Factory(ApiFetcher),
        'google': providers.Factory(DifferentApiFetcher),
    }
    instance_factory = providers.Factory(FetcherFactory, instances)

