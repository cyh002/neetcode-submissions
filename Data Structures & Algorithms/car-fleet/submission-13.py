class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Need to zip position and speed together
        # 2. Do the Reordering 
        # 3. 

        car_list = sorted(zip(position, speed), reverse = True)
        #print(f"car_list {car_list}")
        fleets = 0
        stack = []
        for pos, spd in car_list:
            car_time = (target - pos) / spd
            if stack: 
                # do the comparison
                if car_time <= stack[-1]:
                    continue
            stack.append(car_time)
            fleets += 1
        return fleets

