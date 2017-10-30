import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py

df = pd.read_csv('results.csv')

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
