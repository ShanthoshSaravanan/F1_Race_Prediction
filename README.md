# F1_Race_Prediction
This model is built to determine the winner of Saudi Arabian grand prix in 2025 formula 1. so the algorithm used here is Linear Model based on Weighted Scoring System

# 🏎️ F1 Race Predictor

This project predicts driver rankings in Formula 1 based on the below features for the Saudi Arabian grand prix:
- Driver points
- Team points
- Qualifying performance
- Fastest laps

### 📁 Structure

- `data/constants.py`: All driver and team metadata
- `utils/data_loader.py`: Converts data into a structured DataFrame
- `utils/scoring.py`: Scoring formula to rank drivers
- `main.py`: Main script to execute the prediction

### 🚀 Run It

```bash
python main.py

