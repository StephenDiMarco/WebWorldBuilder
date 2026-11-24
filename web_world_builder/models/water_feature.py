from web_world_builder.randomizers.water_feature_randomizer import WaterFeatureRandomizer
from web_world_builder.utilities import name_is_possesive

class WaterFeature:

    def __init__(self):
        self.type = None
        self.name = None

    def randomize(self):
        self.type = WaterFeatureRandomizer.get_instance().randomize_type()
        self.name = WaterFeatureRandomizer.get_instance().randomize_name()

    def __str__(self):
        return f"{self.__prefix_possible_possessive_with_definite_article(self.name)} {self.type}"

    def __prefix_possible_possessive_with_definite_article(self, name):
        if name_is_possesive(self.name) or self.type in ["Lake", "Pond", "Marsh"]:
            return name
        else:
            return f"the {name}"