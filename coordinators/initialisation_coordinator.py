from data_model.system.solar_system import SolarSystem
from data_model.location.planet import Planet
from data_model.location.moon import Moon
from data_model.location.asteroid import Asteroid
from data_model.resource.resource import Resource
from data_model.base.earth_base import EarthBase
from data_model.base.moon_base import MoonBase
from data_model.equipment.equipment import Equipment, EquipmentType
from coordinators.coordinator import Coordinator
from data_model.game_state import GameState


class InitialisationCoordinator(Coordinator):
    """
    Coordinator for initializing game components like the solar system.
    """
    
    def __init__(self, game_state: GameState):
        """
        Initialize the coordinator with a game state.
        
        Args:
            game_state: The current game state
        """
        super().__init__(game_state)
    
    def initialize_solar_system(self) -> SolarSystem:
        """Initialize the Solar System with all planets, moons, and their resources."""
        solar_system = SolarSystem()
        
        # Mercury
        mercury = Planet()
        mercury.name = 'Mercury'
        mercury.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(mercury)
        
        # Venus
        venus = Planet()
        venus.name = 'Venus'
        venus.resources = {
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PLATINUM: 100.0
        }
        solar_system.add_location(venus)
        
        # Earth
        earth = Planet()
        earth.name = 'Earth'
        earth.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0
        }
        solar_system.add_location(earth)

        earth_base = EarthBase()
        earth_base.add_equipment(EquipmentType.DERRICK, 1)
        earth.set_resource_base(earth_base)
        
        # Earth's Moon
        moon = Moon()
        moon.name = 'Moon'
        moon.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(moon)

        moon_base = MoonBase()
        moon.set_resource_base(moon_base) 

        # Mars
        mars = Planet()
        mars.name = 'Mars'
        mars.resources = {
            Resource.IRON: 100.0,
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.SILVER: 100.0
        }
        solar_system.add_location(mars)
        
        # Mars' Moons
        phobos = Moon()
        phobos.name = 'Phobos'
        phobos.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(phobos)
        
        deimos = Moon()
        deimos.name = 'Deimos'
        deimos.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(deimos)
        
        # Asteroid Belt
        asteroid_belt = Asteroid()
        asteroid_belt.name = 'Asteroid Belt'
        asteroid_belt.resources = {
            Resource.TITANIUM: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.SILVER: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(asteroid_belt)
        
        # Jupiter
        jupiter = Planet()
        jupiter.name = 'Jupiter'
        jupiter.resources = {
            Resource.HYDROGEN: 100.0,
            Resource.HELIUM: 100.0
        }
        solar_system.add_location(jupiter)
        
        # Jupiter's Moons
        amalthea = Moon()
        amalthea.name = 'Amalthea'
        amalthea.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(amalthea)
        
        io = Moon()
        io.name = 'Io'
        io.resources = {
            Resource.CARBON: 100.0,
            Resource.METHANE: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(io)
        
        europa = Moon()
        europa.name = 'Europa'
        europa.resources = {
            Resource.CARBON: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(europa)
        
        ganymede = Moon()
        ganymede.name = 'Ganymede'
        ganymede.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(ganymede)
        
        callisto = Moon()
        callisto.name = 'Callisto'
        callisto.resources = {
            Resource.IRON: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.COPPER: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.PLATINUM: 100.0
        }
        solar_system.add_location(callisto)
        
        leda = Moon()
        leda.name = 'Leda'
        leda.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.COPPER: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(leda)
        
        himalia = Moon()
        himalia.name = 'Himalia'
        himalia.resources = {
            Resource.CARBON: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(himalia)
        
        elara = Moon()
        elara.name = 'Elara'
        elara.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(elara)
        
        pasiphae = Moon()
        pasiphae.name = 'Pasiphae'
        pasiphae.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(pasiphae)
        
        # Saturn
        saturn = Planet()
        saturn.name = 'Saturn'
        saturn.resources = {
            Resource.HYDROGEN: 100.0
        }
        solar_system.add_location(saturn)
        
        # Saturn's Moons
        mimas = Moon()
        mimas.name = 'Mimas'
        mimas.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(mimas)
        
        enceladus = Moon()
        enceladus.name = 'Enceladus'
        enceladus.resources = {
            Resource.IRON: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(enceladus)
        
        tethys = Moon()
        tethys.name = 'Tethys'
        tethys.resources = {
            Resource.TITANIUM: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.COPPER: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(tethys)
        
        dione = Moon()
        dione.name = 'Dione'
        dione.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(dione)
        
        rhea = Moon()
        rhea.name = 'Rhea'
        rhea.resources = {
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.SILVER: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(rhea)
        
        titan = Moon()
        titan.name = 'Titan'
        titan.resources = {
            Resource.TITANIUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.SILVER: 100.0,
            Resource.GOLD: 100.0
        }
        solar_system.add_location(titan)
        
        hyperion = Moon()
        hyperion.name = 'Hyperion'
        hyperion.resources = {
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(hyperion)
        
        iapet = Moon()
        iapet.name = 'Iapet'
        iapet.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(iapet)
        
        phoebe = Moon()
        phoebe.name = 'Phoebe'
        phoebe.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(phoebe)
        
        # Uranus
        uranus = Planet()
        uranus.name = 'Uranus'
        uranus.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.COPPER: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.HELIUM: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(uranus)
        
        # Uranus' Moons
        miranda = Moon()
        miranda.name = 'Miranda'
        miranda.resources = {
            Resource.IRON: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.SILVER: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(miranda)
        
        ariel = Moon()
        ariel.name = 'Ariel'
        ariel.resources = {
            Resource.ALUMINUM: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(ariel)
        
        umbriel = Moon()
        umbriel.name = 'Umbriel'
        umbriel.resources = {
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(umbriel)
        
        titania = Moon()
        titania.name = 'Titania'
        titania.resources = {
            Resource.IRON: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.SILVER: 100.0,
            Resource.GOLD: 100.0
        }
        solar_system.add_location(titania)
        
        oberon = Moon()
        oberon.name = 'Oberon'
        oberon.resources = {
            Resource.IRON: 100.0,
            Resource.TITANIUM: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(oberon)
        
        # Neptune
        neptune = Planet()
        neptune.name = 'Neptune'
        neptune.resources = {
            Resource.IRON: 100.0,
            Resource.ALUMINUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.COPPER: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.PLATINUM: 100.0
        }
        solar_system.add_location(neptune)
        
        # Neptune's Moons
        triton = Moon()
        triton.name = 'Triton'
        triton.resources = {
            Resource.TITANIUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.DEUTERIUM: 100.0,
            Resource.METHANE: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(triton)
        
        nereid = Moon()
        nereid.name = 'Nereid'
        nereid.resources = {
            Resource.CARBON: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(nereid)
        
        n3 = Moon()
        n3.name = 'N3'
        n3.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(n3)
        
        n4 = Moon()
        n4.name = 'N4'
        n4.resources = {
            Resource.SILICA: 100.0
        }
        solar_system.add_location(n4)
        
        # Pluto
        pluto = Planet()
        pluto.name = 'Pluto'
        pluto.resources = {
            Resource.CARBON: 100.0,
            Resource.HYDROGEN: 100.0,
            Resource.METHANE: 100.0,
            Resource.PALLADIUM: 100.0,
            Resource.PLATINUM: 100.0,
            Resource.GOLD: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(pluto)
        
        # Pluto's Moons
        charon = Moon()
        charon.name = 'Charon'
        charon.resources = {
            Resource.CARBON: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(charon)
        
        decuria = Moon()
        decuria.name = 'Decuria'
        decuria.resources = {
            Resource.TITANIUM: 100.0,
            Resource.CARBON: 100.0,
            Resource.SILVER: 100.0,
            Resource.SILICA: 100.0
        }
        solar_system.add_location(decuria)
        
        self.game_state.solar_system = solar_system