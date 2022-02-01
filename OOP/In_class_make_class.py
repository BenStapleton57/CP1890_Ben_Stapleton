import math

class Address:
        def __init__(self,street_address, city_name, state_name, post_code, country_name):
            self.street = street_address
            self.city = city_name
            self.state = state_name
            self.postal_code = post_code
            self.country = country_name

        def to_string(self):
            return f'{self.street} {self.city}, {self.state}, {self.postal_code}, {self.country}'



my_address = Address(street_address="123 Fake Place", city_name="Toon Town", state_name="Toonamus",\
                     post_code="A2R 2YW", country_name="Toonanda")
work_address = Address(street_address="101 Not Real Place", city_name="Toon Town", state_name="Toonamus",\
                     post_code="A2T 3YW", country_name="Toonanda")

print(my_address.to_string())
print(work_address.to_string())

class Circle:
    def __init__(self, radius_length):
        self.radius = radius_length

    def get_area(self):
        area = math.pi * (self.radius **2)
        return area

    def get_circumerence(self):
        circumference = (math.pi * 2) * (self.radius)
        return circumference

small_circle = Circle(radius_length= 2.2)
big_circle = Circle(radius_length= 20.2)

print(small_circle.get_area())

print(small_circle.get_circumerence())
