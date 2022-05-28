class Student:
    # [assignment] Skeleton class. Add your code here
    #The init method or constructor
    def __init__(self,name,age,tracks,score):
        #Instance Variable
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        #pass
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print("Student details:")
print("His name is",Bob.name)
print("age",Bob.age)
print("tracks",Bob.tracks)
print("score",Bob.score)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

def get_score(self):
    print("Bob score is", self.score)
    return self.score