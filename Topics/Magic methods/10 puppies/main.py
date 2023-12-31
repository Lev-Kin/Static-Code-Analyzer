class Puppy:
    n_puppies = 0  # number of created puppies

    def __new__(cls, *args, **kwargs):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return super().__new__(cls)
        else:
            return None