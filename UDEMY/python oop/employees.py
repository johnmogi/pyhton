class Employee:
    def __init__(self, first_name, last_name, salary, shift):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.shift = shift

    def get_full_name(self):
        return f'{self._last_name} {self._first_name}'

    # def get_work_hours(self):
    #     return f'{self.start_time} : {self.end_time}'

class Mechanic(Employee):
    job_title = "Mechanic"

class Attendant(Employee):
    job_title = "Station Attendant"

class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"

