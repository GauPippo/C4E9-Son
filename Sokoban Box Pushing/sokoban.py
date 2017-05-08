size = {
    "width" : 5,
    "height" : 4
    }

c = {
    "x" : 2,
    "y" : 1
    }

b = {
    "x" : 1,
    "y" : 2
    }

s = {
    "x" : 2,
    "y" : 3
    }

def display_map(size, c, b, s):
    for y in range(size["height"]):
        for x in range(size["width"]):
            if x == c["x"] and y == c["y"]:
                print(" C ", end="")
            elif x == b["x"] and y == b["y"]:
                print(" B ", end="")
            elif x == s["x"] and y == s["y"]:
                print(" S ", end="")
            else:
                print(" - ", end="")
        print()

def maps (x, y):
    if (x > size["width"] - 1 or x < 0 or y > size["height"] - 1 or y < 0)or (x == s["x"] and y == s["y"]):
        c["x"] = cx
        c["y"] = cy
        b["x"] = bx
        b["y"] = by
    return x, y

loop = True

while(loop):
    # graphics
    display_map(size,c,b,s)

    # logic (game play)
    move = input("Your move?(W,A,S,D)").upper()
    if move == "D":
        c["x"] += 1        
    elif move == "A":
        c["x"] -= 1
    elif move == "S":
        c["y"] += 1
    elif move == "W":
        c["y"] -= 1
    else:
        print("Nhap sai roi`, xin moi nhap lai")

    # Maximum of C in maps   
    c["x"] = maps(c["x"], c["y"])[0]
    c["y"] = maps(c["x"], c["y"])[1]

    # C push Box in maps
    if c["x"] == b["x"] and c["y"] == b["y"]:
        b["x"] += b["x"] - cx
        b["y"] += b["y"] - cy
    # Maximum of Box in maps
    b["x"] = maps(b["x"], b["y"])[0]
    b["y"] = maps(b["x"], b["y"])[1]

    # Define position C B
    cx = c["x"]
    cy = c["y"]
    bx = b["x"]
    by = b["y"]

display_map (size, c, b, s)
