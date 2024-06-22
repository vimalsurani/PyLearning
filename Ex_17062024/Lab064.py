def make_pizza(*topings):     # * - Any arguments
    # print(topings)          # O/P -> Tuple
    for topin in topings:
        print(topin)


vimal = make_pizza("tomato")
rahul = make_pizza("Olives", "mushroom", "paneer")
milan = make_pizza("mushroom", "pineapple", "paneer", "sweetcorn")
