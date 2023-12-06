from math import sin, radians, cos, sqrt, atan2


def haversine_distance(id, lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    print(f"lat: {lat1}, {lat2}, lng: {lon1}, {lon2}")
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    print(f"ID: {id},  Distance: {distance}")
    return distance
