class AbstractPhoneState:

    def __init__(
            self,
            number: str,
    ):
        self.number = number

    def call(self, phone_number: str):
        print(f'Trying to call {phone_number} from {self.number}...')

    def answer(self):
        print(f'Answering to incoming call to {self.number}...')

    def top_up_balance(self):
        print(f"Topping up the balance of {self.number}...")


class BlockedPhoneState(AbstractPhoneState):
    def call(self, phone_number: str):
        print(f'Not enough money to call  from {self.number}...')


class WorkingPhoneState(AbstractPhoneState):
    def call(self, phone_number: str):
        print(f'Calling {phone_number} from {self.number}...')


class CallingPhoneState(AbstractPhoneState):
    def call(self, phone_number: str):
        print(f'Can`t call {phone_number} during the call from {self.number}...')

    def answer(self):
        print(f'Can`t answer to incoming call to {self.number} during the call...')


class PhoneState:
    phone: AbstractPhoneState

    def call(self, phone_number: str):
        self.phone.call(phone_number)

    def answer(self):
        self.phone.answer()

    def top_up_balance(self):
        self.phone.top_up_balance()