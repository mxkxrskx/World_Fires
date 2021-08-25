import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Index for automaticlly work
    lat = header_row.index('latitude')
    lon = header_row.index('longitude')
    s = header_row.index('brightness')
    daynight = header_row.index('daynight')

    #Lists for data
    lons, lats, squares, daynights = [], [], [], []
    for row in reader:
        lons.append(float(row[lon]))
        lats.append(float(row[lat]))
        squares.append(float(row[s]))
        daynights.append(row[daynight])

#Data visualization
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': daynights,
    'marker': {
    'color': squares,
    'opacity': 0.7,
    'size': 3,
    'colorscale': 'Rainbow',
    'colorbar': {'title': 'Fire Area'}
    }
}]

t = 'World Fires for one day'
my_layout = Layout(title=t)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_1d.html')
