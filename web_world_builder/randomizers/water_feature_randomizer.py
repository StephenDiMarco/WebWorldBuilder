from web_world_builder.utilities import select_random_list_value
from web_world_builder.randomizers.randomizer_base import Randomizer

class WaterFeatureRandomizer(Randomizer):

    DEFAULT_NAME = "Mira"

    def __init__(self):
        self.data_file_name = 'water_feature_data\\water_feature_data.json'
        self.water_feature_names = []
        self.__load_water_feature_names()

    def __load_water_feature_names(self):
        json_data = self.load_data()
        self.water_feature_names = [self.DEFAULT_NAME]
        if json_data:
            self.water_feature_names = json_data
        else:
            print("Attention: No Waterway json file provided")

    def randomize_name(self):
        return select_random_list_value(self.water_feature_names)

    def randomize_type(self):
        return select_random_list_value(["Stream", "Brook", "Creek", "Gully", "River", "Lake", "Pond", "Marsh"])
