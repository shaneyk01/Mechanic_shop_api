from .schemas import ticket_schema, tickets_schema 
from flask import request ,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Service_tickets, Mechanic, ticket_mechanics, db
from . import tickets_bp
from app.blueprints.mechanics.schemas import mechanic_schema   

@tickets_bp.route('/', methods=['POST'])
def create_ticket():
    if not request.is_json:
        return jsonify({'_schema': ['Request body must be JSON.']}), 400
    try:
        ticket_data = ticket_schema.load(request.get_json())
    except ValidationError as e:
        return jsonify(e.messages), 400
    new_ticket = Service_tickets(**ticket_data) 
    db.session.add(new_ticket)
    db.session.commit()
    return ticket_schema.jsonify(new_ticket), 201


@tickets_bp.route('/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    query = select(Service_tickets).where(Service_tickets.ticket_id == ticket_id)
    ticket = db.session.execute(query).scalar_one_or_none()
    if ticket is not None:
        return ticket_schema.jsonify(ticket), 200
    else:
        return jsonify({'error': 'Ticket not found'}), 404
    
@tickets_bp.route('/<int:ticket_id>/add-mechanic/<int:mechanic_id>', methods=['PUT'])
def add_mechanic(ticket_id, mechanic_id):
    ticket = db.session.get(Service_tickets, ticket_id)
    mechanic = db.session.get(Mechanic, mechanic_id)
    if ticket and mechanic:
        if mechanic not in ticket.mechanics:
            ticket.mechanics.append(mechanic)
    db.session.commit()
    
    return jsonify({
        'message': 'Successfully added mechanic to ticket',
        'ticket': ticket_schema.dump(ticket),
        'mechanic': mechanic_schema.dump(mechanic)
    }), 200

@tickets_bp.route('/<int:ticket_id>/remove-mechanic/<int:mechanic_id>', methods=['PUT'])
def remove_mechanic(ticket_id, mechanic_id):
    ticket = db.session.get(Service_tickets, ticket_id)
    mechanic = db.session.get(Mechanic, mechanic_id)
    if ticket and mechanic:
        if mechanic in ticket.mechanics:
            ticket.mechanics.remove(mechanic)
            db.session.commit()
            return jsonify({
                'message': 'successfully removed mechanic from ticket',
                'ticket': ticket_schema.dump(ticket),
                'mechanic': mechanic_schema.dump(mechanic)
        }), 200
        return jsonify({'error': 'This Mechanic is not assigned to this ticket'}), 404
    return jsonify({'error': 'invalid mechanic_id or ticket_id'}), 404

@tickets_bp.route('/', methods=['GET'])
def get_all_tickets():
    query = select(Service_tickets)
    tickets = db.session.execute(query).scalars().all()
    return tickets_schema.jsonify(tickets), 200


