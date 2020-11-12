class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
    def get_gender(self):
        return print(self._gender)
    def set_gender(self, gender):
        self._gender = gender
        print("Success Modifity gender value now it is %s." % self._gender)

a = Student("tom", "A")
a.get_gender()
a.set_gender("B")