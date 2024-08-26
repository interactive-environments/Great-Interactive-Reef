class Behaviours:
    state_day_nobody = 0
    state_day_somebody = 1
    state_night_nobody = 2
    state_night_somebody = 3
    state_beautiful = 4
    def getBehaviour(self, state):
#         state = self.state_beautiful # Change this to the state you want to test
# Currently the above line is commented out and if you want to use it then you'll have to remove the "#" in front.
# Removing that will disable the actual state the creature is in and set it to a specific state so that you can test that specific state.
        if state == self.state_day_nobody: # If the state is day_nobody then do the following code
            sequence1 = [(0, 0.1, 1, "QuadEaseIn")] # Our sequence here is simply "go to 0 in 0.1 seconds using 1 step" Which translates to just being 0 all the time
            loops1 = 0 # Its for the vibration motor which is either on or off so we chose to keep it off
            sequence2 = [(80, 0.2, 1, "QuadEaseIn"), # Here we have an actual sequence, it goes to 80 in 0.2 seconds and then goes to 100 in 0.2 seconds
                   (100, 0.2, 1, "QuadEaseOut")] # Both are done in one single step so it will be instant. This will make the servo go up and down rather quickly
            loops2 = 0 # We set this to 0 as we want it to continue forever and to never stop.
            return (sequence1, loops1, sequence2, loops2) # Here we return these values which we can then use back in creature.py as our vspeed inputs.



        if state == self.state_day_somebody:
            sequence1 = [(65000, 0.1, 1, "QuadEaseIn")] # This is still the vibration motor, it is on an analog pin which has a range between 0 and 65535 (2^16-1), 65000 is enough to turn it on.
            loops1 = 0
            sequence2 = [(70, 0.1, 1, "QuadEaseIn"), # Same as in the state above except for that its faster and it goes further
                   (110, 0.1, 1, "QuadEaseOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_night_nobody:
            sequence1 = [(0, 0.1, 1, "QuadEaseIn")]
            loops1 = 0
            sequence2 = [(80, 0.4, 10, "QuadEaseIn"), # Here we actually use 10 steps which means you'll get more of a swaying motion rather than instant. It is also a bit slower.
                   (100, 0.4, 10, "QuadEaseOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_night_somebody:
            sequence1 = [(0, 0.1, 1, "QuadEaseIn")]
            loops1 = 0
            sequence2 = [(70, 0.2, 10, "QuadEaseIn"),
                   (110, 0.2, 10, "QuadEaseOut")]
            loops2 = 0
            return (sequence1, loops1, sequence2, loops2)



        if state == self.state_beautiful:
            sequence1 = [(65000, 0.1, 1, "QuadEaseIn"), (0, 5.9, 1, "QuadEaseIn")]
            loops1 = 1
            sequence2 = [(0, 1, 10, "QuadEaseIn"),
                   (180, 1, 10, "QuadEaseOut")]
            loops2 = 3
            return (sequence1, loops1, sequence2, loops2)
