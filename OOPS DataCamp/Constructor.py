class Engineering():
    def __init__(self, Department, Year_Of_Joining, Average_12, Maths_marks):
        self.Departmrnt= Department
        self.Year_Of_Joining=Year_Of_Joining
        self.Average_12= Average_12
        self.Maths_Marks= Maths_marks
    def Calculations_Admission(self):
        return self.Average_12 + (self.Maths_Marks) *2
CSE= Engineering('CSE',2016,85,98)
Pharmacy=Engineering('Pharmacy', 2016, 80,90)

print(f"Total Marks Out of 300 For Admission" , CSE.Calculations_Admission())
