from web_world_builder.utilities import load_json
import os

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return cls._instances[cls]
        else:
            print(f"{cls} singleton already initialized, use get_instance instead")

    def get_instance(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__()
        return cls._instances[cls]

class Randomizer(metaclass=SingletonMeta):

    def __init__(self):
        self.data_file_name = None

    def load_data(self):
        return self.load_data_file(self.data_file_name)

    def load_data_file(self, data_file_name):
        script_dir    = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, data_file_name)
        return load_json(abs_file_path)