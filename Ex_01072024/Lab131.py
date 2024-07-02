class Parent:
    gold = "3kg"

    def TWO_BHK(self):
        print("2BHK House")


class Child(Parent):

    def THREE_BHK(self):
        print("3BHK House")


child_obj_ref = Child()
child_obj_ref.TWO_BHK()
child_obj_ref.THREE_BHK()
print(child_obj_ref.gold)


father_obj_ref = Parent()
# father_obj_ref.TWO_BHK()
# print(father_obj_ref.gold)
# father_obj_ref.THREE_BHK()
