class Flight:
    #instance initializer not constructor
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"'{number}'")
        if not number[:2].isupper():
            raise ValueError(f"'{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 999):
            raise ValueError(f"'{number}'")

        self._number = number #implementation details
        self._aircraft = aircraft

    def aircraft_model(self):
        return self._aircraft.model() #access model from Flight object 

    def number(self):
        #001
        return self._number

    def airline(self):
        #AF
        return self._number[:2]

class Aircraft:
    def __init__(self, model,num_rows, num_seats_per_row):
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def model(self):
        return self._model

    def seating_plan(self):
        # range and string bundled up into a tuple
        return (range(1, self._num_rows + 1),"ABCDEFGHJ"[:self._num_seats_per_row])

#f = Flight("AF001", Aircraft("Airbus A360", num_rows=22, num_seats_row=6))