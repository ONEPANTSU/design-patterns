from behavioral_patterns.state.phone_states import *
phone_number = '1234567890'
states = [
    BlockedPhoneState(phone_number),
    WorkingPhoneState(phone_number),
    CallingPhoneState(phone_number),
]

phone_state = PhoneState()

for state in states:
    print(f'Current state: {type(state)}')
    phone_state.phone = state
    phone_state.call(phone_number)
    phone_state.answer()
    phone_state.top_up_balance()
    print()
