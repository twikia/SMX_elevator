import math
import argparse

TIME_PER_FLOOR = 10


def main(floors: list[int]):

    total_time = 0
    
    prev_floor = floors[0]
    for floor in floors[1:]:
        total_time += TIME_PER_FLOOR * abs(floor - prev_floor)
        prev_floor = floor

    print("Floors visited in order:", floors)
    print("Total time:", total_time)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('floors', type=int, nargs='+',
                       help='A list of numbers')
    
    
    args = parser.parse_args()
    
    # num_floors = args.floors
    # num_elevators = args.elevators
    print("Floors to visit:", args.floors)
    main(args.floors)


    