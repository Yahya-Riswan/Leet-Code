class Robot:
    def __init__(self, id, pos, health, dir):
        self.id = id
        self.pos = pos
        self.health = health
        self.dir = dir

class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        robots = []
        
        # 1. Create Robot objects and keep track of original index (id)
        for i in range(n):
            robots.append(Robot(i, positions[i], healths[i], directions[i]))
            
        # 2. Sort robots by their physical position
        robots.sort(key=lambda x: x.pos)
        
        stack = [] # This will store robots moving Right ('R')
        survivors = []
        
        for robot in robots:
            if robot.dir == 'R':
                stack.append(robot)
            else:
                # Robot is moving Left, resolve collisions with stack
                while stack and robot.health > 0:
                    top_robot = stack[-1]
                    
                    if robot.health > top_robot.health:
                        # Left robot wins, decreases health, stack robot dies
                        stack.pop()
                        robot.health -= 1
                    elif robot.health < top_robot.health:
                        # Right robot wins, decreases health, left robot dies
                        top_robot.health -= 1
                        robot.health = 0
                    else:
                        # Both die
                        stack.pop()
                        robot.health = 0
                
                # If the Left robot survived all collisions in the stack
                if robot.health > 0:
                    survivors.append(robot)
        
        # 3. Combine survivors from stack (Rights) and survivors list (Lefts)
        all_survivors = survivors + stack
        
        # 4. Sort by original ID to return in the required order
        all_survivors.sort(key=lambda x: x.id)
        
        return [r.health for r in all_survivors]