import requests
from typing import Dict, List, Tuple
from requests.exceptions import HTTPError
from datetime import date

# import urllib.error
# import urllib.request
import functools

base_urls = {
    'rotowire': 'https://www.rotowire.com/',
    'historic': 'http://www.pro-football-reference.com/',
    'roster': 'http://www.nfl.com/teams/roster',
    # 'gsis_profile': 'http://www.nfl.com/players/profile',
    # f'years/{2019}/fantasy.htm'
}
previous_season = date.today().year - 1

view_values = "passing rushing receiving kicking defense".split()
type_values = "basic advanced redzone fantasy".split()
pergame_values = "totals pergame".split()
season = [previous_season, previous_season-4, -1]
timeperiod = ['season', map(str, range(1, 17))]
# resource = f'football/tables/player-stats.php?view={view}&type={stat_type}&season={season}&pergame={stat_format}' \
#            f'&timeperiod={time_period}'
param_keys = ['view', 'type', 'season', 'pergame', 'timeperiod']


# response = urllib.request.urlopen(LATEST_URL)
# data = json.loads(response.read())
# current = pd.DataFrame.from_dict(data["draftables"])
def run():
    pass


def get_param_di(params_keys: List, param_value: List) -> Dict:
    return dict(zip(params_keys, param_value))





if __name__ == '__main__':
    run()
