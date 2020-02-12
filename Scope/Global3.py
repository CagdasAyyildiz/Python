def outer():
    value = 4
    print("outer value: {}".format(value))  # Output : 4

    def inner3():
        global value
        print("inner value: {}".format(value))  # Output : 0
        value = 5
        print("inner after value change value: {}".format(value))  # Output : 5

    inner3()
    print("after inner value: {}, value doesn't change".format(value))  # Output : 4


value = 0
print("called outer")
outer()
print("Global: {}".format(value))
print("inner3 changes the global value outer3 local value stays the same")
