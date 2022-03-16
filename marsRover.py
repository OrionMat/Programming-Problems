import re

# List of all robot orientations (North, East, South, West)
allOrientations = ["N", "E", "S", "W"]

# Function to parse user input into a grid size.
# parameter gridSizeString is the raw user input (type string).
# returns tuple of integers (e.g 1, 2).
def parseGridSize(gridSizeString):
    gridSizeList = gridSizeString.split()
    if len(gridSizeList) != 2:
        raise ValueError("Grid size error. Enter two numbers for the grid size.")

    xLength = int(gridSizeList[0])
    yLength = int(gridSizeList[1])

    # TODO: add checks for 0 0 input and negative grids sizes

    return (xLength, yLength)

# Function to parse user instruction into variables.
# parameter rawInstructionString is the raw user input of form (x, y, DIRECTION) COMMANDS.").
# returns tuple of initial states and command string (x, y, orientation, commands).
def parseRobotInstruction(rawInstructionString):

    # Regex pattern match to pull out initial state and commands into variables.
    parsedInstruction = re.match(r'\((\d+), (\d+), ([NESW])\) (\b[FLR]+\b)', rawInstructionString)

    if parsedInstruction.lastindex != 4:
        raise ValueError("Instruction parsing error. Enter instructions in the form (x, y, DIRECTION) COMMANDS.")

    x = int(parsedInstruction.group(1))
    y = int(parsedInstruction.group(2))
    orientation = parsedInstruction.group(3)
    commands = parsedInstruction.group(4)

    return (x, y, orientation, commands)

# Function to rotate the robot.
# parameter initialDirection is the robots initial direction.
# parameter rotateDirection is the command to rotate the robot Right (R) or Left (L).
# returns the direction the robot is facing (N, S, E or W).
def rotate(initialDirection, rotateDirection):
    initialDirectionIndex = allOrientations.index(initialDirection)
    if (rotateDirection == "R"):
        # If rotating right go to the next index in the list ["N", "E", "S", "W"]. Modulo the length + 1 to cycle through.
        nextDirectionIndex = (initialDirectionIndex + 1) % (len(allOrientations) + 1)
        return allOrientations[nextDirectionIndex]
    elif (rotateDirection == "L"):
        # If rotating left go to the previous index in the list ["N", "E", "S", "W"]. -1 index is end of list.
        return allOrientations[initialDirectionIndex - 1]
    else:
        raise ValueError("Rotate error. Rotation should be 'R' or 'L'.")
        
# Function to move the robot forward one space.
# parameter xStart is the starting x coordinate.
# parameter yStart is the starting y coordinate.
# parameter direction is the direction the robot is facing.
# returns the direction the robot is facing (N, S, E or W).
def moveForward(xStart, yStart, direction):
    (xEnd, yEnd) = xStart, yStart
    if (direction == "N"):
        yEnd = yStart + 1
    elif (direction == "S"):
        yEnd = yStart - 1
    elif (direction == "E"):
        xEnd = xStart + 1
    elif (direction == "W"):
        xEnd = xStart - 1
    else:
        raise ValueError("Move error. Direction should be 'N', 'E', 'S', 'W'.")
    return (xEnd, yEnd)

# Function to execute instruction for a robot.
# parameter xGrid is the length of the grid.
# parameter yGrid is the height of the grid.
# parameter xInitial is the starting x coordinate of the robot.
# parameter yInitial is the starting y coordinate of the robot.
# parameter initialOrientation is the initial orientation of the robot.
# parameter commandString is the string of commands for the robot.
# returns the final position and orientation of the robot.
def executeInstruction(xGrid, yGrid, xInitial, yInitial, initialOrientation, commandString):

    # Initialise variables.
    orientation = initialOrientation
    (xPrev, yPrev) = (xInitial, yInitial)
    (x, y) = (xInitial, yInitial)

    for command in commandString:
        if (x < 0 or x > xGrid or y < 0 or y > yGrid):
            # robot is outside the grid and becomes lost.
            return (xPrev, yPrev, orientation, "LOST")
        elif (command == "F"):
            # move one space in direction robot is facing.
            (xPrev, yPrev) = (x, y)
            (x, y) = moveForward(xPrev, yPrev, orientation)
        else:
            # rotate orientation
            orientation = rotate(orientation, command)
    
    return (x, y, orientation, "")



# Read grid size
rawGridSize = input("Enter grid size: ")
(xGrid, yGrid) = parseGridSize(rawGridSize)

finalStatesList = []
isAnotherInstruction = "y"
while(isAnotherInstruction == "y"):
    try:
        # Read initial state and movement commands
        rawCommand = input("Enter initial state and commands for a robot: ")
        (xState, yState, initialOrientation, commandString) = parseRobotInstruction(rawCommand)

        # Execute instructions
        finalState = executeInstruction(xGrid, yGrid, xState, yState, initialOrientation, commandString)
        finalStatesList.append(finalState)

        isAnotherInstruction = input("Enter command for another robot? (y/n): ")
    except Exception as error:
        print(error)

# Print output
for (xFinal, yFinal, orientationFinal, lostOrNot) in finalStatesList:
    print(f"({xFinal}, {yFinal}, {orientationFinal}) {lostOrNot}")