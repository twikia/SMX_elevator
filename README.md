# SMX_elevator

Assumptions: 

The list is in order of buttons pressed. The first index is where the elevator is, the second is the oldest request, third is second oldest etc.

Elevators travel in the current direction until the furthest floor in that direction is reached.

The elevator will move in the direction of the second element in the array because that is the button that was requested first.
