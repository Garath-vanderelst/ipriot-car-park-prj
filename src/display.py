class Display:
    def __init__(self, id, message, is_on):
        self.id = id
        self.message = message or ''
        self.is_on = is_on or False

    def __str__(self):
        return f'Display {id}: {message}.'



