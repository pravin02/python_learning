from classes import Vehicle


class TestClasses:

    @classmethod
    def setup_class(cls):
        cls.vehicle = Vehicle("Audi","3")
        print("setup")
    
    @classmethod
    def teardown_class(cls):
        del cls.vehicle
    
    def test_number_of_wheels(self):
        assert self.vehicle.wheels == 4