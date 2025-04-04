from dataclasses import dataclass
from data_model.personnel.personnel import Personnel
from data_model.rank.researcher_rank import ResearcherRank
from typing import Optional

@dataclass
class Researcher(Personnel):
    """Personnel specialized in research"""
    leader_name: Optional[str] = None
    rank: ResearcherRank = ResearcherRank.TECHNICIAN 