from isoduration.formatter import check_global_sign


class Programmer:
    def __init__(self, value):
        self.experience = value

    def set_experience(self, new_value):
        if new_value < 0:
            raise ValueError("Experience cannot be negative")

        self.experience = new_value
        self.experience = new_value

    @property
    def experience(self):
        return f'self._experience years'

    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError(f'Experience cannot be negative')
        self._experience = value

    def get_experience(self):
        return self.experience

    experience = property(get_experience, set_experience)

    def __str__(self):
        if self.experience <= 5:
            title = "junior"
        elif self.experience <= 10:
            title = "regular"
        else:
            title = "senior"
        return f'{self.experience} - {title}'


Rysiu = Programmer(3)
print(dir(Rysiu))
# Rysiu.set_experience(12)
# Rysiu._experience = - 10
# Rysiu.experience = 12

# print(Rysiu.get_experience)
print(Rysiu)
# print(help(property))
