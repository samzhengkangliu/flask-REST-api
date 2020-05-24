# Class Inheritance

class Device: 
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        # !r calls wrapper method and puts on quotes on self.name
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")
    
# Inheritance in Python    
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # gets the super class Device and call the init method in Device
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -=pages
    
printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

printer.disconnect()
printer.print(30)