class Square:	
	side=5
	def calculate_area(self):
		return self.side * self.side
class Triangle:
	base=5
	height=4
	def calculate_area(self):
		return 0.5*self.base * self.height
sq=Square()
tri=Triangle()
print("Area of Square:”, sq. calculate_area())
print("Area of Triangle:”, tri. calculate_area())
