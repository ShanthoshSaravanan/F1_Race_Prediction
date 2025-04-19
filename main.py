# main.py

from tabulate import tabulate
from f1_predictor.utils.data_loader import load_driver_data
from f1_predictor.utils.scoring import calculate_score

def main():
    df = load_driver_data()
    df["Score"] = df.apply(calculate_score, axis=1)
    top_drivers = df.nlargest(20, "Score")[["Driver", "Score", "Team", "Points", "TeamPoints", "Qualifying", "FastestLaps"]]
    
    print("Driver Rankings:")
    print("----------------")
    print(tabulate(top_drivers, headers='keys', tablefmt='psql'))

if __name__ == "__main__":
    main()
