from src.domain.model.ticket import Ticket
from src.domain.ports.ticket_repository import TicketRepositoryInterface
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class TicketInPG(TicketRepositoryInterface):

    db_name = 'database'
    db_user = 'postgres'
    db_pass = 'postgres'
    db_host = 'qs-hexagonal-db'
    db_port = '5432'

    # Connecto to the database
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    db = create_engine(db_string)

    def create(self, ticket: Ticket) -> Ticket:
        query_str = "INSERT INTO tickets (description, priority, status, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}')"
        query = text(query_str.format(ticket.description, ticket.priority, ticket.status, ticket.created_at, ticket.updated_at))
        with self.db.begin() as conn:
            ticket = conn.execute(query)
        return ticket

    def find_all(self) -> list[Ticket]:
        tickets = []
        query = text('SELECT * FROM tickets')
        with self.db.begin() as conn:
            result = conn.execute(query)
            for row in result.fetchall():
                tickets.append(Ticket(row[1], row[2], row[0], row[3], row[4], row[5]))
        return tickets