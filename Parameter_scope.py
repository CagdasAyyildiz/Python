def with_parameters(value):
    print("parameter value : {}, global value".format(value))

    def inner_with_parameters():
        print("inner value:{}".format(value))  # Unresolved reference
        value = 4

    inner_with_parameters()
    print(("after inner: {}".format(value)))


value = 0
print("called with_parameters")
with_parameters(value)
