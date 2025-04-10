class StarCookie:
    milk = 0.1
    
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


starCookie1 = StarCookie("red", 10)
print(starCookie1.color)
print(starCookie1.__dict__) # show the dictionary of the object
print(StarCookie.__dict__)

starCookie1.milk = 0.2
print(starCookie1.__dict__)
StarCookie.milk = 0.5
print(starCookie1.__dict__)
print(StarCookie.__dict__)


class Youtube:
    def __init__(self, username, subscribers=0):
        self.username = username
        self.subscribers = subscribers
        
user1 = Youtube('Arbabian')
print(user1.subscribers)