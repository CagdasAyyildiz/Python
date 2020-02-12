def outer():
    global value
    print("outer value: {}".format(value))  # Output : 0

    def inner():
        global value
        value = 5
        print("inner value: {}".format(value))  # Output : 5

    inner()
    value = 3
    print("after inner value: {}".format(value))  # Output : 3


value = 0
print("called outer")
outer()  # Output 0 5 3
print("Global: {}".format(value))  # Output : 3
# Global value changed with outer
