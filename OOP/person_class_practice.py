class Person:
    def __init__(self,fname: str, lname: str ):
        self.__fname = fname
        self.__lname = lname

    @property
    def fname(self):
        return self.__full_name

    @property
    def lname(self):
        return self.__lname

    @property
    def full_name(self):
        return f'{self.__fname} {self.__lname}'


ben = Person("Ben", "Stapleton")

print (ben.full_name)
