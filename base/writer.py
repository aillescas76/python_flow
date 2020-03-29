class Writer(object):
    @staticmethod
    def write(data):
        pass

    @classmethod
    def run(cls, data, extra_effects):
        cls.write(data)
        for side_effect in extra_effects:
            side_effect.write(data)
        return data
