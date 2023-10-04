

class MovingAnimal:
    """Returns a string describing how an animal moves.

    Attributes
    ----------
    ambulation: str
        A string describing how an animal moves.
    
    Methods
    -------
    move()
        Returns ambulation string.
    """
    def __init__(self, ambulation: str):
        self.ambulation = ambulation

    def move(self):
        return self.ambulation


class Cat(MovingAnimal):
    def __init__(self):
        super().__init__("Cats prowl")

class Kangaroo(MovingAnimal):
    def __init__(self):
        super().__init__("Kangaroos hop.")

class Snake(MovingAnimal):
    def __init__(self):
        super().__init__("Snakes slither.")

if __name__ == "__main__":
    print(f"Cat: {Cat().move()}")
    print(f"Kangaroo: {Kangaroo().move()}")
    print(f"Snake: {Snake().move()}")