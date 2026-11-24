
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from web_world_builder.utilities import capitalize_sentences, prefix_indefinite_article
from web_world_builder.randomizers.town_randomizer import TownRandomizer
from web_world_builder.models.geography import Geography
from web_world_builder.sqlite_db_manager import Base

class Town(Base):

    SIZE_THRESHOLDS = {
        "hamlet": 0,
        "village": 150,
        "town": 1000,
        "city": 10000
    }

    __tablename__ = 'towns'
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(50), unique=True)
    population_size = Column(Integer)
    geography: Mapped["Geography"] = relationship(back_populates="town", cascade="all, delete-orphan")

    def __init__(self, name=None):
        self.town_constructor = TownRandomizer.get_instance()
        if not name:
            self.name = self.town_constructor.randomize()
        else:
            self.name = name
        self.population_size = 1000
        self.geography  = Geography()

    def randomize(self):
        self.geography.randomize()

    def __repr__(self):
        return f'<User {self.name!r}>'

    def __size_description(self):
        return next((town_type for town_type, pop_threshold in reversed(self.SIZE_THRESHOLDS.items()) if pop_threshold < self.population_size), None)

    def __str__(self):
        description = f"{self.name} is {prefix_indefinite_article(self.geography.describe_town_geography())} {self.__size_description()}"
        return capitalize_sentences(description)
