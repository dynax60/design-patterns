# DIP

from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name) -> None:
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self) -> None:
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:  # high level module
    def __init__(self, browser) -> None:
        for p in browser.find_all_children_of('Jhon'):
            print(f'Jhon has a child called {p}')

parent = Person('Jhon')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
