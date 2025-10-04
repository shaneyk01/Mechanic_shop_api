from app.models import Service_tickets
from app.extensions import ma



class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service_tickets
        include_fk = True



ticket_schema = ServiceTicketSchema()
tickets_schema = ServiceTicketSchema(many=True)