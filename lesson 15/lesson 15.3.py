class TVController:

    def __init__(self, CHANNELS):
        self.CHANNELS = CHANNELS
        self.channel_index = 0

    def first_channel(self):
        self.channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.channel_index = len(self.CHANNELS) - 1
        return self.current_channel()

    def turn_channel(self, x):
        if x < 1 or x > len(self.CHANNELS):
            print('Такого канала немає!')
        self.channel_index = x-1
        return self.current_channel()

    def next_channel(self):
        self.channel_index = (self.channel_index + 1) % len(self.CHANNELS)
        return self.current_channel()

    def previous_channel(self):
        self.channel_index = (self.channel_index - 1) % len(self.CHANNELS)
        return self.current_channel()
    def current_channel(self):
        return self.CHANNELS[self.channel_index]

    def is_exist(self, channel):
        if type(channel) == str:
            return 'Yes' if channel in self.CHANNELS else 'No'
        elif type(channel) == int:
            return 'Yes' if 1<= channel <= len(self.CHANNELS) else 'No'
        else:
            print('invalid argument')


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(3))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(2))
print(controller.is_exist("BBC"))
