import random

class RNG:
    def __init__(self, seed):
        self.seed = seed

    @staticmethod
    def toss() -> bool:
        return random.getrandbits(1)

    def seed(self, seed_int:int) -> None:
        self.seed = seed_int
        random.seed(self.seed)

    def get_seed(self) -> int:
        return self.seed