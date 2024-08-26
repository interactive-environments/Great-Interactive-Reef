def loop(self):
	beh = behaviours.getBehaviour(self.current_state)
	positionR, runningR, changedR = vsR.sequence(beh[0], beh[1]) # Here we input the sequence from sequence.py and our most important output is position1. This is the number we should currently be at when following our sequence
	positionG, runningG, changedG = vsG.sequence(beh[2], beh[3])
	positionB, runningB, changedB = vsB.sequence(beh[4], beh[5])
	position1, running1, changed1 = vs1.sequence(beh[6], beh[7]) # Same as above but for our second sequence
	self.checkState(runningR or running1)
	###############################################################
	# This is about where you'll have to start coding yourself    #
	# If you want to test out the code here then do the following #
	# Put a button in A2, a servo motor in D4 and a vibration     #
	# motor in D2                                                 #
	###############################################################
	led.update_full_color((positionR,positionG,positionB))
	buzzer.update(position1)