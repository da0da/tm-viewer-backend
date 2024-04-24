from dependency_injector import containers, providers

from app.use_cases.gbx.load_file import LoadRunUseCase


class WebAppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.api", __name__])

    load_gbx_file_use_case: providers.Factory[LoadRunUseCase] = providers.Factory(
        LoadRunUseCase
    )
