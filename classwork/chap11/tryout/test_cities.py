# from city_functions import city_country

# def test_city_country():
#     """Test that city_country() returns correctly formatted strings."""
#     result = city_country('santiago', 'chile')
#     assert result == "Santiago, Chile"

from city_functions import city_country

def test_city_country():
    """Test city & country only."""
    result = city_country('santiago', 'chile')
    assert result == "Santiago, Chile"

def test_city_country_population():
    """Test city, country, and population."""
    result = city_country('santiago', 'chile', 5000000)
    assert result == "Santiago, Chile – population 5000000"
