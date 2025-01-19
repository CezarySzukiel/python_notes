class Object:

    def __getattribute__(self, name):
        cls = type(self)

        if hasattr(cls, "__slots__"):
            if name in cls.__slots__:
                index = cls.__slots__.index(name)
                return self.slot_array[index]

        if name in vars(self):
            return vars(self)[name]

        if hasattr(cls, name):
            return getattr(cls, name)

        if hasattr(cls, "__getattr__"):
            return cls.__getattr__(self, name)

        raise AttributeError(f"{cls.__name__} has no attribute {name}")