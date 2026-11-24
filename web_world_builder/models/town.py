
from sqlalchemy import Column, Integer, String
from web_world_builder.utilities import capitalize_sentences
from web_world_builder.randomizers.town_randomizer import TownRandomizer
from web_world_builder.sqlite_db_manager import Base

class Town(Base):

    __tablename__ = 'towns'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    population_size = Column(Integer)

    def __init__(self, name=None, email=None):
        self.town_constructor = TownRandomizer.get_instance()
        if not name:
            self.name = self.town_constructor.randomize()
        else:
            self.name = name
        self.population_size = 1000

    def __repr__(self):
        return f'<User {self.name!r}>'

    def __str__(self):
        description = f"{self.name}"
        return capitalize_sentences(description)
