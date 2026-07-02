# Task 3: Chat System using OOP

class User:
    def __init__(self, name):
        self.name = name

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def display(self):
        return f"{self.sender.name}: {self.text}"

class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.name, "joined the chat room.")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(user.name, "left the chat room.")

    def send_message(self, sender, text):
        if sender in self.users:
            message = Message(sender, text)
            self.messages.append(message)
            print("Message Sent!")
        else:
            print(sender.name, "is not in the chat room.")

    def view_history(self):
        print("\n----- Chat History -----")
        if len(self.messages) == 0:
            print("No messages.")
        else:
            for message in self.messages:
                print(message.display())
# Driver Code

chat = ChatRoom()

user1 = User("Ali")
user2 = User("Sara")

chat.join(user1)
chat.join(user2)

chat.send_message(user1, "Hello Everyone!")
chat.send_message(user2, "Hi Ali, how are you?")
chat.send_message(user1, "I'm fine. Thanks!")

chat.view_history()

chat.leave(user2)