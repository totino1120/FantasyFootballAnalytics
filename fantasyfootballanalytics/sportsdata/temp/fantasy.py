"""
*What is this pattern about?

In Java and other languages, the Abstract Factory Pattern serves to provide an interface for
creating related/dependent objects without need to specify their
actual class.

The idea is to abstract the creation of objects depending on business
logic, platform choice, etc.

In Python, the interface we use is simply a callable, which is "builtin" interface
in Python, and in normal circumstances we can simply use the class itself as
that callable, because classes are first class objects in Python.

*What does this example do?
This particular implementation abstracts the creation of a pet and
does so depending on the factory we chose (Dog or Cat, or random_animal)
This works because both Dog/Cat and random_animal respect a common
interface (callable for creation and .speak()).
Now my application can create pets abstractly and decide later,
based on my own criteria, dogs over cats.

*Where is the pattern used practically?

*References:
https://sourcemaking.com/design_patterns/abstract_factory
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

*TL;DR
Provides a way to encapsulate a group of individual factories.
"""


class StatsShop:

    """A Stats shop"""

    def __init__(self, stats_factory=None):
        """stat_factory is our abstract factory.  We can set it at will."""
        self.sport_factory = stats_factory

    def show_sport(self):
        """Creates and shows a pet using the abstract factory"""
        sport = self.sport_factory()
        # print("We have a lovely {}".format(pet))
        sport.base_url()


class RotoWire:


    def __str__(self):
        return "Rotowire"

    def get_data(self):

        pass


class FantasyPros:
    def base_url(self):
        return 'www.fantasypros.com/nfl/projections/'

    def __str__(self):
        return "FantasyPros"


# Additional factories:

# Create a random animal
def random_animal():
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])()


# Show pets with various factories
def main():
    """
    # A Shop that sells only cats

    """
    rotowire_stats = StatsShop(RotoWire)
    rotowire_stats.show_sport()

    # A shop that sells random animals
    >>> shop = PetShop(random_animal)
    >>> for i in range(3):
    ...    shop.show_pet()
    ...    print("=" * 20)
    We have a lovely Cat
    It says meow
    ====================
    We have a lovely Dog
    It says woof
    ====================
    We have a lovely Dog
    It says woof
    ====================
    """


if __name__ == "__main__":
    random.seed(1234)  # for deterministic doctest outputs
    import doctest

    doctest.testmod()
