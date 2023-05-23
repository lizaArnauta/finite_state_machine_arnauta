import random

class StateMachine:
    SLEEP = 'Sleep'
    EAT = 'Eat'
    WORK = 'Work'
    RELAX = 'Relax'
    CRY = 'Cry'
    SMOKE = 'Smoke'
    SOCIALIZE = 'Socialize'
    def __init__(self):
        self.state = StateMachine.SLEEP
        self.energy = 100
        self.hunger = 0
    
    def transition(self, hour):
        if self.state == StateMachine.SLEEP:
            if random.random() < 0.6 and hour == 7:
                print('Новий день ура!')
                self.state = StateMachine.EAT
            elif hour == 8:
                print("Я проспала! Знов плачі")
                self.state = StateMachine.CRY
        elif self.state == StateMachine.EAT:
            if hour == 9:
                print('Смачно поснідала!) Тепер тре йти на пари!')
                self.state = StateMachine.WORK
            elif hour == 15:
                print('Час для обіду. Йду в трапезну.')
                self.state = StateMachine.WORK
            elif hour == 18:
                print('Треба повечеряти!')
                self.state = StateMachine.RELAX
        elif self.state == StateMachine.WORK:
            if hour == 8:
                print("перша пара... треш")
                self.state = StateMachine.WORK
            if hour == 12:
                print('роблю лабу і практичні з дискретної!')
                self.state = StateMachine.CRY
            if hour == 17:
                print('Пари всьо! треба йти робити практичні. знов плачі.')
                self.state = StateMachine.RELAX
            elif random.random() < 0.1:
                print('Страшенно втомлена... треба піти покурити')
                self.state = StateMachine.SMOKE
        elif self.state == StateMachine.RELAX:
            if random.random() < 0.4 and hour >= 19:
                print('Мені сумно( треба потеревеніти з кимось')
                self.state = StateMachine.SOCIALIZE
        elif self.state == StateMachine.CRY:
            if hour == 9:
                print('Плакаю. Мені сумно. Треба перекусити!')
                self.state = StateMachine.EAT
            else:
                print('Просто плачі. як завжди.')
                self.state = StateMachine.WORK
        elif self.state == StateMachine.SMOKE:
            if hour >= 18:
                print('Файно подихала повітрям)')
                self.state = StateMachine.WORK
        elif self.state == StateMachine.SOCIALIZE:
            if hour >= 22:
                print('Прекрасно провела час! Тре тепер йти спати')
                self.state = StateMachine.SLEEP
        
        if hour == 23:
            print("ліза намагалась відпочти, але її загризла совість! роблю знов практичну(")
            self.state = StateMachine.SLEEP

    
    def run_day(self):
        print('zzz...')
        for hour in range(24):
            self.transition(hour)
            self.update_indicators(hour)
        print('zzz...')

    
    def update_indicators(self, hour):
        if hour == 8:
            self.energy -= 10
        elif hour == 9:
            self.hunger += 10
        elif hour == 12:
            self.energy -= 15
            self.hunger += 10
        elif hour == 15:
            self.energy -= 10
            self.hunger += 5
        elif hour == 18:
            self.energy -= 10
            self.hunger += 5
        elif hour == 19:
            self.energy -= 5

        if self.energy < 10:
            if self.state != StateMachine.SLEEP:
                print('я втомлена. треба відпочити')
                self.state = StateMachine.SLEEP
        elif self.hunger >= 40:
            if self.state != StateMachine.EAT:
                print('я хочу їсти. треба піти в трапезну!')
                self.state = StateMachine.EAT


machine = StateMachine()
machine.run_day()
