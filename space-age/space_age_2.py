EARTH_ORBITAL_PERIOD_IN_SEC = 31557600

PLANET_YEARS_RELATIVE = dict(
    Mercury=0.2408467,
    Venus=0.61519726,
    Earth=1.0,
    Mars=1.8808158,
    Jupiter=11.862615,
    Saturn=29.447498,
    Uranus=84.016846,
    Neptune=164.79132
)


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

        for planet in PLANET_YEARS_RELATIVE:
            self.add_function(planet)

    def add_function(self, planet):
        setattr(self, 'on_' + planet.lower(), lambda: self.calc_years(planet))

    def calc_years(self, planet):
        return round(self.seconds / (PLANET_YEARS_RELATIVE[planet] * EARTH_ORBITAL_PERIOD_IN_SEC), 2)


q = SpaceAge(1000000000).on_earth(), 31.69
q
q = SpaceAge(2134835688).on_mercury(), 280.88
q
q = SpaceAge(189839836).on_venus(), 9.78
q
q = SpaceAge(2129871239).on_mars(), 35.88
q
q = SpaceAge(901876382).on_jupiter(), 2.41
q
q = SpaceAge(2000000000).on_saturn(), 2.15
q
q = SpaceAge(1210123456).on_uranus(), 0.46
q
q = SpaceAge(1821023456).on_neptune(), 0.35
q
