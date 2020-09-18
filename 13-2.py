class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False

    def turnOn(self):
        if(self.on):
            print("TV가 이미 켜져있습니다.")
        else:
            self.on=True
            print("TV 켜짐")
    def turnOff(self):
        if(self.on):
            self.on=False
            print("TV 꺼짐")
        else:
            print("이미 꺼져있습니다.")
    def setChannel(self, channel):
        self.chennel=channel
        print("채널 : "+ str(self.chennel) + "볼륨 : " + str(self.volume))
        
    def setVolume(self, volume):
        self.volume=volume
        print("채널 : "+ str(self.chennel) + "볼륨 : " + str(self.volume))
        
myTV =  TV()
myTV.turnOn()
myTV.turnOn()
myTV.setChannel(11)
myTV.setChannel(12)
myTV.setVolume(11)
myTV.setVolume(12)

myTV.turnOff()
myTV.turnOff()
