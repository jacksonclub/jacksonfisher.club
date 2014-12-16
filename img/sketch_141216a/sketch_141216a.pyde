def setup():
    size(350, 381)
    global img
    img = loadImage("jackson.jpeg")

def draw():
    c = radians(random(360))
    tint(random(255), random(255), random(255), random(255)) 
    #translate(width/2, height/2)
    rotate(c)
    image(img, 0, 0)
    saveFrame("frames/#####.png")
