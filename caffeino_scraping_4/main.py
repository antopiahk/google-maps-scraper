import sys
from src.gmaps import Gmaps
from src.category import Category
from city_queries import city_queries as city_queries_list

# get the start and end range from the command line arguments
start = int(sys.argv[1])
end = int(sys.argv[2])

# get the correct range of city queries
city_queries = city_queries_list[start:end+1]

city_queries = [item for sublist in city_queries for item in sublist]

print(f"About to run the following range: {start} - {end}")

Gmaps.places(city_queries)