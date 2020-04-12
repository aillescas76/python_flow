from itertools import chain

class Executor(object):
    step_list = []
    step_set = {}

    @classmethod
    def execute(cls, data):
        for step in cls.step_list:
            data = step.run(data)

        for step in cls.step_set:
            data = step.run(data)
        return data

    @classmethod
    def get_extra_effects(cls):
        effects = []
        for step in chain(cls.step_list, cls.step_set):
            effects.extend(step.side_effects())
        return effects
