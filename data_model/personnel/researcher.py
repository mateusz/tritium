from dataclasses import dataclass
from data_model.personnel.personnel import Personnel

@dataclass
class Researcher(Personnel):
    """Personnel specialized in research"""
    pass 