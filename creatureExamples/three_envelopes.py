# Example 1
def loop(self):
	beh = behaviours.getBehaviour(self.current_state)
	position1, running1, changed1 = vs1.sequence(beh[0], beh[1]) # Here we input the sequence from sequence.py and our most important output is position1. This is the number we should currently be at when following our sequence
	position2, running2, changed2 = vs2.sequence(beh[2], beh[3]) # Same as above but for our second sequence
	position3, running3, changed3 = vs3.sequence(beh[4], beh[5]) # Same as above but for our second sequence
	self.checkState(running1 or running2 or running3)
	###############################################################
	# This is about where you'll have to start coding yourself    #
	# If you want to test out the code here then do the following #
	# Put a button in A2, a servo motor in D4 and a vibration     #
	# motor in D2                                                 #
	###############################################################

	led.update_full_color((position1, int(position1/27), 0)) # Here we set the motor to position 1
	buzzer.update(position2) # Here we set the servo to position 2
	buzzer.set_frequency(position3)

# Example 2
def loop(self):
	print("state:", self.current_state)
	beh = behaviours.getBehaviour(self.current_state)

	hue, running1, changed1 = vs_h.sequence(beh[0], beh[1])
	light, running2, changed2 = vs_l.sequence(beh[2], beh[3])
	sat, running3, changed3 = vs_s.sequence(beh[4], beh[5])

	mag, running4, _changed4 = vs_mag.sequence(beh[6], beh[7])

	self.checkState(running1 or running2 or running3 or running4)

	c = convert_color(hue, light, sat)
	leds.update_full_color(c)
	print("hls:", hue, light, sat)
	print("rgb:", c)

	magnet.update(mag)

	#time.sleep(1)

def convert_color(hue, light, sat):
	(r, g, b) = colorsys.hls_to_rgb(hue / 360.0, light, sat)
	return (int(r), int(g), int(b))