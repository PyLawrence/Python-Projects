class Student:
    _schoolName = 'The Tech Academy'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def _display(self):
        print("My name is {}, and I am {} years old.".format(self.__name, self.__age))

    @property
    def school(self):
        return self._schoolName

    @school.setter
    def school(self, schoolName):
        # although schoolName is protected, we made 'school' a property
        # this will allow us to use this setter to do something else first if needbe, such as contacting a database
        print("changing...")
        self._schoolName = schoolName


testVar = Student("John", 25)

print(testVar._Student__name)

print(testVar.school)
testVar.school = "not the original school"
print(testVar.school)
