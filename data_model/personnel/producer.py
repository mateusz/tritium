from dataclasses import dataclass
from data_model.personnel.personnel import Personnel

@dataclass
class Producer(Personnel):
    """Personnel specialized in production"""
    pass 