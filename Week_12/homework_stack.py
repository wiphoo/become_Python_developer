

class Stack():

    def __init__(self):
        pass

    def add(self, val):
        pass

    def get(self):
        pass

    def __len__(self):
        pass

    def __repr__(self):
        pass


def main():

    my_stack = Stack()

    my_stack.add("Grace")
    assert len(my_stack) == 1

    result = my_stack.get()
    assert result == "Grace"

    my_stack.add("Grand")
    my_stack.add("Grace")    
    assert len(my_stack) == 2

    result = my_stack.get()
    assert result == "Grace"
    result = my_stack.get()
    assert result == "Grand"

if __name__ == "__main__":
    main()