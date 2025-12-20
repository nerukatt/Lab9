class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def get_radius(self):
        return f'Радиус равен: {self.radius}'

    def set_radius(self, new_radius):
        self.radius = new_radius
        
Circle1=Circle('134')
print(Circle1.get_radius())

rad=int(input("Задайте новый радиус: "))
Circle1.set_radius(rad)
print(Circle1.get_radius())