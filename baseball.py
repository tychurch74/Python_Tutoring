
import pandas as pd
from datetime import datetime, timedelta
from pybaseball import batting_stats


def fangraphs_batting(start_season, end_season):

    start_season = int(start_season)
    end_season = int(end_season)

    fangraphs_batting_df = batting_stats(start_season, end_season, qual=0).sort_values("Name")

    return fangraphs_batting_df

data = fangraphs_batting(2024,2024)

# Save to CSV
data.to_csv('batting_data.csv', index=False) 

print(data)

