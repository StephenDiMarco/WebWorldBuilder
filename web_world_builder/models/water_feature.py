from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from web_world_builder.randomizers.water_feature_randomizer import WaterFeatureRandomizer
from web_world_builder.utilities import name_is_possesive, random_occurance
from web_world_builder.sqlite_db_manager import Base

class WaterFeature(Base):

    __tablename__ = 'water_feature'
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(50))
    type = Column(String(50))
    is_boundary_feature = Column(Boolean())
    geography_id: Mapped[int] = mapped_column(ForeignKey("geography.id"))

    def __init__(self):
        self.type = None
        self.name = None
        self.is_boundary_feature = False

    BOUNDARY_WATER_FEATURE_PROBABILITY = 0.5

    def randomize(self):
        self.type = WaterFeatureRandomizer.get_instance().randomize_type()
        self.name = WaterFeatureRandomizer.get_instance().randomize_name()
        self.is_boundary_feature =  random_occurance(self.BOUNDARY_WATER_FEATURE_PROBABILITY)

    def __str__(self):
        return f"{self.__prefix_possible_possessive_with_definite_article(self.name)} {self.type}"

    def __prefix_possible_possessive_with_definite_article(self, name):
        if name_is_possesive(self.name) or self.type in ["Lake", "Pond", "Marsh"]:
            return name
        else:
            return f"the {name}"
