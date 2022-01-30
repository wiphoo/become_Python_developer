

class Queue():

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

    my_queue = Queue()

    my_queue.add("Grace")
    assert len(my_queue) == 1

    result = my_queue.get()
    assert result == "Grace"

    my_queue.add("Grand")
    my_queue.add("Grace")    
    assert len(my_queue) == 2

    result = my_queue.get()
    assert result == "Grand"
    result = my_queue.get()
    assert result == "Grace"

if __name__ == "__main__":
    main()