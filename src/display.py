class Display:
    def __init__(self, id, message, is_on, car_park):
        self.id = id
        self.is_on = is_on or False
        self.message = message
        self.data = {'message': self.message or ''}

    def __str__(self):
        return f'Display {id}: {message}.'

    def update(self, data):
        for key, value in data.items():
            self.data[key] = value


