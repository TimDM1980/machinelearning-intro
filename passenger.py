class Passenger():

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def get_name(self):
        return 'Mr ' + self.name
