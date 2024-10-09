# Project Name

## Tracking Script Setup

The scripts were designed to track 5 year historical price data and PE ratios as of 2024-06-30 of S&P500 constituents. Feel free to update it.

## Data Scraping and Processing Instructions

1. **Scraping Data from Gurufocus.com:**
   - Run `Final_EPS_TTM.py` to scrape data from Gurufocus.com.
   - Create a premium account or utilize the free trial.
   - Insert your own cookies before running the script.
   - This will generate the `EPS.csv` file in the repository.

2. **Resampling Data:**
   - Execute `Final_EPS_TTM.py` to resample the data in `EPS.csv`, spreading quarterly EPS to daily intervals.
   - After running this script, `Final_EPS_TTM.csv` will be generated.

3. **Merging Price and EPS Data:**
   - Run `Merged_Final_PE.py` to merge price and EPS data, calculating the Price-Earnings (PE) ratio.
   - The output will be saved in `PE_Final.csv`.

## Important Note

Make sure to follow the steps in the specified order for successful data tracking and processing.
