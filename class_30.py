class AllPeople:
    def __init__(self) -> None:
        self.__all = []
    
    def add_person(self, person):
        self.__all.append(person)
    def get_all(self):
        return self.__all
    

class Person:
    def __init__(self, firstName, secondName, born, address) -> None:
        self.__firstname = firstName
        self.__secondname = secondName
        self.__born = born
        self.__address = address
    
    def get_info(self):
        return {
            "first name": self.__firstname,
            "second name": self.__secondname,
            "born in": self.__born,
            "address": self.__address,
        }
    
class Student(Person):
    def __init__(self, firstName, secondName, born, address, id, grade=1) -> None:
        super().__init__(firstName, secondName, born, address)
        self.__id = id
        self.__grade = grade
    
    def update_grade(self):
        self.__grade += 1
    
    def get_info(self):
        info = super().get_info()
        info.update({
            "role": "student",
            "id": self.__id,
            "grade": self.__grade
        })
        return info

class Teacher(Person):
    def __init__(self, firstName, secondName, born, address, username, degree) -> None:
        super().__init__(firstName, secondName, born, address)
        self.__username = username
        self.__degree = degree

    def get_info(self):
        info = super().get_info()
        info.update({
            "role": "teacher",
            "username": self.__username,
            "degree": self.__degree,
        })
        return info

class Address:
    def __init__(self, home, street, district, city) -> None:
        self.__home = home
        self.__street = street
        self.__district = district
        self.__city = city
    
    def update_address(self, home, street, district, city):
        self.__home = home
        self.__street = street
        self.__district = district
        self.__city = city

    def get_address(self):
        # return f"Home: {self.__home} \nStreet: {self.__street} \nDistrict: {self.__district} \nCity: {self.__city}"
        return f"Home: {self.__home}, Street: {self.__street}, District: {self.__district}, City: {self.__city}"

all = AllPeople()

def add_address():
    print("Let's enter address now: ")
    home = input("Home: ")
    street = input("Street: ")
    district = input("District: ")
    city = input("City: ")

    address = Address(home, street, district, city)

    data = address.get_address()
    return data

while True:
    print("Do you want to add more people to the school? y-(Yes) n-(No):")
    addMorePeople = input(">> ").lower()
    if addMorePeople == "y":
        while True:
            print("Who do you want to add? s-(Student) t-(Teacher). ")
            option = input(">> ").lower()
            if option == "s":
                firstName = input("Firstname: ")
                secondName = input("Secondname: ")
                born = input("Born in: ")
                address = add_address()
                id = len(all.get_all()) + 1
                print("Do you want to input grade or not? y-(Yes) n-(No): ")
                while True:
                    gradeOption = input(">> ").lower()
                    if gradeOption == "y":
                        while True:
                            grade = input("Enter grade 1-4: ")
                            if int(grade) in list(range(1, 5)):
                                student = Student(firstName, secondName, born, address, id, int(grade))
                                print("===== New student is added =====")
                                for key, value in student.get_info().items():
                                    print(f"{key}: {value}")
                                print(30*"=")
                                all.add_person(student.get_info())
                                break
                            else:
                                print("Grade should be between 1 and 4!!! Now, try again. ")
                                continue
                        break
                    
                    elif gradeOption == "n":
                        print("Okay, now your student is freshman by default!")
                        student = Student(firstName, secondName, born, address, id)
                        print("===== New student is added =====")
                        for key, value in student.get_info().items():
                            print(f"{key}: {value}")
                        print(30*"=")
                        all.add_person(student.get_info())
                        break
                    else:
                        print(f"{gradeOption} is not allowed!!! Try again. ")
                        continue

            elif option == "t":
                firstName = input("Firstname: ")
                secondName = input("Secondname: ")
                born = input("Born in: ")
                address = add_address()
                username = input("Username: ")
                degree = input("Degree, ex: (Master, PhD): ")
                teacher = Teacher(firstName, secondName, born, address, username, degree)
                print("===== New teacher is added =====")
                for key, value in teacher.get_info().items():
                        print(f"{key}: {value}")
                print(30*"=")
                all.add_person(teacher.get_info())
            else:
                print("Only (t/T) or (s/S) are allowed as an input! ")
                continue
            break
    elif addMorePeople == "n":
        for obj in all.get_all():
            print(30*"=")
            for key, value in obj.items():
                print(f"{key}: {value}")
            print(30*"=")
        break