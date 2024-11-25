class Temperature:
    def __init__(self, temp):
        self.temp_c = temp

    @property
    def temp_c(self):
        return f'{self._temp_c:.2f} °C'

    @temp_c.setter
    def temp_c(self, value):
        if value < -273.15:
            raise ValueError(f'Temperature is to low.')
        self._temp_c = value

    @property
    def temp_f(self):
        return f'{32 + 9 / 5 * self._temp_c:.2f} °F'

    @temp_f.setter
    def temp_f(self, value):
        self.temp_c = 5 / 9 * (value - 32)

    @property
    def temp_k(self):
        return f'{self._temp_c + 273.15:.2f} K'

    @temp_k.setter
    def temp_k(self, value):
        self.temp_c = value - 273.15

    def __str__(self):
        return str(self.temp_c)


t1 = Temperature(0)
print(t1.temp_c)
print(t1.temp_f)
print(t1.temp_k)
t1.temp_k = -0.0001
print(t1.temp_c)
print(t1.temp_f)
print(t1.temp_k)