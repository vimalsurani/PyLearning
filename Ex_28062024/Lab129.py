class Sample:
    def m1(self):
        print("m1 is instance method called with object name")


s1 = Sample()
s1.m1()
print(dir(Sample))
