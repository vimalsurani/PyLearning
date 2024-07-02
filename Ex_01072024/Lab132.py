# Hierarchical Inheritance

# Father - Multiple Children
class Father:

    def One_BHK(self):
        print("Father's 1BHK House")


class Vimal(Father):

    def Two_BHK(self):
        print("Vimal's 2BHK House")


class Rahul(Father):

    def Three_BHK(self):
        print("Rahul's 3BHK House")


class Mohit(Father):

    def No_House(self):
        print("Mohit have No House")


vimal = Vimal()
vimal.One_BHK()
vimal.Two_BHK()

rahul = Rahul()
rahul.One_BHK()
rahul.Three_BHK()
# rahul.Two_BHK()  # this is belong to vimal

mohit = Mohit()
mohit.One_BHK()
mohit.No_House()
# mohit.Two_BHK()  # this is belong to vimal
# mohit.Three_BHK() # this is belong to rahul





