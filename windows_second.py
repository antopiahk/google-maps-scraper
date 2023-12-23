from src.gmaps import Gmaps
from src.category import Category
from city_queries import city_queries as city_queries_list


first_quarter = len(city_queries_list)//4
second_quarter = round(len(city_queries_list)//(4/2))
third_quarter = round(len(city_queries_list)//(4/3))
fourth_quarter = len(city_queries_list)

city_queries = city_queries_list[57:84] # 84

city_queries = [item for sublist in city_queries for item in sublist]

# city_queries.reverse()

Gmaps.places(city_queries)