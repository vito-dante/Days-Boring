# // money available
villetes200 = 1
villetes100= 3
villetes50= 0
villetes20= 20
villetes10= 20

def verification200():
	global villetes200
	if villetes200>0:
		villetes200-=1
		return True
	else:
		return False


def verification100():
	global villetes100
	if villetes100>0:
		villetes100-=1
		return True
	else:
		return False

def verification50():
	global villetes50
	if villetes50>0:
		villetes50-=1
		return True
	else:
		return False

def verification20():
	global villetes20
	if villetes20>0:
		villetes20-=1
		return True
	else:
		return False

def verification10():
	global villetes10
	if villetes10>0:
		villetes10-=1
		return True
	else:
		return False



def delevery(amount):
	vill200= 0
	vill100= 0
	vill50= 0
	vill20= 0
	vill10= 0

	while amount > 0:
		if(verification200() and amount>=200):
				amount -=200
				vill200+=1
		else:
			if(verification100() and amount>=100 ):
					amount -=100
					vill100+=1

			else:
				if(verification50() and amount>=50):
						amount -=50
						vill50+=1
				else:
					if(verification20() and amount>=20):
							amount -=20
							vill20+=1
					else:
						if(verification10() and amount>=10):
								amount -=10
								vill10+=1
	print(""" 
		200 : %s
		100 : %s
		50 : %s
		20 : %s
		10 : %s
			"""%(vill200,vill100,vill50,vill20,vill10))		


delevery(670)
