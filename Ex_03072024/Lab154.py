class ABC:
    def func1(self):
        try:
            num = int(input("Enter a number : "))
        except Exception as e:
            print("Enter int only value of number")
        else:
            print(num)
        finally:
            print("FINALLY : Anyhow I will be printed")


a = ABC()
a.func1()
