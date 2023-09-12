from dependency_injector import containers, providers
from src.domain.ports.ticket_service import TicketService
from src.adapters.db.pg_repository import TicketInPG


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.adapters.api.blueprints"])

    repo = TicketInPG()

    ticket_service = providers.Factory(
        TicketService,
        ticket_repo=repo
    )
