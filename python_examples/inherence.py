
class Something(object):
    def __init__(self, message: str) -> None:
        self.message = message
    def printer(self) -> str:
        return self.message

class Son(Something):
    def __init__(self, sms: str) -> None:
        super(Son, self).__init__(sms)

    def message_son(self) -> None:
        print(self.printer()+" <- message son")

    def printer(self) -> str:
        print(super(Son, self).printer()+" <- message father")
        print("my message SON")
        return "PRINT THIS"

a = Son("this message")
a.message_son()
a.printer()
