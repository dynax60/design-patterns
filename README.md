SOLID
=====

The SOLID ideas are

1. The Single-responsibility principle (SRP): "There should never be more than one reason for a class to change." In other words, every class should have only one responsibility. SOC (Separations of Concern) - the same thing.

Цель - не перегружать ваши объекты "лишними обязанностями", иначе объекты превращаются в God code, такой код является плохим.

Анти-паттерн, т.н. God code - In object-oriented programming, a god object (sometimes also called an omniscient or all-knowing object) is an object that references a large number of distinct types, has too many unrelated or uncategorized methods, or some combination of both. The god object is an example of an anti-pattern and a code smell.

2. The Open–closed principle: "Software entities ... should be open for extension, but closed for modification."

Принцип OCP в добавлении функционала производится через расширение, а не исправление.
