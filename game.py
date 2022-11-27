from src.rover import Rover

game_map = input("Enter map size:")

start_location = input("Enter start location: ")

start_direction = input("Enter start direction: ")

game_map = list(map(int, game_map.split(",")))
start_location = list(map(int, start_location.split(",")))

rover = Rover(game_map=game_map, start_location=start_location, start_direction=start_direction)

while not rover.crashed:
    [list(rover.valid_directions.values()).index(rover.direction)]
    print(f"Current location: {rover.location}, Current Heading: {rover.cardinal_direction}")
    rover.move(input("Better get a move on: "))
