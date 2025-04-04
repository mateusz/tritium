from data_model.game_progression.game_progression import GameProgression
from data_model.equipment.equipment import EquipmentType


class InitialProgress(GameProgression):
    """
    Initial game progression state.
    Defines the starting set of available technologies for a new game.
    """
    
    def _initialize_technologies(self) -> None:
        """Initialize the set of available technologies for the initial game state."""
        # Add the starting set of available technologies
        self._available_technologies.add(EquipmentType.DERRICK)
        self._available_technologies.add(EquipmentType.SHUTTLE_CHASSIS)
        self._available_technologies.add(EquipmentType.SHUTTLE_DRIVE)  # SHUTTLE_ENGINE in the requirements
        self._available_technologies.add(EquipmentType.CRYO_POD)
        self._available_technologies.add(EquipmentType.RESOURCE_POD)
        self._available_technologies.add(EquipmentType.TOOL_POD)
        self._available_technologies.add(EquipmentType.ORBITAL_FACTORY_FRAME) 