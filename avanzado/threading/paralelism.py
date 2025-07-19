import multiprocessing as mp
from dataclasses import dataclass, field

@dataclass
class ResistanceFleet():
    x_wings: int
    y_wings: int
    sizeHole:list = field(default_factory=list)
    def __post_init__(self):
        if not isinstance(self.x_wings, int) or not isinstance(self.y_wings, int):
            raise TypeError("X-wings and Y-wings must be integers")
        if self.x_wings < 0 or self.y_wings < 0:
            raise ValueError("X-wings and Y-wings cannot be negative")
        print(f"{self.x_wings} X-wings and {self.y_wings} Y-wings has been starting their engines.")
    
    def x_wing_calcs(self):
        for i in range(self.x_wings): # i = cant_ships
            print(f"X-wing {i+1} is ready for takeoff.")
            x_wing_area_fleet = (i+1 * 5.5)**2 *3.1415
            self.sizeHole.append(x_wing_area_fleet)
            print(f"X-wing {i+1} area: {x_wing_area_fleet:.2f} square meters.")
            
    def y_wing_calcs(self):
        for i in range(self.y_wings): # i = cant_ships
            print(f"Y-wing {i+1} is ready for takeoff.")
            y_wing_area_fleet = (i+1 * 6.5)**2 *3.1415
            self.sizeHole.append(y_wing_area_fleet)
            print(f"X-wing {i+1} area: {y_wing_area_fleet:.2f} square meters.")
            
if __name__ == "__main__":
    try:
        fleet = ResistanceFleet(3, 5, [])
        print("Starting X-wing calculations...")
        p1 = mp.Process(target=fleet.x_wing_calcs)
        p2 = mp.Process(target=fleet.y_wing_calcs)
        
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")