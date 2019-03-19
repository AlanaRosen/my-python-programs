class Car:
    def __init__(self,gas):
        """Initiates Car class"""
        self.gas_level = gas
    def get_gas(self):
        """Tells you the gas level"""
        return(self.gas_level)
    def add_gas(self,new_gas):
        """If you add gas to the car, this changes the state of car gas level to the new gas level"""
        self.gas_level = self.gas_level + new_gas
    def fill_up(self):
        """Shows how much gas you need to fill the tank up to 13.0"""
        if self.gas_level >= 13.0:
            return(0)
        else:
            full_gas = 13
            added_gas = full_gas - self.gas_level
            self.add_gas(added_gas)
            return(added_gas)

def main(): 
#Here’s an example.
    example_car = Car(9)
    print(example_car.fill_up())  # should print 4

    another_car = Car(18)
    print(another_car.fill_up()) # should print 0

    print(example_car.get_gas())
    print(another_car.get_gas())

if __name__ == "__main__":
    main()