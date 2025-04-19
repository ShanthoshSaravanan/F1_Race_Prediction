# f1_predictor/data/constants.py

driver_list = [
    "Lando Norris", "Oscar Piastri", "Max Verstappen", "George Russell",
    "Charles Leclerc", "Kimi Antonelli", "Lewis Hamilton", "Alexander Albon",
    "Esteban Ocon", "Lance Stroll", "Pierre Gasly", "Nico Hulkenberg",
    "Oliver Bearman", "Yuki Tsunoda", "Isack Hadjar", "Carlos Sainz",
    "Fernando Alonso", "Liam Lawson", "Jack Doohan", "Gabriel Bortoleto"
]

driver_abbr = {
    "Lando Norris": "NOR", "Oscar Piastri": "PIA", "Max Verstappen": "VER", "George Russell": "RUS",
    "Charles Leclerc": "LEC", "Kimi Antonelli": "ANT", "Lewis Hamilton": "HAM", "Alexander Albon": "ALB",
    "Esteban Ocon": "OCO", "Lance Stroll": "STR", "Pierre Gasly": "GAS", "Nico Hulkenberg": "HUL",
    "Oliver Bearman": "OLI", "Yuki Tsunoda": "TSU", "Isack Hadjar": "HAD", "Carlos Sainz": "SAI",
    "Fernando Alonso": "ALO", "Liam Lawson": "LAW", "Jack Doohan": "DOO", "Gabriel Bortoleto": "GAB"
}

driver_to_team = {
    "NOR": "McLaren", "PIA": "McLaren", "VER": "Red Bull", "RUS": "Mercedes",
    "LEC": "Ferrari", "ANT": "Mercedes", "HAM": "Ferrari", "ALB": "Williams",
    "OCO": "Haas", "STR": "Aston Martin", "GAS": "Alpine", "HUL": "Kick Sauber",
    "OLI": "Haas", "TSU": "Red Bull", "HAD": "Racing Bulls", "SAI": "Williams",
    "ALO": "Aston Martin", "LAW": "Racing Bulls", "DOO": "Alpine", "GAB": "Kick Sauber"
}

team_points = {
    "McLaren": 151, "Mercedes": 93, "Red Bull": 71, "Williams": 19, "Ferrari": 57,
    "Haas": 20, "Aston Martin": 10, "Kick Sauber": 6, "Racing Bulls": 7, "Alpine": 6
}

driver_points = {
    "Lando Norris": 77, "Oscar Piastri": 74, "Max Verstappen": 69, "George Russell": 63,
    "Charles Leclerc": 32, "Kimi Antonelli": 30, "Lewis Hamilton": 25, "Alexander Albon": 18,
    "Esteban Ocon": 14, "Lance Stroll": 10, "Pierre Gasly": 6, "Nico Hulkenberg": 6,
    "Oliver Bearman": 6, "Yuki Tsunoda": 5, "Isack Hadjar": 4, "Carlos Sainz": 1,
    "Fernando Alonso": 0, "Liam Lawson": 0, "Jack Doohan": 0, "Gabriel Bortoleto": 0
}

qualifying_performance = {
    "Lando Norris": 8, "Oscar Piastri": 7, "Max Verstappen": 9, "George Russell": 6,
    "Charles Leclerc": 8, "Kimi Antonelli": 5, "Lewis Hamilton": 7, "Alexander Albon": 4,
    "Esteban Ocon": 5,
