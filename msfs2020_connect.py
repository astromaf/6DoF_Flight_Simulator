from SimConnect import *
import math
import time

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 to be refreshed every 2 seconds
aq = AircraftRequests(sm, _time=2000)

altitude = 250
angle = 0
ae = AircraftEvents(sm)
event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off

while angle>-math.pi/2:
	time.sleep(0.00001)

	#aq.set("PLANE_ALTITUDE", altitude)
	aq.set("PLANE_ALT_ABOVE_GROUND", altitude)
	aq.set("PLANE_BANK_DEGREES", 0)
	aq.set("PLANE_PITCH_DEGREES", angle)
	aq.set("PLANE_HEADING_DEGREES_TRUE", 0)

	angle -= 0.001
	altitude += 0
	event_to_trigger()
	print(angle)

angle = -angle
speed = 1
while altitude < 250000:
	time.sleep(0.00001)
	# aq.set("PLANE_ALTITUDE", altitude)
	aq.set("PLANE_ALT_ABOVE_GROUND", altitude)
	aq.set("INDICATED_ALTITUDE", altitude)
	aq.set("PLANE_BANK_DEGREES", 0)
	aq.set("PLANE_PITCH_DEGREES", 3*math.pi/2)
	aq.set("PLANE_HEADING_DEGREES_TRUE", 0)
	speed += 0.01
	altitude += speed
	event_to_trigger()

angle = -angle
while angle<0:
	time.sleep(0.00001)

	#aq.set("PLANE_ALTITUDE", altitude)
	aq.set("PLANE_ALT_ABOVE_GROUND", altitude)
	aq.set("PLANE_BANK_DEGREES", 0)
	aq.set("PLANE_PITCH_DEGREES", angle)
	aq.set("PLANE_HEADING_DEGREES_TRUE", 0)
	angle += 0.001
	altitude -= 0
	event_to_trigger()
	print(angle)

ae = AircraftEvents(sm)
# Trigger a simple event
event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off
event_to_trigger()

# Trigger an event while passing a variable
target_altitude = 15000
event_to_trigger = ae.find("AP_ALT_VAR_SET_ENGLISH")  # Sets AP autopilot hold level
event_to_trigger(target_altitude)
sm.exit()
quit()

