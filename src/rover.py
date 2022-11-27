import sys
class Rover:
    def __init__(self, start_location: tuple, start_direction: str, game_map: tuple):

        self.valid_directions = {"N": [1,0], "E": [0,1], "S": [-1,0], "W": [0,-1]}
        self.headings = [[1,0], [0,1], [-1,0], [0,-1]]

        
        
        if game_map[0] < 1 or game_map[1] < 1:
            sys.stderr.write("Map must be created with non zero, positive values")
            raise SystemExit
        self.game_map = game_map

        if start_location[0] not in range(0, self.game_map[0]+1) and start_location[1] not in range(0, self.game_map[1]+1):
            sys.stderr.write("Start location must be inside map area")
            raise SystemExit


        self.location = start_location
        self.direction = None
        self.game_map = game_map
        self.crashed = False
        
        try:
            self.direction = self.valid_directions[start_direction.upper()]
            self.cardinal_direction = start_direction.upper()
        except Exception:
            sys.stderr.write(f"Start direction '{start_direction}' is not valid, please use N, E, S, or W")
            raise SystemExit
        
        print("The Rover has landed! Lets Go!")

    def _rotate(self, rotate: str) -> int:
        index = list(self.valid_directions.values()).index(self.direction)
        if rotate == "R":
            if index + 1 > len(self.valid_directions)-1:
                return 0
            return index + 1
        else:
            return index -1

    def _forward(self) -> tuple:
        """
        concatenates self.location and self.direction element wise
        if the new location is in the range of the map return it,
        else return the old location
        """
        new_location = list(map( lambda i,j: i+j, self.location, self.direction))
        if new_location[0] in range(0, self.game_map[0]+1) and new_location[1] in range(0, self.game_map[1]+1):
            return new_location
        self.crashed = True
        return self.location

    def move(self, commands):
        for command in commands:
            if not self.crashed:
                if command in ["F", "f"]:
                    self.location = self._forward()

                elif command in ["L", "R", "l", "r"]:
                    index = self._rotate(command.upper())
                    self.direction = self.headings[index]
                    self.cardinal_direction = list(self.valid_directions.keys())[index]
                else:
                    sys.stderr.write("Invalid Move!")
                    raise SystemExit
        if self.crashed:
            print("The Rover has been lost!!")
            print(f"Last know location: {self.location}")
