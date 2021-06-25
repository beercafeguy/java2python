class motor_bike:

    def __init__(self,gear,speed):
        self.gear=gear
        self.speed=speed

    def __repr__(self):
        return repr((self.gear,self.speed))

    def start(self):
        print("starting bike")

pulsar=motor_bike(5,150)
print(pulsar)
pulsar.start()