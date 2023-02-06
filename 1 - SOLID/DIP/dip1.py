# DIP

from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Relationships:
    def __init__(self) -> None:
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

class Research:
    def __init__(self, relationships) -> None:
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'Jhon' and r[1] == Relationship.PARENT:
                print(f'Jhon has a child called {r[2].name}.')

parent = Person('Jhon')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
