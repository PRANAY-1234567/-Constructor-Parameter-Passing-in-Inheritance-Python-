class Base():
    def __init__(self, x):
        print("Inside class Base constructor, value is", x)

class Derived(Base):
    def __init__(self, v):
        super().__init__(v)
        print("Inside class Derived constructor")

if __name__ == "__main__":
    obj = Derived(157)
