class Task:
    def __init__(self, value):
        self.value = value

    def execute(self):
        new_value = self.value**2
        self.value = new_value
        return self.value
