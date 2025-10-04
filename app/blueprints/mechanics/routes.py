from app.blueprints.mechanics.schemas import mechanic_schema, mechanics_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Mechanic
from app.extensions import db
from . import mechanics_bp




@mechanics_bp.route('/', methods=['POST'])
def create_mechanic():          
    if not isinstance(request.json, dict):
        return jsonify({'_schema': ['Invalid input type. Expected a JSON object.']}), 400
    try:
        mechanic_data = mechanic_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_mechanic = Mechanic(**mechanic_data) 
    db.session.add(new_mechanic)
    db.session.commit()
    return mechanic_schema.jsonify(new_mechanic), 201


@mechanics_bp.route('/', methods=['GET'])
def get_mechanics():
        query  = select(Mechanic)
        mechanics = db.session.execute(query).scalars().all()
        return mechanics_schema.jsonify(mechanics), 200
    
@mechanics_bp.route('/<int:mechanic_id>', methods=['PUT'])
def update_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)
    if not mechanic:
        return jsonify({'error': 'Mechanic not found'}), 404
    
    try:
        mechanic_data = mechanic_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    for key, value in mechanic_data.items():
        setattr(mechanic, key, value)
    db.session.commit()
    return mechanic_schema.jsonify(mechanic), 200

@mechanics_bp.route('/<int:mechanic_id>', methods=['DELETE'])
def delete_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)
    if not mechanic:
        return jsonify({'error': 'Mechanic not found'}), 404
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({'message': 'Mechanic deleted successfully'}), 200



