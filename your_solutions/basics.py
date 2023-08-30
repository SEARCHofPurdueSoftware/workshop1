# TO-DO: 

G_CONST = 6.67e-11 # N * m^2 / kg^2

M_SUN = 2e30 # kg
M_EARTH = 6e24 # kg
M_SATURN_V_ROCKET = 3e6 # kg

R_EARTH = 6400 # km

D_SUN_EARTH = 150e6 # km

#*-------------------------*#
#*-----TO BE CALCULATED----*#
#*-------------------------*#
F_SUN_EARTH = None # Newtons
F_ROCKET_EARTH = None # Newtons
EARTH_ESC_VEL = None # meters per second
#*-------------------------*#
#*-------------------------*#
#*-------------------------*#




#*-------------------------*#
#*----DO YOUR WORK HERE----*#
#*-------------------------*#

# we need to calculate the force between the Sun and the Earth
# in Newtons and store that in F_SUN_EARTH

# ...and then the force between the Earth and our rocket, and
# store that in F_ROCKET_EARTH

# and lastly, we need to calculate the escape velocity from 
# earth given that we're on the surface. Can we use some physics 
# to figure out how to do this?
#
# A hint:
# - We know that gravitational potential energy is -G * m1 * m1 / r
# -
# - And we know that kinetic energy is (1 / 2) * m * v^2...
# -
# - Escape velocity is defined as the velocity necessary to escape
# - the gravitational pull of an object fully, which means that all
# - the kinetic energy it has at the surface has to equal the
# - additive inverse (the negative) of the potential energy it has
# - at the surface.
# - This way, as the rocket gets further away from the Earth, the
# - potential energy of the system goes up (but down in magnitude,
# - remember that negative sign) and the kinetic energy goes down.


#*-------------------------*#
#*-------------------------*#
#*-------------------------*#


print(f"The gravitational force between the Earth and the Sun is < {F_SUN_EARTH:.2E} > Newtons.")
print(f"The gravitational force between the Earth and the Saturn V Rocket is < {F_ROCKET_EARTH:.2E} > Newtons.")
print(f"The escape velocity on Earth is < {EARTH_ESC_VEL:.2E} > m/s.")



