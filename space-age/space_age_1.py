class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.orbital_period = dict(
            EARTH=31557600,
            MERCURY=0.2408467,
            VENUS=0.61519726,
            MARS=1.8808158,
            JUPITER=11.862615,
            SATURN=29.447498,
            URANUS=84.016846,
            NEPTUNE=164.79132
        )

    def on_earth(self):
        return round(self.seconds / self.orbital_period['EARTH'], 2)

    def on_mercury(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['MERCURY']), 2)

    def on_venus(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['VENUS']), 2)

    def on_mars(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['MARS']), 2)

    def on_jupiter(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['JUPITER']), 2)

    def on_saturn(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['SATURN']), 2)

    def on_uranus(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['URANUS']), 2)

    def on_neptune(self):
        return round(self.seconds / (self.orbital_period['EARTH'] * self.orbital_period['NEPTUNE']), 2)


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
