class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = 20

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Well you see a dead person doesn't eat...because the person's dead..........(your pets dead)")

    def sleep(self):
        print("Zzzzzzz...food...zzzzzzz...nachos...zzzzzzzz...himalayan cheese dip...zzzzzzz ")

    def play(self):
        print("YAY!")
        
    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " kills " + other.name + " and " + other.name + "is left for dead!")
        other.is_alive -= 1
  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
#Zike is a panther
pet1 = Pet("Zike")
#Oscar is a red wolf with blue eyes
pet2 = Pet("Oscar")
#Ralph is a rare brown panda 
pet3 = Pet("Ralph")

