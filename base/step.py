class Step(object):
    side_effects = []

    @classmethod
    def run(data):
        return data

    @classmethod
    def side_effects(cls):
        return cls.side_effects
