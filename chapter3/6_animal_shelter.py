# Animal Shelter
# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter, or they can select
# whether they would prefer a dog or a cat (and will receive the oldest animal
# of that type). They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations
# such as enqueue, dequeue_any, dequeue_dog, and dequeue_cat.

from myqueue import Queue
import random
from typing import List
import unittest


class Animal:
    """Class for animals in AnimalShelter"""
    CAT = 1
    DOG = 2

    def __init__(self, kind: int, name: str, time: int = None):
        self.kind = kind
        self.name = name
        self.time = time


class AnimalShelter():
    """Class for animal shelter as described in the problem"""

    def __init__(self, animals: List[Animal]):
        self.time = 0
        self.dogq = Queue()
        self.catq = Queue()
        if animals is not None:
            for animal in animals:
                self.enqueue(animal)

    def enqueue(self, animal: Animal) -> None:
        """Add cat or dog Animal to animal shelter"""
        self.time += 1
        animal.time = self.time
        if animal.kind == Animal.CAT:
            self.catq.add(animal)
        elif animal.kind == Animal.DOG:
            self.dogq.add(animal)
        else:
            raise TypeError("enqueue can only be called on dog or cat")

    def dequeue_any(self):
        """Dequeue first animal in animal shelter"""
        if self.catq.isempty() and self.dogq.isempty():
            raise Exception("dequeue_any called on empty shelter")
        cattime = self.catq.peek().time if not self.catq.isempty() else float("inf")
        dogtime = self.dogq.peek().time if not self.dogq.isempty() else float("inf")
        if cattime <= dogtime:
            return self.catq.remove()
        else:
            return self.dogq.remove()

    def dequeue_cat(self):
        """Dequeue first cat in animal shelter"""
        return self.catq.remove()

    def dequeue_dog(self):
        """Dequeue first dog in animal shelter"""
        return self.dogq.remove()


def generate_animals() -> (List[Animal], List[Animal], List[Animal]):
    """Returns shuffled list of animals, then separated lists by cats and dogs"""
    catnames = ["Oliver", "Simba", "Leo", "Tiger", "Tigger",
                "Chloe", "Lucy", "Sophie", "Luna", "Gracie"]
    dognames = ["Charlie", "Max", "Buddy", "Oscar", "Milo",
                "Bella", "Molly", 'Coco', "Ruby", "Lucy"]
    animals = [Animal(Animal.CAT, name) for name in catnames]
    animals.extend([Animal(Animal.DOG, name) for name in dognames])
    cats = []
    dogs = []
    random.shuffle(animals)
    for animal in animals:
        if animal.kind == Animal.CAT:
            cats.append(animal)
        elif animal.kind == Animal.DOG:
            dogs.append(animal)
    return animals, cats, dogs


class TestAnimalShelter(unittest.TestCase):
    def test_dequeue_dog(self):
        animals, _, dogs = generate_animals()
        shelter = AnimalShelter(animals)
        for i in range(len(dogs)):
            with self.subTest(i=i):
                self.assertEqual(shelter.dequeue_dog().name, dogs[i].name)

    def test_dequeue_cat(self):
        animals, cats, _ = generate_animals()
        shelter = AnimalShelter(animals)
        for i in range(len(cats)):
            with self.subTest(i=i):
                self.assertEqual(shelter.dequeue_cat().name, cats[i].name)

    def test_dequeue_any(self):
        animals, _, _ = generate_animals()
        shelter = AnimalShelter(animals)
        for i in range(len(animals)):
            with self.subTest(i=i):
                self.assertEqual(shelter.dequeue_any().name, animals[i].name)


if __name__ == "__main__":
    unittest.main()
