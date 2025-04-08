import argparse

TIME_PER_FLOOR = 10


def find_direction(floors: list[int], first: int):
    """ loops through all the elements until it finds one different than the first and then returns 1 for up -1 for down"""
    for floor in floors:
        if floor > first:
            return 1
        if floor < first:
            return -1
        
    return 1


def main(floors: list[int]):
    """
    Calculates the optimal path and total time for an elevator to visit all requested floors.
    The elevator follows these rules:
    - Starts at the first floor in the input list
    - Moves in the initial direction determined by the next different floor number
    - Visits all floors in that direction before reversing to visit remaining floors
    - Takes TIME_PER_FLOOR time units to move between consecutive floors
    
    Args:
        floors (list[int]): List of floor numbers to visit
        
    Returns:
        tuple: (total_time, visited_floors)
            - total_time (int): Total time taken to visit all floors
            - visited_floors (list[int]): List of floors in order visited
    """
    
    if len(floors) <= 0: return 0, []


    first_floor = floors[0]
    direction = find_direction(floors, first_floor)

    floors = sorted(list(set(floors)))  # Remove duplicates first
    
    # Split floors into above and below first floor
    floors_above = [f for f in floors if f > first_floor]
    floors_below = [f for f in floors if f < first_floor]


    if len(floors_above) + len(floors_below) <= 1:
        return 0, [first_floor]
    
    if len(floors_above) <= 0:
        return abs(first_floor - floors_below[0]) * TIME_PER_FLOOR, [first_floor] + floors_below[::-1]
    
    if len(floors_below) <= 0:
        return abs(first_floor - floors_above[-1]) * TIME_PER_FLOOR, [first_floor] + floors_above
    
    if direction == 1:
        return (abs(first_floor - floors_above[-1]) + abs(floors_above[-1] - floors_below[0])) * TIME_PER_FLOOR, [first_floor] + floors_above + floors_below[::-1]

    return (abs(first_floor - floors_below[0]) + abs(floors_above[-1] - floors_below[0])) * TIME_PER_FLOOR, [first_floor] + floors_below[::-1] + floors_above
    

    
    ####################################################################
    # code to visit every floor in sequential order and return the time - not used
    ####################################################################

    # total_time = 0
    # prev_floor = floors[0]
    # for floor in floors[1:]:
    #     total_time += TIME_PER_FLOOR * abs(floor - prev_floor)
    #     prev_floor = floor

    # print("Floors visited in order:", floors)
    # print("Total time:", total_time)





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('floors', type=int, nargs='+', help='A list of numbers seperated by spaces')
    
    args = parser.parse_args()

    print("Floors to visit:", args.floors)
    print("result:", main(args.floors))


    