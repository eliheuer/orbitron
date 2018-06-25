# Render this specimen with DrawBot3: http://www.drawbot.com/

# Import modules:
import math

# Basic variables:
W, H, M, F = 1024, 1024, 128, 32

# Load font and print font info:
# print(installedFonts(supportsCharacters=None))
font("fonts/Orbitron-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))  # Get axis info from font


# Draw a grid from a given increment:
def grid(inc):
    stroke(0.6, 0, 0)  # Set grid line color
    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX  # Set position for next gridline
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY  # Set position for next gridline


# Page loop
varAnim = 0
varWght = 400
stepUp = 0
stepDown = 0
for frame in range(60):
    newPage(W, H)
    fill(0)           # Background color
    rect(0, 0, W, H)  # Draw the background

    # Draw the grid
    # grid(32)

    # Basic Style
    stroke(None)
    fill(1)
    
    # Calculate the weight, stepping through 360 degrees by frames
    if frame <= 35:
        pass
        if frame > 5:
            stepUp = stepUp + 20
            varWght = 400 + stepUp
    if frame > 35:
        stepDown = stepDown + 20
        varWght = 900 - stepDown

    # Set variations
    if varWght >= 900:
        varWght = 900
    if varWght <= 400:
        varWght = 400
         
    fontVariations(wght=varWght)
    print("varWght=", varWght)

    # Iterate through weight
    fill(1)
    stroke(None)
    font("fonts/Orbitron-VF.ttf")
    fontSize(94)
    text("abcdefghijklmn", (M-4, (896)-(2*96)))
    text("opqrstuvwxyz", (M-4, (896)-(3*96)))
    text("ABCDEFGHIJK", (M-4, (896)-(4*96)))
    text("LMNOPQRSTU", (M-4, (896)-(5*96)))
    text("VWXYZ(.,;:)!?[]{}", (M-4, (896)-(6*96)))
    text("123456789", (M-4, (896)-(7*96)))
    text("orbitron", (M-4, (928)-(1*96)))
    # Draw secondary text
    fill(1, 0, 0)
    fontSize(94)
    text("weight:", (W/8), (H/8))
    text(str(int(varWght)), (W-500), (H/8))
 
# Save GIF
saveImage("basic-animated-specimen.gif")
