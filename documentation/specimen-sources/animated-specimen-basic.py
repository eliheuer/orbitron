# Render this specimen with DrawBot3: http://www.drawbot.com/

# Basic variables
WIDTH, HEIGHT = 1024, 512
MARGIN = 64 # Margin around the page
PADDING = 40
FRAMES = 20

# Layout
size(WIDTH, HEIGHT)
fill(0) # Background color
rect(0, 0, WIDTH, HEIGHT) # Draw the background

def grid():
    fill(None)
    # stroke(0.75)
    stroke(0.4)
    strokeWidth(1)
  
    # Grid X-axis
    stepx  = -32  # step in sequence on x axis             
    incx   =  32  # grid increment
    for x in range(29):
        save()
        stepx = stepx + incx
        polygon((MARGIN + stepx, MARGIN), (MARGIN+stepx, CANVAS_WIDTH-MARGIN))
        restore()

    # Grid Y-axis
    stepy  = -32  # step in sequence on y axis 
    incy   =  32  # grid increment
    for y in range(13):
        save()
        stepy = stepy + incy
        polygon((MARGIN, MARGIN + stepy), (CANVAS_HEIGHT-MARGIN, MARGIN+stepy))
        restore()

def main():
    
    # Font setup
    font("fonts/Orbitron-VF.ttf")
    fontSize(76)
    for axis, data in listFontVariations().items():
        print((axis, data)) # Get axis info from font

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
        text("ORBITRON", MARGIN, (450 -(i*64)))
      
    # a box has an x, y, width and height
    x, y, w, h = ((WIDTH/2)+MARGIN), MARGIN, ((WIDTH/2)-(MARGIN*2)), (HEIGHT-(MARGIN*2))
    # set a fill
    fill(1, 0, 0)
    # draw a rectangle with variables from above
    rect(x, y, w, h)
        
    fill(1)
    fontSize(54)
    fontVariations(wght=900)    
    text("ABCDEF", 580, (456-(1*64)))
    text("GHIJKL", 580, (456-(2*64)))
    text("MNOPQR", 580, (456-(3*64)))
    text("STUVWX", 580, (456-(4*64)))
    text("YZ", 580, (456-(5*64)))
    # Draw the grid
    grid()
    saveImage('animated-specimen-basic.gif')
    
if __name__ == "__main__":  
    main()
    
