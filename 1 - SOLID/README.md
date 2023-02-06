SOLID
=====

SOLID - это принципы разработки программного обеспечения, следуя которым Вы получите хороший код, который в дальнейшем будет хорошо масштабироваться и поддерживаться в рабочем состоянии.

# S - Single Responsibility Principle (SRP) - принцип единственной ответственности. Каждый класс должен иметь только одну зону ответственности.

Не нужно перегружать объекты "лишней ответственностями", иначе объекты превращаются в анти-паттерн, т.н. God code (In object-oriented programming, a god object (sometimes also called an omniscient or all-knowing object) is an object that references a large number of distinct types, has too many unrelated or uncategorized methods, or some combination of both. The god object is an example of an anti-pattern and a code smell).

# O - Open closed Principle (OCP) - принцип открытости-закрытости. Классы должны быть открыты для расширения, но закрыты для изменения.

# L - Liskov substitution Principle (LSP) - принцип подстановки Барбары Лисков. Должна быть возможность вместо базового (родительского) типа (класса) подставить любой его подтип (класс-наследник), при этом работа программы не должна измениться.

# I -  Interface Segregation Principle (ISP) - принцип разделения интерфейсов. Данный принцип обозначает, что не нужно заставлять клиента (класс) реализовывать интерфейс, который не имеет к нему отношения.

# D - Dependency Inversion Principle (DIP) - принцип инверсии зависимостей. Модули верхнего уровня не должны зависеть от модулей нижнего уровня. И те, и другие должны зависеть от абстракции.
