def loop(self):
	beh = behaviours.getBehaviour(self.current_state)
	position1, running1, changed1 = vs1.sequence(beh[0], beh[1]) # Here we input the sequence from sequence.py and our most important output is position1. This is the number we should currently be at when following our sequence
	position2, running2, changed2 = vs2.sequence(beh[2], beh[3]) # Same as above but for our second sequence
	position3, running3, changed3 = vs3.sequence(beh[4], beh[5])
	self.checkState(running1 or running2 or running3)
	
	led.update_full_color(self.getColor(beh[6], position1))
	servo.update(position2)
	motor.update(position3)
