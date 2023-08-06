on_start_callback = lambda steps: ()
on_step_start_callback = lambda name: ()
on_step_finish_callback = lambda: ()
on_finish_callback = lambda info: ()

class Step:
    def __init__(self, name: str):
        on_step_start_callback(name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        on_step_finish_callback()


class Taskeeper:
    def __init__(self, steps: int):
        self.info: str = None
        on_start_callback(steps)

    def __enter__(self):
        return self
    
    def step(self, name: str) -> Step:
        return Step(name)

    def set_info(self, info:str):
        self.info = info

    def __exit__(self, exc_type, exc_value, traceback):
        on_finish_callback(self.info)
        

def taskeeper(steps:int):
    return Taskeeper(steps)


