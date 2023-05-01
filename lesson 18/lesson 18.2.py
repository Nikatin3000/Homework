
class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        self.workers.append([worker.name,worker.id,worker.company])
    def get_workers(self):
        return self.workers

    def __str__(self):
        return f'name: {self.name},company: {self.company}, id: {self.id}'

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, other):
        if not isinstance(other,Boss):
            raise 'boss not found'
        self.boss = other
    def __str__(self):
        return f'id: {self.id},name: {self.name},company: {self.company},boss: {self.boss}'

boss1 = Boss(1,'Ibrahim','ATB')
boss2 = Boss(2,'Pupkin','Fora')

worker1 = Worker(1,'Vasul','ATB', boss1)
worker2 = Worker(2,'Petro','ATB',boss1)

print(worker1.get_boss)

worker1.get_boss = boss2
print(worker1.get_boss)

boss1.add_worker(worker1)
print(boss1.workers)

