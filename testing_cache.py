from src.gmaps import Gmaps
from src.category import Category
from city_queries import city_queries as city_queries_list

city_queries = city_queries_list[58] # 84

#city_queries = [item for sublist in city_queries for item in sublist]

# city_queries.reverse()

Gmaps.places(city_queries)