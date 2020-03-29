class Flow(object):
    recolector = None
    executor = None
    writer = None

    @classmethod
    def start(cls, initial_data):
        data = cls.recolector.recolect(initial_data)
        data = cls.executor.execute(data)
        extra_effects = cls.executor.get_effects()
        return cls.writer.run(data, extra_effects)
