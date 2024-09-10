
import plotly.express as px

## https://plotly.com/python/bar-charts/
## 2024-Sep-09

data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()