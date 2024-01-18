
##### The purpose of this program is to allow users to produce pictures of their own ascii graphics #####




#This comment is meaningless#

# Function to print a box
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol needs to be 1 character"')
    print(symbol * width)
    if userinput[0] == 'b':
        for i in range(height-2):
            print(symbol * width)
    elif userinput[0] == 's':
        for i in range(height - 2):
            print(symbol + (' '  * (width - 2)) + symbol)
    print(symbol * width)


# Function to print a line
def linePrint(symbol, length):
    if len(symbol) != 1:
        raise Exception('"symbol needs to be 1 character"')
    if linedimension == 'v':
        for i in range(length):
            print(symbol)
    elif linedimension == 'h':
        print(symbol * length)
    elif linedimension == 'r':
        for i in range(length):
            space = length - i
            print((space * ' ') + (symbol) + (i * ' '))
    elif linedimension == 'l':
        for i in range(length):
            space = length - i
            print((i * ' ') + (symbol) + (space * ' '))
    else:
        print("Invalid second argument. Type '!info' for commands")
            
        
# Function to print a diamond
def diamondPrint(symbol, diameter):
    if len(symbol) != 1:
        raise Exception('"symbol needs to be 1 character"')
    radius = int(round(diameter/2))
    for i in range(radius):
        space = radius - i
        print((space * ' ') + (symbol) + (2 * i * ' ') + (symbol) + (space * ' '))
    for i in range(radius + 1):
        space = radius - i
        print((i * ' ') + (symbol) + (2 * space * ' ') + (symbol))

    


# Function to print an equilateral triangle
def trianglePrint(symbol, base):
    if len(symbol) != 1:
        raise Exception('"symbol needs to be 1 character"')
    half = int(round(base/2))
    if tritype == 'u':
        print((symbol)*(base+1))
        for i in range(half):
            space = half - i
            print((i * ' ') + (symbol) + (2 * space * ' ') + (symbol))
    else:
        for i in range(half):
            space = half - i
            print((space * ' ') + (symbol) + (2 * i * ' ') + (symbol) + (space * ' '))
        print((symbol)*(base + 1))

    




# Main loop where commands are entered

while True:

    # State variables
    width = 0
    height = 0
    
    userinput = input("Enter a command. Type '!info' to see a list of commands.\n").lower()

    if userinput[:4] == 'line':
        linedimension = userinput[-1]
        try:
            symbol = input('Enter a symbol\n')
            length = int(input('Enter length of line\n'))
        except ValueError:
            print('length must be numeric value\n')
        linePrint(symbol, length)
        
    elif userinput == 'box' or userinput == 'square':
        try:
            symbol = input('Enter a symbol\n')
            while (width < 2) or (height < 2):
                width = int(input('Enter a width, 2 or more\n'))
                height = int(input('Enter a height, 2 or more\n'))
        except ValueError:
            print('width and height must be numeric values\n')
        boxPrint(symbol, width, height)


    elif userinput == 'diamond':
        diameter = 0
        try:
            symbol = input('Enter a symbol\n')
            while (diameter < 2):
                diameter = int(input("enter the diameter of the diamond (2+)\n"))                        
        except ValueError:
            print('diameter must be a numeric value\n')
        diamondPrint(symbol, diameter)
    
    elif userinput[:8] == 'triangle':
        base = 0
        try:
            tritype = userinput[-1]
            symbol = input('Enter a symbol\n')
            while (base < 3):
                base = int(input("enter the length of the base (widest part) of the triangle (3+)\n")) - 1
        except ValueError:
            print('Base must be a numeric value\n')
        trianglePrint(symbol, base)
    
    elif userinput[0] == '!':
        print("Commands list\n\
            \t'square'\t\tprint empty box\n\
            \t'box'\t\t\tprint solid box\n\
            \t'line-v'\t\tprint vertical line\n\
            \t'line-h'\t\tprint horizontal line\n\
            \t'line-r'\t\tprint diagonal right leaning line\n\
            \t'line-l'\t\tprint diagonal left leaning line\n\
            \t'diamond'\t\tprint diamond\n\
            \t'triangle'\t\tprint triangle\n\
            \t'triangle-u'\t\tprint upside down triangle\n\n")

    else:
        print('Enter a valid command')   
        












    
