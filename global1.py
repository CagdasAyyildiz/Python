def outer():
    value = 3
    print("outer value: {}".format(value))  # Output : 3

    def inner():
        value = 5
        print("inner value: {}".format(value))  # Output : 5

    inner()
    print("after inner  value: {}".format(value))  # Output : 3


value = 0
print("called outer")
outer()  # Output : 3 5 3
print("Global: {}".format(value))  # Output : 0
# Global value didn't change
