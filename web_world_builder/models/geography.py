from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from web_world_builder.utilities import random_occurance, capitalize_sentences, random_occurance_boolean
from web_world_builder.models.water_feature import WaterFeature
from web_world_builder.sqlite_db_manager import Base


class Geography(Base):

    __tablename__ = 'geography'
    __table_args__ = {'extend_existing': True} 
    id: Mapped[int] = mapped_column(primary_key=True)
    is_coastal = Column(Boolean())
    town_id: Mapped[int] = mapped_column(ForeignKey("towns.id"))
    town: Mapped["Town"] = relationship(back_populates="geography")

    WATER_FEATURE_PROBABILITY = 0.80
    BOUNDARY_KEY     = "boundary"
    PASS_THROUGH_KEY = "pass through"
    BOUNDARY_WATER_FEATURE_PROBABILITY = 0.5

    def __init__(self):
        self.is_coastal = False
        self.water_features = {self.BOUNDARY_KEY: [], self.PASS_THROUGH_KEY: []}

    def randomize(self):
        self.is_coastal = random_occurance_boolean()
        while random_occurance(self.WATER_FEATURE_PROBABILITY):
            water_feature = WaterFeature()
            water_feature.randomize()
            if random_occurance(self.BOUNDARY_WATER_FEATURE_PROBABILITY):
                self.water_features[self.BOUNDARY_KEY].append(water_feature)
            else:
                self.water_features[self.PASS_THROUGH_KEY].append(water_feature)

    def __str__(self):
        description = self.describe_town_geography()
        description += self.describe_water_features()
        return description

    def describe_town_geography(self):
        if self.is_coastal:
            return "coastal"
        else:
            return "inland"

    def describe_water_features(self):
        description = ""

        if not self.water_features[self.BOUNDARY_KEY] and not self.water_features[self.PASS_THROUGH_KEY]:
            return capitalize_sentences("has no notable bodies of water.")

        if self.water_features[self.BOUNDARY_KEY]:
            water_features = self.__describe_water_features_by_type(self.water_features[self.BOUNDARY_KEY])
            description += water_features + " border the town. " if water_features.find(",") != -1 else water_features + " borders the town. "

        if self.water_features[self.PASS_THROUGH_KEY]:
            description += self.__describe_water_features_by_type(self.water_features[self.PASS_THROUGH_KEY]) + " can be found within the town."

        return capitalize_sentences(description)

    def __describe_water_features_by_type(self, water_features):
        description = ""
        if len(water_features) == 1:
            description += str(water_features[0])
        if len(water_features) == 2:
            description += str(water_features[0]) + ', and '
            description += str(water_features[1])
        elif len(water_features) > 2:
            description += str(water_features[0])
            for water_feature in water_features[1:-1]:
                description += ', ' + str(water_feature)
            description += ", and " + str(water_features[-1])
        return description