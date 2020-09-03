class NFLStats:
    """NFL Abstract Stats Class"""
    def __init__(self, source_factory=None):
        """pet_factory is our abstract factory.
        We can set it at will."""
        self.stat_factory = source_factory

    def show_pet(self):
        """Creates and shows a pet using the
        abstract factory"""

        stat_source = self.stat_factory.get_pet()
        print
        "This is a lovely", pet
        print
        "It says", pet.speak()
        print
        "It eats", self.pet_factory.get_food()

    def __repr__(self):
        # return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)
        return f'Pizza({self.radius} - {self.ingredients})'

    @classmethod
    def rotowire(cls):
        """ Class Method Definition
            Can't modify object instance state
            Can modify class state"""
        return cls(4.5, ['cheese', 'tomatoes'])

    @classmethod
    def mmfl(cls):
        """ Class Method Definition
            Can't modify object instance state
            Can modify class state"""
        return cls(4.5, ['cheese', 'tomatoes'])