class Record:


    def __init__(self, id, name, value, createdAt):
        self.id = id
        self.name = name
        self.value = value 
        self.createdAt = createdAt 


    def __str__(self):
        return f"{self.id} | {self.name} | {self.value} | {self.createdAt}"