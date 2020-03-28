class Flow(object):
    recolector = None
    executor = None
    writer = None

    @classmethod
    def start(cls):
        data = cls.recolector.recolect()
        data = cls.executor.execute(data)
        extra_effects = cls.executor.get_effects()
        return cls.writer.run(data, extra_effects)
