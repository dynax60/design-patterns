class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "    self.%s = %s" % (self.name, self.value)
    
class Class:
    def __init__(self, name):
        self.class_name = name
        self.fields = []

    def __str__(self):
        lines = []
        lines.append("class %s:" % self.class_name)
        if not self.fields:
            lines.append("  pass")
        else:
            lines.append("  def __init__(self):")
            for i in self.fields:
                lines.append(str(i))
        return "\n".join(lines)

class CodeBuilder:
    def __init__(self, root_name):
        self.cb = Class(root_name)

    def add_field(self, type, name):
        self.cb.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.cb.__str__()

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)