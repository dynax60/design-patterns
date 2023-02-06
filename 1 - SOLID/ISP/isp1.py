# ISP
# Плохой подход (чего-то вспомнился Netmiko :-)

class Machine:
    def print(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    
    def fax(self, document):
        pass
    
    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass
    
    def fax(self, document):
        pass  # noop
    
    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('This printer cannot scan!')
