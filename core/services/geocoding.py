import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT = "DBD-Restaurantes/1.0"


def geocode_address(address):
    if not address:
        return None

    params = {
        "q": address,
        "format": "json",
        "limit": 1,
    }
    headers = {
        "User-Agent": USER_AGENT,
    }

    try:
        response = requests.get(
            NOMINATIM_URL,
            params=params,
            headers=headers,
            timeout=4,
        )
        response.raise_for_status()
        payload = response.json()
    except (requests.RequestException, ValueError):
        return None

    if not payload:
        return None

    try:
        latitude = float(payload[0]["lat"])
        longitude = float(payload[0]["lon"])
    except (KeyError, TypeError, ValueError):
        return None

    if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        return None

    return latitude, longitude
