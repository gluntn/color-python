# Program that converts hex color to letter
# Can output RGB code
# Can generate letter to hex
# example: lightblue -> 00 af ff > 0, 175, 255
## Idea for later: webpage, write in hex get colour easy
# get colour -> 'darker' (decrease every decreasable value), 'lighter' (increase what can be increased)

# CLASS
class Color(object):
	def __init__(self, r=0, b=0, g=0):
		# by default white
		self.r = r
		self.b = b
		self.g = g
		self.rgb = [r,g,b]
		self.hx = '%02x%02x%02x' % tuple(self.rgb)

	def inverse(self):
		# Return the complimentary colour
		# Oh lord, the parsing tho
		inver = int(hex(int('0xffffff', 16) - int("0x"+self.hx, 16)), 16)
		return '#%.6X' % inver

	def printFormat(self):
		return "RGB: {0} \nHex: {1}".format(self.rgb, "#"+self.hx)

	def decrease(self, num=10):
		for i in range(len(self.rgb)):
			if self.rgb[i-1] - num <= 0:
				self.rgb[i-1] == 0
			else:
				self.rgb[i-1] -= num

	def toRGB(self, hxVal=0):
		if hxVal == 0:
			hxVal = self.hx
		newRGB = []
		hx_ = [hxVal[i:i+2] for i in range(0, len(hxVal), 2)]
		for i in hx_:
			newRGB.append(int('0x'+i, 16))
		return newRGB

	def increase(self,num=10):
		# go through the variables in class, increase them (not go above 255)
		for i in range(len(self.rgb)):
			if self.rgb[i-1] + num >= 255:
				self.rgb[i-1] == 255
			else:
				self.rgb[i-1] += num


def addColor(name, r=0, b=0, g=0):
	r, g, b = int(r), int(b), int(g)
	if name in colors:
		print "Color already exists!"
	else:
		colors[name] = Color(r, g, b)
		print "Added {0}!".format(name)

# FUNCTIONS
def exit():
	running = False
	# The print module, prints formatted colours and can add unknown colours

def printColor(name):
	try:
		print "*** {0} ***\n{1}".format(name.upper(), colors[name].printFormat())
	except KeyError:
		print "There are no colours called {0}.".format(name)
		ans = raw_input("Would you like to add the colour? (y/n)")
		if ans == 'n':
			# Is this the right way to do it?
			pass
		elif ans == 'y':
			new_rgb = raw_input("Please input its RGB values: n,n,n")
			new_rgb = new_rgb.split(",")
			try:
				addColor(name, new_rgb[0], new_rgb[1], new_rgb[2])
			except TypeError:
				print "Does not follow format"

def add(command):
	try:
		new_rgb = command[2].split(",")
		addColor(command[1], new_rgb[0], new_rgb[1], new_rgb[2])
	except TypeError:
		print "Does not follow format."

def inverse(color):
	try:
		print colors[color].inverse()
	except KeyError:
		print "There are no colours called {0}.".format(color)

# DICTIONARIES
colors = {
	"red": Color(255,0,0),
	"blue": Color(0,255,0),
	"green": Color(0,0,255),
	}

commands = {
	"exit": exit,
	"print": printColor,
	"inverse": inverse,
	"add": addColor,
}

# WHILE LOOP
running = True
print "What would you like to do? \n Exit: exit \n Print: print name \n Add: add color 0 0 0 \n Inverse: inverse color"
while running:
	command = raw_input("\n >").lower().split(" ")
	main_command, command = command[0], command[1::]
	if main_command not in commands:
		print "{0} is not a command!".format(main_command)
	else:
		commands[main_command](*command)
