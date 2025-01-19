from weakref import WeakKeyDictionary


class Positive:
    def __init__(self):
        self.instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.instance_data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f" value {value} is not positive.")
        self.instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")


class Planet:
    def __init__(
            self,
            name,
            radius_metres,
            mass_kilograms,
            orbital_period_seconds,
            surface_temperature_kelvin,
    ):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    # def _get_radius_metres(self):
    #     return self._radius_metres
    #
    # def _set_radius_metres(self, value):
    #     if value <= 0:
    #         raise ValueError(f"radius_metres value {value} is not positive.")
    #     self._radius_metres = value

    # radius_metres = property(fget=_get_radius_metres, fset=_set_radius_metres)
    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()

    # def _get_mass_kilograms(self):
    #     return self._mass_kilograms
    #
    # def _set_mass_kilograms(self, value):
    #     if value <= 0:
    #         raise ValueError(f"mass_kilograms value {value} is not positive.")
    #     self._mass_kilograms = value
    #
    # def _get_orbital_period_seconds(self):
    #     return self._orbital_period_seconds
    #
    # def _set_orbital_period_seconds(self, value):
    #     if value <= 0:
    #         raise ValueError(f"orbital_period_seconds value {value} is not positive.")
    #     self._orbital_period_seconds = value
    #
    # def _get_surface_temperature_kelvin(self):
    #     return self._surface_temperature_kelvin
    #
    # def _set_surface_temperature_kelvin(self, value):
    #     if value <= 0:
    #         raise ValueError(f"surface_temperature_kelvin value {value} is not positive.")
    #     self._surface_temperature_kelvin = value


pluto = Planet(
    name="Pluto",
    radius_metres=1184e3,
    mass_kilograms=1.305e22,
    orbital_period_seconds=7816012992,
    surface_temperature_kelvin=55,
)

print(pluto.radius_metres)
print(Positive.__get__(Planet.__dict__["radius_metres"], pluto, Planet))
