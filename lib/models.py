from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Provided metadata and naming convention
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Create a base class with the provided metadata
Base = declarative_base(metadata=metadata)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    platform = Column(String)
    genre = Column(String)
    price = Column(Integer)

    # Define the relationship with Review using a back reference
    reviews = relationship("Review", backref=backref("game"))

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    game_id = Column(Integer, ForeignKey('games.id'))  # Establish foreign key relationship

# You can continue with the test code or use the classes in other parts of your application.
