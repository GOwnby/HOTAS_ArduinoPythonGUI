import sys # Package used to exit the application properly
import os # Package used to navigate folders correctly
import tkinter as tk # Package used for creating GUI window
from PIL import ImageTk, Image # Package used to add Image to GUI
import matplotlib.backends.backend_tkagg # Package used to add Plot Graph to GUI
import matplotlib.figure # Package used to add Plot Graph to GUI
import ArduinoConnect # Package used for connecting to the Arduino

# Find All Arduinos Connected
SerialConnections = ArduinoConnect.findArduinos()

parentWindowManager = tk.Tk()

# For each connection, create a Window
for connection in SerialConnections:
    # Create tkinter window  for GUI
    window = tk.Toplevel(parentWindowManager)
    window.transient(parentWindowManager)
    # Name the window and set the geometry of the window to fill the screen
    window.title(connection[1])
    # Set the window to be full screen
    window.geometry("1920x1080")
    # Load the OU Logo
    img = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.dirname(os.path.realpath(__file__) ) ) + os.sep + "media" + os.sep + "OUlogo.png") )
    panel = tk.Label(window, image=img)
    panel.pack(side="top", fill="none", expand="no") # Add the Logo to the top of the GUI
    # Create a frame at the bottom of the window
    bottomFrame = tk.Frame(window, width=1920, height=300)
    bottomFrame.pack(side="bottom", anchor='n')
    # Create a frame to fill space at the bottom of the window
    frameFigLabelSpace = tk.Frame(bottomFrame, width = 1920, height=250)
    frameFigLabelSpace.pack(side="bottom", anchor='s')
    # Create a frame to hold the updates value of the X and Y coords on plot 1
    frameFig1Label= tk.Frame(bottomFrame, height=5, width=100)
    frameFig1Label.pack(side="left", anchor='n')
    # Create a frame to hold the updates value of the X and Y coords on plot 2
    frameFig2Label = tk.Frame(bottomFrame, height=5, width=100)
    frameFig2Label.pack(side="right", anchor='n')
    # Create a label for Joystick 1's updated values
    plot1Label = tk.Label(frameFig1Label, text="Joystick 1", width=50, anchor='nw', padx=60, font=('TkDefaultFont', 14))
    plot1Label.pack(side='top')
    # Create a label for Joystick 2's updated values
    plot2Label = tk.Label(frameFig2Label, text="Joystick 2", width=50, anchor='ne', padx=60, font=('TkDefaultFont', 14))
    plot2Label.pack(side='top')
    # The Width and Height used in by figsize to create a Joystick Figure plot in the shape of a square
    joystickFigureWidthHeight = 5
    # The Joystick Figure plot size is determined by the area we want to use on the screen by the stretch factor used in by dpi
    # dpi (density (or dots) per inch) is a relative positioning factor whose total value is the same for every screen juxtaposed to ppi (pixels per inch) 
    joystickFigureStretchFactor = 100
    # Create a Figure to hold the First Joystick Position Plot
    joystickFigure1 = matplotlib.figure.Figure(figsize=(joystickFigureWidthHeight,joystickFigureWidthHeight), dpi=joystickFigureStretchFactor)
    # Add the Figure to a Canvas Frame within the Window
    canvasPlot1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(joystickFigure1, window)
    canvasPlot1.get_tk_widget().pack(side="left")
    # Add a Frame Filler for padding between the canvas plot and Digital Input Buttons
    frameFillA = tk.Frame(width="75")
    frameFillA.pack(side="left")
    # Add a Frame to hold the First 16 Digital Input Buttons
    frameA = tk.Frame()
    frameA.pack(side="left")
    frameFillAled = tk.Frame(width="10")
    frameFillAled.pack(side="left")
    frameAled = tk.Frame()
    frameAled.pack(side="left")
    # Add a Frame Filler for padding between the First 16 Digital Input and Last 16 Digital Input Buttons
    frameFillA1 = tk.Frame(width="75")
    frameFillA1.pack(side="left")
    # Add a Frame to hold the Last 16 Digital Input Buttons
    frameA1 = tk.Frame()
    frameA1.pack(side="left")
    frameFillA1led = tk.Frame(width="10")
    frameFillA1led.pack(side="left")
    frameA1led = tk.Frame()
    frameA1led.pack(side="left")
    frameFillA1led = tk.Frame(width="75")
    frameFillA1led.pack(side="left")
    #fillFrameC = tk.Frame(height="35")
    #fillFrameC.pack()
    frameC = tk.Frame(width=100)
    frameC.pack(side="left")
    # Add each Slider Scale to the GUI with a Label stating which Potentiometer it is
    labelS1 = tk.Label(frameC, text="Potentiometer 1")
    labelS1.pack()
    sliderS1 = tk.Scale(frameC, from_=0, to=5)
    sliderS1.pack()
    labelS2 = tk.Label(frameC, text="Potentiometer 2")
    labelS2.pack()
    sliderS2 = tk.Scale(frameC, from_=0, to=5)
    sliderS2.pack()
    labelS3 = tk.Label(frameC, text="Potentiometer 3")
    labelS3.pack()
    sliderS3 = tk.Scale(frameC, from_=0, to=5)
    sliderS3.pack()
    labelS4 = tk.Label(frameC, text="Potentiometer 4")
    labelS4.pack()
    sliderS4 = tk.Scale(frameC, from_=0, to=5)
    sliderS4.pack()

    # Add a Frame Filler for padding between the canvas plot and Digital Output Buttons
    frameFillB = tk.Frame(width="100")
    frameFillB.pack(side="left")
    # Add a Frame to hold the Digital Output Buttons
    frameB = tk.Frame()
    frameB.pack(side="left")
    # Create a Figure to hold the Second Joystick Position Plot
    joystickFigure2 = matplotlib.figure.Figure(figsize=(joystickFigureWidthHeight,joystickFigureWidthHeight), dpi=joystickFigureStretchFactor)
    # Add the Figure to a Canvas Frame within the Window
    canvasPlot2 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(joystickFigure2, window)
    canvasPlot2.get_tk_widget().pack(side="right")

    # Functions to send characters to the Arduino specifying which Digital Output should be turned on
    def turnOnLED1():
        connection[0].write(b"1")
    def turnOnLED2():
        connection[0].write(b"2")
    def turnOnLED3():
        connection[0].write(b"3")
    def turnOnLED4():
        connection[0].write(b"4")
    def turnOnLED5():
        connection[0].write(b"5")
    def turnOnLED6():
        connection[0].write(b"6")
    def turnOnLED7():
        connection[0].write(b"7")
    def turnOnLED8():
        connection[0].write(b"8")
    def turnOnLED9():
        connection[0].write(b"9")
    def turnOnLED10():
        connection[0].write(b"q")
    def turnOnLED11():
        connection[0].write(b"w")
    def turnOnLED12():
        connection[0].write(b"e")
    def turnOnLED13():
        connection[0].write(b"r")
    def turnOnLED14():
        connection[0].write(b"t")
    def turnOnLED15():
        connection[0].write(b"y")
    def turnOnLED16():
        connection[0].write(b"u")
    # Define a function to read the next line in the Serial buffer and return it
    def getNextLine():
        next = connection[0].readline().decode('ascii').strip() # Reads the line ending in a carriage return, decodes it into the ASCII format it was sent in, and strips the null characters
        return next
    def turnOnButton(label):
        label.config(text="ON!", bg='red') # Turns label "ON!", changing the background color to red
    def turnOffButton(label):
        label.config(text="OFF", bg="SystemButtonFace") # Turns the label off, changes banckground to default
    def updateLabelVal(label, newText):
        label.config(text=newText)
    # Define a function to request a packet of data each loop of the program
    def requestData():
        dataList = [] # empy list to hold contents of each line passed
        nextLine = getNextLine() # Read in the next line from the buffer
        while (nextLine != '<'):  # While the nextLine is not the Start Delimiter, continue on and get the next line
            nextLine = getNextLine()
        # Loop above terminates when nextLine is the Start deliminer, so read the first data point into nextLine
        nextLine = getNextLine()
        # Loop to iterate through all of the valid data being sent, concluding when the End Delimiter is read into nextLine
        while (nextLine != '>'):
            dataList.append(nextLine)
            nextLine = getNextLine()

        connection[0].flush() # Flush out the buffer to maintain only full packets from Arduino are being read in 

        return dataList # Return the data points to be displayed in the GUI
        
    # Add all the Digital Input buttons to Frame A
    buttonB1I = tk.Label(frameA, text="Digital Input 1", pady=7)
    buttonB1I.pack()
    buttonB2I = tk.Label(frameA, text="Digital Input 2", pady=7)
    buttonB2I.pack()
    buttonB3I = tk.Label(frameA, text="Digital Input 3", pady=7)
    buttonB3I.pack()
    buttonB4I = tk.Label(frameA, text="Digital Input 4", pady=7)
    buttonB4I.pack()
    buttonB5I = tk.Label(frameA, text="Digital Input 5", pady=7)
    buttonB5I.pack()
    buttonB6I = tk.Label(frameA, text="Digital Input 6", pady=7)
    buttonB6I.pack()
    buttonB7I = tk.Label(frameA, text="Digital Input 7", pady=7)
    buttonB7I.pack()
    buttonB8I = tk.Label(frameA, text="Digital Input 8", pady=7)
    buttonB8I.pack()
    buttonB9I = tk.Label(frameA, text="Digital Input 9", pady=7)
    buttonB9I.pack()
    buttonB10I = tk.Label(frameA, text="Digital Input 10", pady=7)
    buttonB10I.pack()
    buttonB11I = tk.Label(frameA, text="Digital Input 11", pady=7)
    buttonB11I.pack()
    buttonB12I = tk.Label(frameA, text="Digital Input 12", pady=7)
    buttonB12I.pack()
    buttonB13I = tk.Label(frameA, text="Digital Input 13", pady=7)
    buttonB13I.pack()
    buttonB14I = tk.Label(frameA, text="Digital Input 14", pady=7)
    buttonB14I.pack()
    buttonB15I = tk.Label(frameA, text="Digital Input 15", pady=7)
    buttonB15I.pack()
    buttonB16I = tk.Label(frameA, text="Digital Input 16", pady=7)
    buttonB16I.pack()
    # Add all the Digital Input buttons to Frame A1 to the right of the other Digital Input Buttons
    buttonB17I = tk.Label(frameA1, text="Digital Input 17", pady=7)
    buttonB17I.pack()
    buttonB18I = tk.Label(frameA1, text="Digital Input 18", pady=7)
    buttonB18I.pack()
    buttonB19I = tk.Label(frameA1, text="Digital Input 19", pady=7)
    buttonB19I.pack()
    buttonB20I = tk.Label(frameA1, text="Digital Input 20", pady=7)
    buttonB20I.pack()
    buttonB21I = tk.Label(frameA1, text="Digital Input 21", pady=7)
    buttonB21I.pack()
    buttonB22I = tk.Label(frameA1, text="Digital Input 22", pady=7)
    buttonB22I.pack()
    buttonB23I = tk.Label(frameA1, text="Digital Input 23", pady=7)
    buttonB23I.pack()
    buttonB24I = tk.Label(frameA1, text="Digital Input 24", pady=7)
    buttonB24I.pack()
    buttonB25I = tk.Label(frameA1, text="Digital Input 25", pady=7)
    buttonB25I.pack()
    buttonB26I = tk.Label(frameA1, text="Digital Input 26", pady=7)
    buttonB26I.pack()
    buttonB27I = tk.Label(frameA1, text="Digital Input 27", pady=7)
    buttonB27I.pack()
    buttonB28I = tk.Label(frameA1, text="Digital Input 28", pady=7)
    buttonB28I.pack()
    buttonB29I = tk.Label(frameA1, text="Digital Input 29", pady=7)
    buttonB29I.pack()
    buttonB30I = tk.Label(frameA1, text="Digital Input 30", pady=7)
    buttonB30I.pack()
    buttonB31I = tk.Label(frameA1, text="Digital Input 31", pady=7)
    buttonB31I.pack()
    buttonB32I = tk.Label(frameA1, text="Digital Input 32", pady=7)
    buttonB32I.pack()

    virtLEDList = []
    # Add all the Digital Input button labels to Frame A LED
    buttonB1IvLed= tk.Label(frameAled, text = "OFF", pady=7)
    buttonB1IvLed.pack()
    buttonB2IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB2IvLed.pack()
    buttonB3IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB3IvLed.pack()
    buttonB4IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB4IvLed.pack()
    buttonB5IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB5IvLed.pack()
    buttonB6IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB6IvLed.pack()
    buttonB7IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB7IvLed.pack()
    buttonB8IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB8IvLed.pack()
    buttonB9IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB9IvLed.pack()
    buttonB10IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB10IvLed.pack()
    buttonB11IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB11IvLed.pack()
    buttonB12IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB12IvLed.pack()
    buttonB13IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB13IvLed.pack()
    buttonB14IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB14IvLed.pack()
    buttonB15IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB15IvLed.pack()
    buttonB16IvLed= tk.Label(frameAled, text="OFF", pady=7)
    buttonB16IvLed.pack()
    # Add all the Digital Input buttons labels to Frame A1 LED to the right of the other Digital Input Buttons and Labels
    buttonB17IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB17IvLed.pack()
    buttonB18IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB18IvLed.pack()
    buttonB19IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB19IvLed.pack()
    buttonB20IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB20IvLed.pack()
    buttonB21IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB21IvLed.pack()
    buttonB22IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB22IvLed.pack()
    buttonB23IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB23IvLed.pack()
    buttonB24IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB24IvLed.pack()
    buttonB25IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB25IvLed.pack()
    buttonB26IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB26IvLed.pack()
    buttonB27IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB27IvLed.pack()
    buttonB28IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB28IvLed.pack()
    buttonB29IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB29IvLed.pack()
    buttonB30IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB30IvLed.pack()
    buttonB31IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB31IvLed.pack()
    buttonB32IvLed= tk.Label(frameA1led, text="OFF", pady=7)
    buttonB32IvLed.pack()

    # Add all vLEDs to a list to easily turn them on and off based on data from Arduino
    virtLEDList.append(buttonB1IvLed)
    virtLEDList.append(buttonB2IvLed)
    virtLEDList.append(buttonB3IvLed)
    virtLEDList.append(buttonB4IvLed)
    virtLEDList.append(buttonB5IvLed)
    virtLEDList.append(buttonB6IvLed)
    virtLEDList.append(buttonB7IvLed)
    virtLEDList.append(buttonB8IvLed)
    virtLEDList.append(buttonB9IvLed)
    virtLEDList.append(buttonB10IvLed)
    virtLEDList.append(buttonB11IvLed)
    virtLEDList.append(buttonB12IvLed)
    virtLEDList.append(buttonB13IvLed)
    virtLEDList.append(buttonB14IvLed)
    virtLEDList.append(buttonB15IvLed)
    virtLEDList.append(buttonB16IvLed)
    virtLEDList.append(buttonB17IvLed)
    virtLEDList.append(buttonB18IvLed)
    virtLEDList.append(buttonB19IvLed)
    virtLEDList.append(buttonB20IvLed)
    virtLEDList.append(buttonB21IvLed)
    virtLEDList.append(buttonB22IvLed)
    virtLEDList.append(buttonB23IvLed)
    virtLEDList.append(buttonB24IvLed)
    virtLEDList.append(buttonB25IvLed)
    virtLEDList.append(buttonB26IvLed)
    virtLEDList.append(buttonB27IvLed)
    virtLEDList.append(buttonB28IvLed)
    virtLEDList.append(buttonB29IvLed)
    virtLEDList.append(buttonB30IvLed)
    virtLEDList.append(buttonB31IvLed)
    virtLEDList.append(buttonB32IvLed)


    buttonList = []
    # Add all the Digital Output buttons to Frame B and attach the command corresponding to each Digital Output
    buttonB1O = tk.Button(frameB, text="Digital Output 1", command=turnOnLED1)
    buttonB1O.pack()
    buttonB2O = tk.Button(frameB, text="Digital Output 2", command=turnOnLED2)
    buttonB2O.pack()
    buttonB3O = tk.Button(frameB, text="Digital Output 3", command=turnOnLED3)
    buttonB3O.pack()
    buttonB4O = tk.Button(frameB, text="Digital Output 4", command=turnOnLED4)
    buttonB4O.pack()
    buttonB5O = tk.Button(frameB, text="Digital Output 5", command=turnOnLED5)
    buttonB5O.pack()
    buttonB6O = tk.Button(frameB, text="Digital Output 6", command=turnOnLED6)
    buttonB6O.pack()
    buttonB7O = tk.Button(frameB, text="Digital Output 7", command=turnOnLED7)
    buttonB7O.pack()
    buttonB8O = tk.Button(frameB, text="Digital Output 8", command=turnOnLED8)
    buttonB8O.pack()
    buttonB9O = tk.Button(frameB, text="Digital Output 9", command=turnOnLED9)
    buttonB9O.pack()
    buttonB10O = tk.Button(frameB, text="Digital Output 10", command=turnOnLED10)
    buttonB10O.pack()
    buttonB11O = tk.Button(frameB, text="Digital Output 11", command=turnOnLED11)
    buttonB11O.pack()
    buttonB12O = tk.Button(frameB, text="Digital Output 12", command=turnOnLED12)
    buttonB12O.pack()
    buttonB13O = tk.Button(frameB, text="Digital Output 13", command=turnOnLED13)
    buttonB13O.pack()
    buttonB14O = tk.Button(frameB, text="Digital Output 14", command=turnOnLED14)
    buttonB14O.pack()
    buttonB15O = tk.Button(frameB, text="Digital Output 15", command=turnOnLED15)
    buttonB15O.pack()
    buttonB16O = tk.Button(frameB, text="Digital Output 16", command=turnOnLED16)
    buttonB16O.pack()
    
    # Create a list of buttons to iterate through
    buttonList.append(buttonB1O)
    buttonList.append(buttonB2O)
    buttonList.append(buttonB3O)
    buttonList.append(buttonB4O)
    buttonList.append(buttonB5O)
    buttonList.append(buttonB6O)
    buttonList.append(buttonB7O)
    buttonList.append(buttonB8O)
    buttonList.append(buttonB9O)
    buttonList.append(buttonB10O)
    buttonList.append(buttonB11O)
    buttonList.append(buttonB12O)
    buttonList.append(buttonB13O)
    buttonList.append(buttonB14O)
    buttonList.append(buttonB15O)
    buttonList.append(buttonB16O)

    # A function that asks the user if they would like to quit the program when they try to close the program
    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            connection[0].write(b"x") # Send disconnection signal
            window.destroy() # Destroy window
    # Attach the closing function to the window
    window.protocol("WM_DELETE_WINDOW", on_closing)

    #window.update()
    #window.update_idletasks()

    # Start the Main Loop that refreshes the values of Inputs and Outputs on the GUI
    startChar = ""
    continueLoop = True
    while continueLoop == True:
        try:
            # Read in data in the order that it was printed
            # Pass an error if the serial connection cannot be found because the application was closed
            for i in range(0,32):
                turnOffButton(virtLEDList[i])
            inputData = []
            inputData = requestData()
            if (inputData != [] and len(inputData) == 40):
                # Read in the serial data corresponding to both Joysticks
                serialDataX1 = float(inputData[0]) # Joystick 1 X-axis
                serialDataY1 = float(inputData[1]) # Joystick 1 Y-axis
                serialDataX2 = float(inputData[2])  # Joystick 2 X-axis
                serialDataY2 = float(inputData[3])  # Joystick 2 Y-axis
                # Read in the serial data corresponding to each Potentiometer
                serialDataPot1 = float(inputData[4])  # Potentiometer 1
                serialDataPot2 = float(inputData[5])  # Potentiometer 2
                serialDataPot3 = float(inputData[6])  # Potentiometer 3
                serialDataPot4 = float(inputData[7])  # Potentiometer 4
                # Read in the serial data corresponding to each Digital Input Button
                for i in range(8,40):
                    # If the button value is high, turn it on - i.e. update the label
                    if int(inputData[i]) == 1:
                        turnOnButton(virtLEDList[i-8])
                for j in range(0,16):
                    if(buttonList[j]["relief"]== "sunken"):
                        buttonList[j].invoke()
                # Decode the range from 0V to 5V to a -1.0 to +1.0 axis range for Joystick 1
                # Values greater than 2.5 are positive, values less than 2.5 are negative
                if serialDataX1 >= 2.5:
                    positionX1 = (serialDataX1 - 2.5) * 0.4 # Adjust to a range of 0 to 1
                elif serialDataX1 < 2.5:
                    positionX1 = (2.5 - serialDataX1) * -0.4 # Adjust to a range of 0 to 1
                if serialDataY1 >= 2.5:
                    positionY1 = (serialDataY1 - 2.5) * -0.4 # Adjust to a range of 0 to 1
                elif serialDataY1 < 2.5:
                    positionY1 = (2.5 - serialDataY1) * 0.4 # Adjust to a range of 0 to 1
                # Decode the range from 0V to 5V to a -1.0 to +1.0 axis range for Joystick 2
                # Values greater than 2.5 are positive, values less than 2.5 are negative
                if serialDataX2 >= 2.5:
                    positionX2 = (serialDataX2 - 2.5) * 0.4 # Adjust to a range of 0 to 1
                elif serialDataX2 < 2.5:
                    positionX2 = (2.5 - serialDataX2) * -0.4 # Adjust to a range of 0 to 1
                if serialDataY2 >= 2.5:
                    positionY2 = (serialDataY2 - 2.5) * -0.4 # Adjust to a range of 0 to 1
                elif serialDataY2 < 2.5:
                    positionY2 = (2.5 - serialDataY2) * 0.4 # Adjust to a range of 0 to 1
                # Update the Labels with the current values for x&y position
                updateLabelVal(plot1Label, "Joystick 1:\n X Position: %.2f\n Y Position: %.2f" % (positionX1, positionY1))
                updateLabelVal(plot2Label, "Joystick 2:\n X Position: %.2f\n Y Position: %.2f" % (positionX2, positionY2))
                # Print the plot to the Tkinter GUI by adding a plot to the Figure within the Canvas within the Window
                joystickPlot1 = joystickFigure1.add_subplot(111) # Add a subplot to the first x y z position 1, 1, 1 in the subplot grid
                joystickPlot1.scatter(float(positionX1), float(positionY1)) # Flip the orientation of the y-axis for this joystick
                # Set the Axis range
                joystickPlot1.set_xlim(-1, 1)
                joystickPlot1.set_ylim(-1, 1)
                # Draw updated values to the plot
                canvasPlot1.draw()
                # Run all waiting GUI events for the Canvas Frame holding the Joystick Figure within the Window before moving forward in the loop
                canvasPlot1.flush_events()
                # Print the plot to the Tkinter GUI by adding a plot to the Figure within the Canvas within the Window
                joystickPlot2 = joystickFigure2.add_subplot(111) # Add a subplot to the first x y z position 1, 1, 1 in the subplot grid
                joystickPlot2.scatter(float(positionX2), float(positionY2)) # Flip the orientation of the y-axis for this joystick
                # Set the Axis range
                joystickPlot2.set_xlim(-1, 1)
                joystickPlot2.set_ylim(-1, 1)
                # Draw updated values to the plot
                canvasPlot2.draw()
                # Run all waiting GUI events for the Canvas Frame holding the Joystick Figure within the Window before moving forward in the loop
                canvasPlot2.flush_events()
                
                # Set the value of the Sliders after the Potentiometer data has been read and update their labels with this value
                sliderS1.set(int(serialDataPot1))
                updateLabelVal(labelS1, "Potentiometer 1: %.2f V" % serialDataPot1)
                sliderS2.set(int(serialDataPot2))
                updateLabelVal(labelS2, "Potentiometer 2: %.2f V" % serialDataPot2)
                sliderS3.set(int(serialDataPot3))
                updateLabelVal(labelS3, "Potentiometer 3: %.2f V" % serialDataPot3)
                sliderS4.set(int(serialDataPot4))
                updateLabelVal(labelS4, "Potentiometer 4: %.2f V" % serialDataPot4)
                
                window.update()
                # Clear the plots from the Tkinter GUI to prepare to write new Frames
                joystickFigure1.clear()
                joystickFigure2.clear()
        except Exception: # If the plots on the Frame cannot be found/destroyed it is because the application was closed mid-loop (they are gone already)
            connection[0].write(b"x") # Send disconnection signal
            connection[0].write(b"x") # Send disconnection signal
            connection[0].write(b"x") # Send disconnection signal
            ArduinoConnect.closeConnection(connection[0]) # Make sure the connection is closed
            sys.exit(0) # Exit the Application