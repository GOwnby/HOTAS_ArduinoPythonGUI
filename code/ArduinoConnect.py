import serial.tools.list_ports

knownDevices = []
# Define a function to determine which COM port the Arduino is connected to
def findArduinos():
    # Get a list of ports
    ports = serial.tools.list_ports.comports()
    commPort = 'None'
    # Find the number of ports
    numConnection = len(ports)
    deviceData = []
    thisDeviceData = []
    # For each port check if there is an Arduino Connected
    for i in range(0, numConnection):
        port = ports[i]
        strPort = str(port)
        # Check if there is an Arduino Connected
        if 'Arduino' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
            # Create a Serial instance using the COM port found above
            serialInst = serial.Serial(commPort, baudrate=9600, timeout = 1)
            # Create a device data array to hold the Serial Instance and UUID
            thisDeviceData = []
            thisDeviceData.append(serialInst)
            idVal = '0'

            # Wait for the Arduino to post its UUID
            while (len(idVal) < 2):
                idVal = serialInst.readline().decode('ascii').strip()

                # Write the connection back to the Arduino
                if idVal not in knownDevices:
                    serialInst.write(b'a')
                    knownDevices.append(idVal)
                    thisDeviceData.append(idVal)
                    print('Connected to Device UUID: ' + idVal)
                else:
                    serialInst.write(b'a')
                    thisDeviceData.append(idVal)
                    print('Connected to Device UUID: ' + idVal)
    # Append the device data for this connection
    deviceData.append(thisDeviceData)
    # Return the device data for all Arduino connections
    return deviceData

# A Function for closing an Arduino connection given a Serial Instance
def closeConnection(serialInst):
    serialInst.close()