class HelloWorldService:
    def __init__(self):
        self.messages = {
            'welcome': "Welcome to Hello World! You can say hello or help.",
            'hello': "Hello World!",
            'help': "You can say hello to me!",
            'goodbye': "Goodbye!"
        }

    def get_welcome_message(self):
        return self.messages['welcome']
    
    def get_hello_message(self):
        return self.messages['hello']
    
    def get_help_message(self):
        return self.messages['help']
    
    def get_goodbye_message(self):
        return self.messages['goodbye']

    def get_personalized_message(self, name=None):
        base_message = self.get_hello_message()
        if name:
            return f"{base_message} Nice to meet you, {name}!"
        return base_message