from src.gmaps import Gmaps
from src.category import Category
from city_queries import city_queries as city_queries_list

star_it = '''Help us reach 850 stars, and we'll break the GMaps 120 limit, giving you 150+ to 250+ potential customers per search.
             Star us to make it happen ⭐! https://github.com/omkarcloud/google-maps-scraper/'''
 
queries = city_queries_list

first_quarter = len(city_queries_list)//4
second_quarter = round(len(city_queries_list)//(4/2))
third_quarter = round(len(city_queries_list)//(4/3))
fourth_quarter = len(city_queries_list)

city_queries = city_queries_list[175:180] #175:]

city_queries = [item for sublist in city_queries for item in sublist]

# city_queries.reverse()

Gmaps.places(city_queries)