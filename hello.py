import dronekit_sitl, time
from dronekit import connect, VehicleMode

# methods
def armtakeoff(altitude):
    # will takeoff with current altitude
    print ('trying to arm...')
    # trying to connect with
    while vehicle.is_armable is False:
        print ('retrying')
        time.sleep(1)
    if vehicle.is_armable is True:
        vehicle.mode = VehicleMode('GUIDED')
        vehicle.armed = True
        print('vehicle armed')

# initialization
sitl = dronekit_sitl.start_default()

# connecting via udp port
print ("connecting to vehicle...")
vehicle = connect('127.0.0.1:14551', wait_ready=True)
# vehicle = connect('/dev/ttyACM0', wait_ready=True)
# vehicle = connect('/dev/ttyUSB0', wait_ready=True)
# -------------------------------------------------------------------------------------------------

#  vehicle states
print ('is armable: %s' % vehicle.is_armable)
print ('GPS : %s' % vehicle.gps_0)
print('mode :  %s' % vehicle.mode.name)
print ('home : %s'%vehicle.home_location)

# in action
armtakeoff(5)

# closing
vehicle.close()