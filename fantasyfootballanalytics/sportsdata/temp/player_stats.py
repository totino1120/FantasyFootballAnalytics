from typing import Dict, List, Tuple
from datetime import date

previous_season = date.today().year - 1
stat_values = "passing rushing receiving kicking defense".split()
stat_type = "basic advanced redzone fantasy".split()
stat_format = "totals pergame".split()
stat_season = [previous_season, previous_season-4, -1]
stat_period = ['season', map(str, range(1, 17))]

# stat_pos = 'qb rb wr te k dst'.split()
# stat_pos = 'draft'.split()

class NFLStats:
    def __init__(self, site_name: str, url_host: str, keys_list: List):
        """pet_factory is our abstract factory.
        We can set it at will."""
        self.site_name = site_name
        self.url_host = url_host
        self.keys_list = keys_list

    def __repr__(self):
        return f'{self.__class__.__name__}({self.url_host} - {self.keys_list})'

    @classmethod
    def rotowire(cls):
        """ Class Method Definition
            Can't modify object instance state
            Can modify class state"""
        param_keys = ['view', 'type', 'season', 'pergame', 'timeperiod']
        base_url = 'https://www.rotowire.com/football/player-stats.php'
        return cls('rotowire', base_url, param_keys)

    @classmethod
    def mmfl(cls):
        """ Class Method Definition
            Can't modify object instance state
            Can modify class state"""
        return cls(4.5, ['cheese', 'tomatoes'])

    @classmethod
    def fantasypros(cls):
        """ Class Method Definition
            Can't modify object instance state
            Can modify class state"""
        param_keys = ['week']
        base_url = 'www.fantasypros.com/nfl/projections/'
        return cls('fantasypros', base_url, param_keys)
