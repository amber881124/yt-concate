from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None  # data的初始值設為None
        for step in self.steps:
            try:
                # 接收：每個步驟執行完所return出來的東西(data)
                # 再傳進下一個step
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened', e)
                break
