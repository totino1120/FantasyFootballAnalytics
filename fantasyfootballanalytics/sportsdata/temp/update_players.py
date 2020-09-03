import requests
from typing import Dict, List, Tuple
from requests.exceptions import HTTPError
from datetime import date

# import urllib.error
# import urllib.request
import functools



# response = urllib.request.urlopen(LATEST_URL)
# data = json.loads(response.read())
# current = pd.DataFrame.from_dict(data["draftables"])
def run():
    pass


def get_param_di(params_keys: List, param_value: List) -> Dict:
    return dict(zip(params_keys, param_value))





if __name__ == '__main__':
    run()
