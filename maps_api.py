import googlemaps
from datetime import datetime
from config import API_KEY

def tracer_trajet(depart, arrivee, arrets):
    gmaps = googlemaps.Client(key=API_KEY)

    directions = gmaps.directions(
        depart,
        arrivee,
        waypoints=arrets,
        mode="driving",
        departure_time=datetime.now()
    )

    print("\n📍 TRAJET GOOGLE MAPS :\n")

    for leg in directions[0]["legs"]:
        print(f"{leg['start_address']}  →  {leg['end_address']}")
