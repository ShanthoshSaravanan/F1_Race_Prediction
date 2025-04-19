# f1_predictor/utils/scoring.py

def calculate_score(driver):
    points_weight = 0.4
    team_weight = 0.2
    qualifying_weight = 0.2
    fastest_laps_weight = 0.2
    
    points_score = driver["Points"] / 100
    team_score = driver["TeamPoints"] / 200
    qualifying_score = driver["Qualifying"] / 10
    fastest_laps_score = driver["FastestLaps"] / 5
    
    return (points_weight * points_score +
            team_weight * team_score +
            qualifying_weight * qualifying_score +
            fastest_laps_weight * fastest_laps_score)
