from celery import task
from celery import Task
from ansible import runner
@task()
def add(x, y):
    return x + y

@task()
def modrun(inventory, mod, args ):
    result = runner.Runner(
        pattern=inventory,
        module_name=mod,
        module_args=args,
    ).run()
    print result

    return result


class ModRun(Task):

    def __init__(self, inventory, mod, args):
        self.inventory = inventory
        self.mod = mod
        self.args = args


    def run(self):
        return runner.Runner(
            pattern=self.inventory,
            module_name=self.mod,
            module_args=self.args
        ).run()


