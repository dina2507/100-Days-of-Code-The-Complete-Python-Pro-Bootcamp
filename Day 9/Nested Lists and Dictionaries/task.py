travel_log = {
    "Frace" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# Pause 1
print(travel_log["Frace"][1])

# Pause 2
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# PAUSE 3
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])
