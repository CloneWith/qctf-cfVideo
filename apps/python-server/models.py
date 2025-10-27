from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Attachment(Base):
    __tablename__ = 'attachments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255))
    # requests = relationship('Request', back_populates='attachment')

class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64))
    email = Column(String(128))
    theme = Column(String(128))
    content = Column(String(1024))
    contact = Column(String(128))
    fee = Column(Float)
    attachment_id = Column(Integer, ForeignKey('attachments.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # attachment = relationship('Attachment', back_populates='requests')

class Budget(Base):
    __tablename__ = 'budget'
    id = Column(Integer, primary_key=True, autoincrement=True)
    reason = Column(String(255))
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Sponsorship(Base):
    __tablename__ = 'sponsorship'
    username = Column(String(64), primary_key=True)
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
