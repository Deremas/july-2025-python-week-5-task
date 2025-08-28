# Python OOP Assignments - Dereje Masresha

GitHub: [Deremas](https://github.com/Deremas)

## Overview

This repository contains two Python OOP assignments demonstrating:

- **Classes, attributes, and methods**
- **Constructors**
- **Inheritance**
- **Polymorphism**
- **Encapsulation concepts**

---

## Assignment 1: AI and Python - OOP Example

### Description

- Create a base class `AIModel` representing AI models.
- Derived classes `NeuralNetwork` and `DecisionTree` inherit from `AIModel`.
- Each class implements a `train()` method differently.
- Use constructors to initialize attributes dynamically.

### Example Usage

```python
nn = NeuralNetwork("ImageClassifier", 0.92, 5)
dt = DecisionTree("SpamFilter", 0.85, 3)

run_training(nn)
run_training(dt)
```

### Output

```text
ImageClassifier with 5 layers is training using backpropagation
ImageClassifier has an accuracy of 92.00%

SpamFilter with depth 3 is training by splitting nodes
SpamFilter has an accuracy of 85.00%
```

## Assignment 2: Polymorphism Challenge

### Description

- Create a base class `Entity`.
- Derived classes include `Dog`, `Bird`, `Car`, `Plane`, and `Human`.
- Each class implements `move()` differently.
  Demonstrates polymorphism in Python.

### Example Usage

```python
entities = [
    Dog("Buddy"),
    Bird("Tweety"),
    Car("Tesla"),
    Plane("Boeing"),
    Human("Alice")
]

for entity in entities:
    print(entity.move())
```

### Output

```text
Buddy is running
Tweety is flying
Tesla is driving
Boeing is flying
Alice is walking
```

## If You want to run this code locally

Follow these steps to clone and run the project locally:

### Prerequisites

Make sure you have **Python 3.7+** installed. You can check your version with:

```bash
python --version
```

### Clone the Repository

```python
git clone git@github.com:Deremas/july-2025-python-week-5-task.git
cd july-2025-python-week-5-task
```

### Run the Project

```python
python python-oop-assignment.py
```

## Concepts Covered

- Python Classes & Objects
- Attributes and Methods
- Constructors (init)
- Inheritance & Super()
- Polymorphism (method overriding)
- Encapsulation (through controlled methods)
- Dynamic instantiation (objects with unique attributes)

## Author

### Dereje Masresha

### GitHub: [Deremas](https://github.com/Deremas)
