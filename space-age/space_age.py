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