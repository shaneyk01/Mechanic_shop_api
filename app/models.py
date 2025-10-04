from .extensions import Base, db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from datetime import date as Date
from sqlalchemy import ForeignKey


ticket_mechanics = db.Table(
    'ticket_mechanics',
    Base.metadata,
    db.Column('ticket_id', db.ForeignKey('tickets.ticket_id')),
    db.Column('mechanic_id', db.ForeignKey('mechanics.mechanic_id'))
)


class Customer(Base):
    __tablename__ = 'customers'
    customer_id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(db.String(255), nullable=False)
    email:Mapped[str] = mapped_column(db.String(255), nullable=False)
    phone:Mapped[str] = mapped_column(db.String(255), nullable=False)
    password:Mapped[str] = mapped_column(db.String(255), nullable=False)
    
    tickets: Mapped[List['Service_tickets']] = db.relationship('Service_tickets', back_populates='customer')

class Mechanic(Base):
    __tablename__ = 'mechanics'
    mechanic_id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(db.String(255), nullable=False)
    email:Mapped[str] = mapped_column(db.String(255), nullable=False)
    phone:Mapped[str] = mapped_column(db.String(255), nullable=False)
    salary:Mapped[str] = mapped_column(db.String(255), nullable=True)
    
    tickets: Mapped[List['Service_tickets']] = db.relationship('Service_tickets', secondary=ticket_mechanics, back_populates='mechanics')

class Service_tickets(Base):
    __tablename__ = 'tickets'
    ticket_id:Mapped[int] = mapped_column(primary_key=True)
    ticket_date:Mapped[Date] = mapped_column(db.Date)
    service_desc:Mapped[str] = mapped_column(db.String(255))
    customer_id:Mapped[int] = mapped_column(db.ForeignKey('customers.customer_id'))

    customer: Mapped['Customer'] = db.relationship('Customer', back_populates='tickets')
    mechanics: Mapped[List['Mechanic']] = db.relationship('Mechanic', secondary=ticket_mechanics, back_populates='tickets')



