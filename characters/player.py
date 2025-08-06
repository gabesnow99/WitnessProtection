import numpy as np

'''
Base class for all characters
'''
class Player():

    def __init__(self, is_good=True, starting_location=[0., 0.], max_speed=10, endurance=10, blendability=10):
        # Properties
        self.is_good = is_good
        self.starting_location = np.array(starting_location, dtype=float).flatten()
        self.max_speed = max_speed
        self.endurance = endurance
        self.blendability = blendability
        # Stats
        self.alive = True
        self.location = np.copy(self.starting_location)
        self.direction = 0.
        self.speed = 0.
        self.stamina = self.max_speed * self.endurance

    # Step time forward
    def tick(self, dt=1):
        self.look_around()
        self.move(dt)

    # Propagate motion
    def move(self, dt):
        self.location += dt * self.speed * np.array([np.cos(self.direction), np.sin(self.direction)])

    # Stop moving
    def stop(self):
        self.speed = 0.

    # Go max speed
    def sprint(self):
        self.speed = self.max_speed

    # Observe nearby players
    def look_around(self):
        pass

    # Die
    def die(self):
        self.alive = False

    # Used to print info/stats on players
    def __str__(self):
        to_print = '===============================\n'
        to_print += f'Class:       {self.__class__.__name__}\n'
        to_print += f'Alignment:   {'Hero' if self.is_good else 'Villian'}\n'
        to_print += '-------------------------------\n'
        to_print += f'Status:      {'Alive' if self.alive else 'Dead'}\n'
        to_print += f'Location:    {self.location}\n'
        to_print += '==============================='
        return to_print