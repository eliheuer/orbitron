# Layout
size(1024, 512)

# gird variables
origin = (32, 32)
height = 448
width = 960
center = width/2
num_x_units = 64
num_y_units = 8
gut = 8 
col = 112
col_num = 8

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(0.5)
    stroke(0.9)  
    fill(None)

    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
        
    step_col = 0 
    stroke(0, 0, 1)
#    for column in range(8): 
#        rect(step_col, 0, col, height)
#        step_col += (col + gut)

# newpage
fill(0.9) # color of background
rect(0, 0, 1024, 512) # draw the background

fill(0)
stroke(None)
# rect(0, 0, 288, 216)

# translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# Debug 
x, y, w, h = 0, 0, ((col * 8)+(gut *7)), 173

# Fonts
font("fonts/Orbitron-VF.ttf")
fontSize(134)

# stroke(None)
fill(0)
stroke(None)
# tracking(0)

for i in range(1,5):
    text("ORBITRON", (-8, -114+(i*114)))

fontSize(60)
fill(1)
stroke(0)
strokeWidth(2)

for j in range(1,5):
    text("variable", (620, -114+(j*114)))

fontSize(50)
letters = ["t", "n", "o", "f"]
fill(0)
stroke(None)

for k in range(1,5):
    text(letters[k-1], (930, -114+(k*114)))

saveImage('example.gif')

