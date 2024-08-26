def loop(self):
	beh = behaviours.getBehaviour(self.current_state)
	position2, running2, changed2 = vs2.sequence(beh[4], beh[5]) # Same as above but for our second sequence
	self.checkState(running2) #or runningfreq)
	print(self.current_state)
	###############################################################
	# This is about where you'll have to start coding yourself    #
	# If you want to test out the code here then do the following #
	# Put a button in A2, a servo motor in D4 and a vibration     #
	# motor in D2                                                 #
	###############################################################
	
	pos2 = int(position2*(self.energy/100))
	lightlevel = int(255*(self.energy/100))
	led.update((lightlevel,lightlevel,lightlevel)) # Here we set the motor to position 1
	servo.update(pos2) # Here we set the servo to position 2
