# import imp
# libardrone = imp.load_source('libardrone', 'python-ardrone/libardrone.py')
import libardrone
drone = libardrone.ARDrone()
# You might need to call drone.reset() before taking off if the drone is in# emergency mode
drone.takeoff()
drone.land()
drone.halt()
