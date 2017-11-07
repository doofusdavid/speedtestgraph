# speedtestgraph
Python file to calculate speedtest and graph it to plotly

## Build

`pip install speedtest`

`pip install plotly`

`pip install pandas`

## Implementation

You'll need to sign up for an account on [plot.ly](http://plot.ly) and put your api_key and login into you ~/.plotly/.credentials file.

To get this running on windows, I set up a scheduled task to run "python speedtestgraph.py" every 30 minutes.  Created another scheduled task to run "python graphit.py" every 4 hours.  You should be able to see your results at http://plot.ly/YOURUSERNAME/

