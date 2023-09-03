import matplotlib.pyplot as plt

G_CONST = 6.67e-11 # N * m^2 / kg^2
M_EARTH = 6e24 # kg
SATELLITE_MASSES = [100, 130, 90, 80, 230, 190] #kg

# The cartesian x-, y-, and z-axes follow spherical 
# coordinate conventions. That is:
# x = r * cos(theta) * cos(phi)
# y = r * sin(theta) * cos(phi)
# z = r * sin(phi)
# In this case, latitude is theta and longitude is phi.
INITIAL_PAYLOAD_VEL = [0, 8000, 0] # m/s
INITIAL_PAYLOAD_LAT = 0
INITIAL_PAYLOAD_LON = 0
INITIAL_PAYLOAD_ALT = 500 #km

R_EARTH = 6400 # km

#*-------------------------*#
#*-----TO BE CALCULATED----*#
#*-------------------------*#
TOTAL_PAYLOAD_MASS = 0
INITIAL_PAYLOAD_POS = [0, 0, 0]
TRAJECTORY = [] # every minute on the interval [0m, 120m)

# use the below variable to keep track of the payload positions
# it should be a list of lists -- and you can ignore the z-component
# of each position. that is, each sublist should be of length two
# and contain solely the x- and y- coordinates
PAYLOAD_POSITIONS = []
#*-------------------------*#
#*----DO YOUR WORK HERE----*#
#*-------------------------*#


#*-------------------------*#
#*-------------------------*#
#*-------------------------*#
# The below code will render your trajectory -- do not modify this!
#*-------------------------*#
#*-------------------------*#
#*-------------------------*#
fig, ax = plt.subplots()
for ind in range(len(PAYLOAD_POSITIONS)):
	l = PAYLOAD_POSITIONS[:ind + 1]
	earth = plt.Circle((0, 0), R_EARTH * 1000, color = 'b')
	ax.set_facecolor('black')
	ax.add_patch(earth)
	ax.plot([p[0] for p in l], [p[1] for p in l], color = 'red')
	plt.pause(0.01)
	plt.cla()
