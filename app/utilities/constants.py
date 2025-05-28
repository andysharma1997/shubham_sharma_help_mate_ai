import yaml
import json
import os.path as path
from app.utilities.singleton_factory import Singleton


class Constants(metaclass=Singleton):
    file_path = path.abspath(
        path.join(__file__, "../../resources/" + str("constants.yaml"))
    )
    
    with open(file_path, "r") as f:
        doc = yaml.safe_load(f)
    

    @classmethod
    def fetch_constant(cls, constant_name):
        return cls.doc[constant_name]
    