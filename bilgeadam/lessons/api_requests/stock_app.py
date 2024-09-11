import requests
import pandas as pd
import plotly.graph_objects as go


api_key = "your_api_key"

# hangi hisse senedini
symbol = input("please enter stock symbol")

# alpha vantage api url
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

# apiden veri cekme
res = requests.get(url)
data = res.json()
print(res.status_code)

# json verilerini pandas DataFrame'e donusturmek
df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
print(df)

# dataframe sutunlarını yeniden ısımlendir
df.columns = ["open", "high", "low", "close", "volume"]
print(df)

# dataframe deki verileri sayısal formata cevirmek
df = df.apply(pd.to_numeric)
df.info()

# verileri indekste verilen tarihe gore sıralamak
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# plotly ile gorsellestirme
fig = go.Figure(data=[go.Candlestick(
                x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.update_layout(
    title="CandleStick Chart",
    yaxis_title="IBM Stock ($)",
    xaxis_title="Date"
)

fig.show()
