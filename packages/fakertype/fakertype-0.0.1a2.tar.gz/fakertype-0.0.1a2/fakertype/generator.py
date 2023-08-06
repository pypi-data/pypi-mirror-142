import random

class int_generator:
    def __init__(self, lb=1, ub=10, seed=None):
        """Return int between lb and ub (including both end points) for every call

        Args:
            lb (int, optional): lower bound. Defaults to 1.
            ub (int, optional): upper bound. Defaults to 10.
        """
        self.lb = lb
        self.ub = ub

        self.seed = seed
        if self.seed is None:
            self.rng = random.Random()
        else:
            self.rng = random.Random(self.seed)
            
    def __call__(self):
        return self.rng.randint(self.lb,self.ub)

    def __iter__(self):
        return self

    def __next__(self):
        return self.rng.randint(self.lb,self.ub)
