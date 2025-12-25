import googlemaps
from config import API_KEY

gmaps = googlemaps.Client(key=API_KEY)


def tracer_trajet(depart, arrivee, arrets):
    directions = gmaps.directions(
        origin=depart,
        destination=arrivee,
        waypoints=arrets,
        mode="driving"
    )

    etapes = []

    for leg in directions[0]["legs"]:
        etapes.append((
            leg["start_address"],
            leg["end_address"]
        ))

    return etapes
