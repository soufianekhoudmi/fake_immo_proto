
# Set up env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 


# To run test
python -m unittest


# Step 1 : data processing
python -m curator
Result : curated csv in data folder

# Step 2 : backtest model
python -m backtester
Result : test csv in data folder
