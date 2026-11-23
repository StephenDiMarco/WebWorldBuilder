from web_world_builder.utilities import select_random_list_value
from web_world_builder.randomizers.randomizer_base import Randomizer

class TownRandomizer(Randomizer):

    DEFAULT_NAME = "Cedar Brook"

    def __init__(self):
        self.data_file_name = 'town_data\\town_names.json'
        self.town_names = []
        self.__load_town_names()
        self.error = None

    def __load_town_names(self):
        json_data = self.load_data()
        self.town_names = [self.DEFAULT_NAME]
        if json_data:
            if "names" in json_data.keys():
                self.town_names = json_data["names"]
            else:
              self.error = "Warning: Malformed json configuration for town names"
        else:
            self.error = "Attention: No town name json file provided"

    def randomize(self):
        return select_random_list_value(self.town_names)