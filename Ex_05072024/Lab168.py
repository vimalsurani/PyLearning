import os

all_dir = os.listdir("Users/ViMS/PycharmProjects/PyLearning/Ex_05072024")
print(all_dir)

# Environment Variables

# set an environment Variables

os.environ['MY_VAR'] = "Vimal"
print(os.getenv("MY_VAR"))
