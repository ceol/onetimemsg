from sqlalchemy import (
    func,
    Column,
    Boolean,
    DateTime,
    Integer,
    Text,
    String,
)
from sqlalchemy.orm import relationship, backref
from onetimemsg.database import Base

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=func.now())
    ip = Column(String)

    uid = Column(String, unique=True)
    text = Column(Text)