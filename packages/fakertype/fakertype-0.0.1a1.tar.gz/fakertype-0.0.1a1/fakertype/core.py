import random
from faker import Faker

class FakerType:
    def __init__(self):
        self.fake = Faker()
        pass

    def fake_dict(self, n=None, key_generator=None, val_generator=None):
        if key_generator is None:
            key_generator = self.fake.name
        if val_generator is None:
            val_generator = self.fake.city
        if n is None:
            n = random.randint(1,100)
        return {key_generator(): val_generator() for i in range(n)}

    def fake_list(self, n=None, val_generator=None):
        if val_generator is None:
            val_generator = self.fake.city
        if n is None:
            n = random.randint(1,100)
        return [val_generator() for i in range(n)]
        