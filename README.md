# SMX_elevator
This code emulates a real life elevator. The code takes in a list of floors to visit and outputs what order the floors will be visited and the total travel time (10 time units per floor change). 

To use the exe use "./elevator!.exe 1 2 3 2 6" this will run with the array [1, 2, 3, 2, 6].

To use the script use "python elevator.py 1 4 2 5" this will run with the array [1, 4, 2, 5]. 

Use any array that you want, even negative numbers!

# behavior
Elevators travel in the current direction until the furthest floor in that direction is reached.

The elevator will move in the direction of the floor that is after the first floor in the array because that is the button that was requested first. Eg. [5, 5, 4] will move downward.

The type of call button for this elevator is single because it doesn't take into account which direction you want to go, only the direction it was already going to fuffil requests.

# Assumptions:

The input list is in order of buttons pressed. The first index is where the elevator is, the second is the oldest request, third is second oldest etc.

The script should be as close as possible to a real life elevator.

The input with the exe or script will be in the exact format I need above otherwise it will output an errora

# testing
tests can be run by just running the tester.py, the tests are an array of tuples with the input then the expected time and array output.
