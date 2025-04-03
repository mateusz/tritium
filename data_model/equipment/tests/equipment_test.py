import unittest
from data_model.equipment.equipment import Equipment, EquipmentType, RequiredLocation
from data_model.resource.resource import Resource

class EquipmentTest(unittest.TestCase):
    
    def test_get_research_technician_days(self):
        """Test the calculation of research technician-days for different equipment configurations."""
        
        # Test case 1: Basic equipment with no rank or costs specified
        basic_equipment = Equipment(type=EquipmentType.DERRICK)
        self.assertEqual(basic_equipment.get_research_technician_days(), 700)
        
        # Test case 2: Equipment with rank but no rare resources
        ranked_equipment = Equipment(
            type=EquipmentType.AUTO_OPERATIONS_COMPUTER, 
            required_rank=2,
            costs={
                Resource.IRON: 10,
                Resource.ALUMINUM: 5,
                Resource.CARBON: 3
            }
        )
        self.assertEqual(ranked_equipment.get_research_technician_days(), 1400)  # 700 * 2 * 1
        
        # Test case 3: Equipment with one rare resource
        single_rare_equipment = Equipment(
            type=EquipmentType.FUZ_LASER, 
            required_rank=1,
            costs={
                Resource.IRON: 20,
                Resource.COPPER: 5,
                Resource.GOLD: 1  # Rare resource
            }
        )
        self.assertEqual(single_rare_equipment.get_research_technician_days(), 840)  # 700 * 1 * 1.2
        
        # Test case 4: High rank equipment with multiple rare resources
        complex_equipment = Equipment(
            type=EquipmentType.HYPERSPACE, 
            required_rank=3,
            costs={
                Resource.TITANIUM: 50,
                Resource.PALLADIUM: 10,  # Rare resource
                Resource.PLATINUM: 5,    # Rare resource
                Resource.DEUTERIUM: 20   # Rare resource
            }
        )
        self.assertEqual(complex_equipment.get_research_technician_days(), 3360)  # 700 * 3 * 1.6
        
        # Test case 5: Highest rank equipment with all rare resources
        advanced_equipment = Equipment(
            type=EquipmentType.COMPLETE_ARTIFACT, 
            required_rank=5,
            costs={
                Resource.PALLADIUM: 50,  # Rare resource
                Resource.PLATINUM: 30,   # Rare resource
                Resource.SILVER: 20,     # Rare resource
                Resource.GOLD: 10,       # Rare resource
                Resource.DEUTERIUM: 100  # Rare resource
            }
        )
        self.assertEqual(advanced_equipment.get_research_technician_days(), 7000)  # 700 * 5 * 2.0

if __name__ == '__main__':
    unittest.main() 