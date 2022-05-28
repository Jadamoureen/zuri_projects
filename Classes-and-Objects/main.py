class Student:

    #The init method or constructor
    def __init__(self,name,age,tracks,score):
        #Instance Variable
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        #pass

    def change_name(self,newname):
        self.name = newname
        print("My name is", self.name)

    def change_age(self,newage):
        self.age = newage
        print("my age is",self.age)

    def add_track(self,tracks):
        self.tracks.append(tracks)
        print("Tracks offered",self.tracks)

    def get_score(self):
        print("The scores got",self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

