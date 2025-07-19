# each worker thread will run one function at a time
import threading
import time
from dataclasses import dataclass

@dataclass
class TieDefenderTravel:
    origin: str
    destination: str
    time: int
    
    def __post_init__(self): # starts the first ship
        self.time = int(self.time)
        if self.time < 0:
            raise ValueError("Time cannot be negative")
        if not isinstance(self.origin, str) or not isinstance(self.destination, str):
            raise TypeError("Origin and destination must be strings")
        print("coming into the hyperspace 🌌")
        time.sleep(self.time)
        print(f"Arrived at {self.destination} from {self.origin} in {self.time}")
    
    def tie_defender_fleete_travel(self):
        ships = []
        for ship in range(3): # 3 Tie Defenders
            hole = threading.Thread(target=TieDefenderTravel, args=(self.origin, self.destination, self.time))
            ships.append(hole)
            hole.start()
        for ship in ships:
            ship.join()
        return f"All ships have arrived at {self.destination} from {self.origin} in {self.time} seconds"
    
if __name__ == "__main__":
    try:
        travel = TieDefenderTravel("Tatooine", "Coruscant", 3)
        print(travel.tie_defender_fleete_travel())
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")