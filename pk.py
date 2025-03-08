


class PickleImage:
    def __init__(self, name: str, colories: float):
        self.name = name
        self.colories = colories

    def describe(self):
        print(self.name, self.colories, sep=": ")


if __name__ == "__main__":
    
    fruit: PickleImage = PickleImage("Mango", 2333.3)
    fruit.describe()
