def global_keyword():
    global value
    print(value)
    # Output : 10


def local_value():
    value = 3
    print(value)


def outer1():
    value = 3
    print("outer1 value: {}".format(value))  # Output : 3

    def inner1():
        value = 5
        print("inner1 value: {}".format(value))  # Output : 5

    inner1()
    print("after inner 1 value: {}".format(value))  # Output : 3


def outer2():
    global value
    print("outer2 value: {}".format(value))  # Output : 10

    def inner2():
        global value
        value = 5
        print("inner2 value: {}".format(value))  # Output : 5

    inner2()
    value = 3
    print("after inner 2 value: {}".format(value))  # Output : 3


def outer3():
    value = 4
    print("outer3 value: {}".format(value))  # Output : 4

    def inner3():
        global value
        print("inner3 value: {}".format(value))  # Output : 3
        value = 5
        print("inner3 after value change value: {}".format(value))  # Output : 5

    inner3()
    print("after inner3 value: {}, value doesn't change".format(value))  # Output : 4


def with_parameters(value):
    print("parameter value : {}, global value".format(value))

    def inner_with_parameters():
        print("inner value:{}".format(value))
        #value = 4 error WHY?
    inner_with_parameters()
    print(("after inner: {}".format(value)))

value = 10

global_keyword()  # Output : 10
local_value()  # Output : 3

print("called outer1()")
outer1()  # Output : 3 5 3
print("Global: {}".format(value))  # Output : 10
print("Global value didn't change")

print("called outer2()")
outer2()  # Output 10 5 3
print("Global: {}".format(value))  # Output : 3
print("Global value changed with outer2")

print("called outer3")
outer3()
print("Global: {}".format(value))
print("inner3 changes the global value outer3 local value stays the same")

print("called with_parameters")
with_parameters(value)
