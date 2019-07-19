def setup():
    size(450,700)
    background(255, 255,255)
    x = 3
    y = 10
    #strokeWeight(50)
    im = loadImage("we clowns.png")
    noStroke()
    
    while x < 490:
        y = 0
        print(x)
        image(im, x, y,  40, 40)
        while y < 700: 
            image(im, x, y,  40, 40)
            y += 35
        x +=41
    fill(48, 128, 255)
    rect(80, 350, 300, 60)
    fill(255,255,255)
    textSize(50)
    text("We Clowns.", 95, 400)

        
        
