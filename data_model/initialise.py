from data_model.system.solar_system import SolarSystem
from data_model.location.planet import Planet
from data_model.location.moon import Moon
from data_model.location.asteroid import Asteroid
from data_model.resource.resource import Resource
from data_model.base.earth_base import EarthBase
from data_model.base.moon_base import MoonBase
from data_model.equipment.equipment import Equipment, EquipmentType


def initialize_solar_system() -> SolarSystem:
    """Initialize the Solar System with all planets, moons, and their resources."""
    solar_system = SolarSystem()
    
    # Mercury
    mercury = Planet()
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
    mars.resources = {
        Resource.IRON: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.SILVER: 100.0
    }
    solar_system.add_location(mars)
    
    # Mars' Moons
    phobos = Moon()
    phobos.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(phobos)
    
    deimos = Moon()
    deimos.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(deimos)
    
    # Asteroid Belt
    asteroid_belt = Asteroid()
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
    jupiter.resources = {
        Resource.HYDROGEN: 100.0,
        Resource.HELIUM: 100.0
    }
    solar_system.add_location(jupiter)
    
    # Jupiter's Moons
    amalthea = Moon()
    amalthea.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(amalthea)
    
    io = Moon()
    io.resources = {
        Resource.CARBON: 100.0,
        Resource.METHANE: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(io)
    
    europa = Moon()
    europa.resources = {
        Resource.CARBON: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(europa)
    
    ganymede = Moon()
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
    callisto.resources = {
        Resource.IRON: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.PLATINUM: 100.0
    }
    solar_system.add_location(callisto)
    
    leda = Moon()
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
    himalia.resources = {
        Resource.CARBON: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(himalia)
    
    elara = Moon()
    elara.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(elara)
    
    pasiphae = Moon()
    pasiphae.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(pasiphae)
    
    # Saturn
    saturn = Planet()
    saturn.resources = {
        Resource.HYDROGEN: 100.0
    }
    solar_system.add_location(saturn)
    
    # Saturn's Moons
    mimas = Moon()
    mimas.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(mimas)
    
    enceladus = Moon()
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
    dione.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(dione)
    
    rhea = Moon()
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
    iapet.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(iapet)
    
    phoebe = Moon()
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
    umbriel.resources = {
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(umbriel)
    
    titania = Moon()
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
    nereid.resources = {
        Resource.CARBON: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(nereid)
    
    n3 = Moon()
    n3.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(n3)
    
    n4 = Moon()
    n4.resources = {
        Resource.SILICA: 100.0
    }
    solar_system.add_location(n4)
    
    # Pluto
    pluto = Planet()
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
    charon.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(charon)
    
    decuria = Moon()
    decuria.resources = {
        Resource.TITANIUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.SILVER: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(decuria)
    
    return solar_system

