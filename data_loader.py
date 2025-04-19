# f1_predictor/utils/data_loader.py

import pandas as pd
from f1_predictor.data import constants

def load_driver_data():
    data = {
        "Driver": constants.driver_list,
        "Abbreviation": [constants.driver_abbr[d] for d in constants.driver_list],
        "Team": [constants.driver_to_team[constants.driver_abbr[d]] for d in constants.driver_list],
        "TeamPoints": [constants.team_points[constants.driver_to_team[constants.driver_abbr[d]]] for d in constants.driver_list],
        "Points": [constants.driver_points[d] for d in constants.driver_list],
        "Qualifying": [constants.qualifying_performance[d] for d in constants.driver_list],
        "FastestLaps": [constants.fastest_laps[d] for d in constants.driver_list],
    }
    return pd.DataFrame(data)
