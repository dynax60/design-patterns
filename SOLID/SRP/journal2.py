# SRP SOC
# Пример плохого использования, где в классе появляется дополнительный функционал (secondary responsibility),
# который несёт в себе дополнительную нагрузку - сохранение и загрузку данных. Это плохая идея. См. journal3.py,
# как можно реализовать этот функционал
#

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text) -> None:
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos) -> None:
        del self.entries[pos]
    
    def __str__(self) -> str:
        return '\n'.join(self.entries)

    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, url):
        pass


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')