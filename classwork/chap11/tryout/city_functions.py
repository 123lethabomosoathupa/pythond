# def city_country(city, country):
#     """Return a city and country, neatly formatted."""
#     return f"{city.title()}, {country.title()}"


def city_country(city, country, population=None):
    """Return a city, country, and optionally population, neatly formatted."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"

