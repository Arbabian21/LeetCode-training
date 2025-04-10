class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    
    def print(self):
        print(f"This is {self.username} with {self.subscribers} number of subscribers and {self.subscriptions} number of subscriptions.")
        
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1
        
arbab = Youtube("Arbabian")
judah = Youtube("Fujoshi")
arbab.print()
arbab.subscribe(judah)
judah.print()
arbab.print()
