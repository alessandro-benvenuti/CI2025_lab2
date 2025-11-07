import matplotlib.pyplot as plt
import requests

CITIES = [
    "Rome",
    "Milan",
    "Naples",
    "Turin",
    "Palermo",
    "Genoa",
    "Bologna",
    "Florence",
    "Bari",
    "Catania",
    "Venice",
    "Verona",
    "Messina",
    "Padua",
    "Trieste",
    "Taranto",
    "Brescia",
    "Prato",
    "Parma",
    "Modena",
]

# coordinates (lat, lon) for the CITIES list in the notebook
COORDS = {
    "Rome": (41.9028, 12.4964),
    "Milan": (45.4642, 9.1900),
    "Naples": (40.8518, 14.2681),
    "Turin": (45.0703, 7.6869),
    "Palermo": (38.1157, 13.3615),
    "Genoa": (44.4056, 8.9463),
    "Bologna": (44.4949, 11.3426),
    "Florence": (43.7696, 11.2558),
    "Bari": (41.1256, 16.8669),
    "Catania": (37.5079, 15.0830),
    "Venice": (45.4408, 12.3155),
    "Verona": (45.4384, 10.9916),
    "Messina": (38.1938, 15.5540),
    "Padua": (45.4064, 11.8768),
    "Trieste": (45.6495, 13.7768),
    "Taranto": (40.4710, 17.2386),
    "Brescia": (45.5416, 10.2118),
    "Prato": (43.8777, 11.1022),
    "Parma": (44.8015, 10.3279),
    "Modena": (44.6471, 10.9252),
}

GEOJSON_ITALY_URL = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries/ITA.geo.json"

def plot_solution_matplotlib(solution_genotype, problem, cities=CITIES, coords=COORDS):
    n = len(solution_genotype)

    plt.figure(figsize=(8,10))

    # try to draw Italy borders under the route using the GeoJSON
    try:
        gj = requests.get(GEOJSON_ITALY_URL, timeout=5).json()
        # geojson could be either FeatureCollection or a single Feature
        geom = None
        if gj.get('type') == 'FeatureCollection':
            # take first feature (repo provides single country)
            geom = gj['features'][0]['geometry']
        elif gj.get('type') == 'Feature':
            geom = gj['geometry']
        else:
            geom = gj.get('geometry', gj)

        polygons = []
        if geom['type'] == 'Polygon':
            polygons = [geom['coordinates']]
        elif geom['type'] == 'MultiPolygon':
            polygons = geom['coordinates']

        for poly in polygons:
            for ring in poly:
                lons = [pt[0] for pt in ring]
                lats = [pt[1] for pt in ring]
                plt.plot(lons, lats, color='0.2', linewidth=1)
    except Exception:
        # if fetching/plotting borders fails, continue without it
        pass

    # route points
    latlons = [coords[cities[i]] for i in solution_genotype] + [coords[cities[solution_genotype[0]]]]
    lats = [p[0] for p in latlons]
    lons = [p[1] for p in latlons]
    plt.plot(lons, lats, '-o', color='tab:blue', zorder=3)

    # annotate cities with index and name
    for idx, city_idx in enumerate(solution_genotype):
        name = cities[city_idx]
        lat, lon = coords[name]
        plt.text(lon + 0.08, lat + 0.05, f"{name}", fontsize=9, ha='left', va='bottom',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1), zorder=4)

    # annotate segments with weights at midpoints
    for i in range(n):
        a_idx = solution_genotype[i]
        b_idx = solution_genotype[(i + 1) % n]
        a = coords[cities[a_idx]]
        b = coords[cities[b_idx]]
        mid_lon = (a[1] + b[1]) / 2
        mid_lat = (a[0] + b[0]) / 2
        w = problem[a_idx, b_idx]
        plt.text(mid_lon, mid_lat, f"{w:.2f}", fontsize=8, color='tab:blue',
                 ha='center', va='center',
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1), zorder=4)

    plt.title("TSP solution (lon, lat) — Italy borders shown if available")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def plot_solution_on_map(solution_genotype, problem, cities=CITIES, coords=COORDS):
    plot_solution_matplotlib(solution_genotype, problem, cities, coords)