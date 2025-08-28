# Assignment 1: AI and Python - OOP Example

# Base class: AIModel
class AIModel:
    def __init__(self, name, model_type, accuracy):
        self.name = name
        self.model_type = model_type
        self.accuracy = accuracy

    def train(self):
        return f"{self.name} ({self.model_type}) is training..."

    def evaluate(self):
        return f"{self.name} has an accuracy of {self.accuracy * 100:.2f}%"


# Inheritance: Specific AI Models
class NeuralNetwork(AIModel):
    def __init__(self, name, accuracy, layers):
        super().__init__(name, "Neural Network", accuracy)
        self.layers = layers

    def train(self):
        return f"{self.name} with {self.layers} layers is training using backpropagation"


class DecisionTree(AIModel):
    def __init__(self, name, accuracy, depth):
        super().__init__(name, "Decision Tree", accuracy)
        self.depth = depth

    def train(self):
        return f"{self.name} with depth {self.depth} is training by splitting nodes"


# Polymorphism Example
def run_training(model: AIModel):
    print(model.train())
    print(model.evaluate())


# Assignment 2: Polymorphism Challenge

# Base class: Entity
class Entity:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving"


# Inheritance: Animals
class Dog(Entity):
    def move(self):
        return f"{self.name} is running"


class Bird(Entity):
    def move(self):
        return f"{self.name} is flying"


# Inheritance: Vehicles
class Car(Entity):
    def move(self):
        return f"{self.name} is driving"


class Plane(Entity):
    def move(self):
        return f"{self.name} is flying"


# Inheritance: Human
class Human(Entity):
    def move(self):
        return f"{self.name} is walking"


# Example Usage
if __name__ == "__main__":
    # Assignment 1
    nn = NeuralNetwork("ImageClassifier", 0.92, 5)
    dt = DecisionTree("SpamFilter", 0.85, 3)

    print("Assignment 1 Output")
    run_training(nn)
    print()
    run_training(dt)
    print("\n" + "="*50 + "\n")

    # Assignment 2
    entities = [
        Dog("Buddy"),
        Bird("Tweety"),
        Car("Tesla"),
        Plane("Boeing"),
        Human("Alice")
    ]

    print("Assignment 2 Output")
    for entity in entities:
        print(entity.move())
