import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py

# convert date column to actual datetime
df = pd.read_csv('results.csv', parse_dates=[0], date_parser=lambda x: pd.to_datetime(x))

# convert column to date in my timezone
df["Date"] = df['Date'].dt.tz_localize('UTC').dt.tz_convert('America/Denver')

download_trace = go.Scatter(
    x=df['Date'],
    y=df['Download'],
    mode="lines+markers",
    name="Download"
)
ping_trace = go.Scatter(
    x=df['Date'],
    y=df['Ping'],
    mode="lines+markers",
    name="Ping"
)
upload_trace = go.Scatter(
    x=df['Date'],
    y=df['Upload'],
    mode="lines+markers",
    name="Upload"
)

layout = go.Layout(title='TDS Speedtest',
                   plot_bgcolor='rgb(230, 230,230)')
fig = go.Figure(data=[download_trace, upload_trace, ping_trace], layout=layout)

py.plot(fig, filename="download", auto_open=False)
