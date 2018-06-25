# Render this specimen with DrawBot3: http://www.drawbot.com/
import math

# Basic variables
WIDTH, HEIGHT = 1024, 512
MARGIN = 64 # Margin around the page
PADDING = 40
FRAMES = 20

# size(WIDTH, HEIGHT)

# Font setup
font("fonts/Orbitron-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data)) # Get axis info from font

def grid():
    fill(None)
    stroke(1)
    strokeWidth(1)
  
    # Grid X-axis
    stepx  = -32  # step in sequence on x axis             
    incx   =  32  # grid increment
    for x in range(29):
        save()
        stepx = stepx + incx
        polygon((MARGIN + stepx, MARGIN), (MARGIN+stepx, WIDTH-MARGIN))
        restore()

    # Grid Y-axis
    stepy  = -32  # step in sequence on y axis 
    incy   =  32  # grid increment
    for y in range(13):
        save()
        stepy = stepy + incy
        polygon((MARGIN, MARGIN + stepy), (WIDTH-MARGIN, MARGIN+stepy))
        restore()


var = 300
for frame in range(12):
    newPage(WIDTH, HEIGHT)
    # Layout
    fill(0) # Background color
    rect(0, 0, WIDTH, HEIGHT) # Draw the background
    
    # Draw the grid
    grid()
    
    stroke(None)
    fill(0) # Background color
    rect(0, 0, WIDTH-257, HEIGHT) # Draw the background
    rect(0, (256+128)+1, WIDTH, HEIGHT) # Draw the background
    
    font("fonts/Orbitron-VF.ttf")
    fontSize(76)

    # Set text fill
    fill(1)
    strokeWidth(2)
    stroke(None)
    tracking(None)
    for i in range(1,7):
        # Magic
        print(300+(i*100))
        fontVariations(wght=400+(i*100))
        # Draw text
        text("ORBITRON", MARGIN, (448 -(i*64)))
  
    # Draw red box + grid
    # x, y = ((WIDTH/2)+MARGIN), MARGIN 
    # w, h = ((WIDTH/2)-(MARGIN*2)), (HEIGHT-(MARGIN*2))
    # fill(1, 0, 0)
    # rect(x, y, w, h)

    
    fill(1)
    # fontSize(64)
    stroke(None)
    
    if frame <= 6:
        var = var + 100
    if frame >6 : 
        var = var - 100
           
    fontVariations(wght=var)   
    text("ABCDEF", 574, (448-(1*64)))
    text("GHIJKL", 574, (448-(2*64)))
    text("MNOP", 574, (448-(3*64)))
    text("QRST", 574, (448-(4*64)))
    text("UVW", 574, (448-(5*64)))
    text("XYZ", 574, (448-(6*64)))
        
saveImage('animated-specimen-basic.gif')

