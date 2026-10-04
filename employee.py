
class Employee:
    '''
    DTO concept later we learnS
    '''
    def __init__(self, id, name, department):
        self.Id = id
        self.Name = name
        self.Department = department

    def display_info(self):
        print(f"ID: {self.Id}, Name: {self.Name}, Department: {self.Department}")