class Agent:
    def __init__(self, N, X, charging_location, gold_location):
        self.N = N
        self.X = X
        self.charging_location = charging_location
        self.gold_location = gold_location
        self.current_location = (0, 0)
        self.visited_rooms = set()
        self.steps_taken = 0
    def move(self, direction):
        x, y = self.current_location
        if direction == "forward":
            if x < self.N - 1:
                x += 1
            else:
                x -= 1  
        elif direction == "backward":
            if x > 0:
                x -= 1
            else:
                x += 1  
        elif direction == "right":
            if y < self.N - 1:
                y += 1
            else:
                y -= 1  
        elif direction == "left":
            if y > 0:
                y -= 1
            else:
                y += 1  
        self.current_location = (x, y)
        self.steps_taken += 1
    def explore(self):
        while self.steps_taken < self.X:
            if self.current_location == self.gold_location:
                print(f"Gold found in room {self.current_location}. Total time taken: {self.steps_taken}")
                break
            if self.current_location not in self.visited_rooms:
                self.visited_rooms.add(self.current_location)
                self.move("forward")
            else:
                self.move("right")
                if self.current_location == self.charging_location:
                    print(f"Charging needed in room {self.current_location}. Total time taken: {self.steps_taken}")
                    break
N = 5
X = 22
charging_location = (2, 2)
gold_location = (4, 3)
agent = Agent(N, X, charging_location, gold_location)
agent.explore()
