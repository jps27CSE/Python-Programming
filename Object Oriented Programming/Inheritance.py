class Bird:

    def __init__(self):
        print("bird is ready")

    def whoIsThis(self):
        print("bird")

    def swim(self):
        print("swim faster")

class penguin(Bird):

    def __init__(self):
        super().__init__()

        print("penguin is ready")

    def whoIsThis(self):
        print("penguin")
    
    def run(self):

        print("run faster")

peggy=penguin()

peggy.whoIsThis()

peggy.run()

peggy.swim()

