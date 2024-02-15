
# Set up env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 


# To run test
python -m unittest

# Gitflow
https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow
1 ) create branch
git checkout -b nouvelle_branche
2 ) code in the branch

# Step 1 : data processing
python -m curator
Result : curated csv in data folder

# Step 2 : backtest model
python -m backtester
Result : test csv in data folder
