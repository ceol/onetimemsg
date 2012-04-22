from sqlalchemy import (
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
    pub_date = Column(DateTime)
    ip = Column(String)

    uid = Column(String, unique=True)
    text = Column(Text)