class Map:
    def __init__(self):  # constructor
        self.width = 5
        self.height = 7
        self.chaien = SKObject(2, 3, " C ")
        self.box = SKObject(1, 4, " B ")
        self.storage = SKObject(1, 1, " S ")
        self.objects = [self.chaien, self.box, self.storage]


    def print_objects(self, x, y):
        for object in self.objects:
            if object.print(x, y):
                return True

        return False

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.print_objects(x, y):
                    pass
                else:
                    print(" - ", end="")
            print()

    def process_input(self):
        move = input("Your move?").upper()
        dx = 0
        dy = 0
        if move == "D":
            dx = 1
        # To do: move, up, down, left
        [next_x, next_y] = self.chaien.caculate_next(dx, dy)

# class Keysetting:
#     def __init__(self, up, down, left, right):
#         self.up

class SKObject:
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.character = character

    def print(self, x, y):
        if self.x == x and self.y == y:
            print(self.character, end="")
            return True
        else:
            return False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

sokoban = Map()
sokoban.print()

