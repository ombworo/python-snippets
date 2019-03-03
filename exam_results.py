"""Exam results.
This will store student names and marks.
"""

class Student(object):
    
    results = {}  # class variable

    def __init__(self, id, name, marks):  # constructor
        self.id = id
        self.name = name #instace variables 
        self.marks =  marks 
        Student.results[id] = [name, marks]

    def update_marks(self, id, marks):  # instance method
        if id not in Student.results:
            raise ValueError('student does not exist !')
        Student.results[id][1] = marks
        return Student.results[id]

    @classmethod  
    def get_marks(cls, id):  # class method
        if id not in Student.results:
            raise ValueError('student does not exist !')
        return cls.results[id] 
    
class Subject(Student):
    """Subject inherits from class Student"""

    def __init__(self):
        super()
        
    def update_subject(self, id, subject):  # instance method
        if id not in Subject.results:
            raise ValueError('student does not exist !')
        Subject.results[id].append(subject)
        return Subject.results[id]



omari = Student("s1", "fred omari", 90)
rules = Student("s2", "ian rules", 72)
nelson = Student("s3", "nelson ryan", 81)
# print(Student.results)

rules.update_marks("s2", 80)
# print(Student.results)

# print(Student.get_marks("s8")) 

subject1 = Subject()
print(subject1.update_subject("s3", "science"))

