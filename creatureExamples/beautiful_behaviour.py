def loop(self):
	beh = behaviours.getBehaviour(self.current_state)
	position1, running1, changed1 = vs1.sequence(beh[0], beh[1]) # Here we input the sequence from sequence.py and our most important output is position1. This is the number we should currently be at when following our sequence
	position2, running2, changed2 = vs2.sequence(beh[2], beh[3]) # Same as above but for our second sequence
	self.checkState(running1 or running2)
		
	#vvv DAY NO INTERACTION vvv
	led.update_full_color((math.floor((10/255)*position1), math.floor(position1), math.floor((50/255)*position1)))
		
	#rainbow code, it's not pretty
	if self.beautiful:
		k=i/255
		if self.i < 255: 
			j = self.i%255
			k=j/255
			led.update_full_color((math.floor((position1)*(1-k)), math.floor((position1)*k), 0))
			print("2")
		elif self.i < 255*2:
			j = self.i%255
			k=j/255
			led.update_full_color((0,math.floor((position1)*(1-k)), math.floor((position1)*k)))
			print("3") 
		elif self.i < 255*3:
			j = self.i%255
			k=j/255
			led.update_full_color((math.floor((position1)*k), 0,math.floor((position1)*(1-k))))
			print("4")
		elif self.i < 255*4:
			self.i=0
		
		self.i+=5
	
	servo.update(position2) # Here we set the servo to position 2