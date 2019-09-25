## Stupid School Teacher
# Create a program to have a conversation with your teacher. This is how he reacts to your responses
# if you responde to your school teacher:
# Go back to school!
# if you ask a questions
# HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!
# if your respond with something ending with !
# YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!
# if your response is 'I'm a doctor'
# WELLL DONE! YOU can now talk to me
# Exits


user_response = input('Hi there! I hope you are well :)')
profession = input('Enter your profession:')
counter = 0
while profession == 'doctor'.lower().strip():
    print('Well done! You can now talk to me')
    user_response = input('What is on your mind?')
    counter += 1
    if user_response.endswith('?'):
        print('HAHAHA! AHAHAHAHAHA! OMG What a silly question! Go back to school!')
    elif user_response.endswith('!'):
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')
    else:
        print('Go back to school!')
        break
else:
    print('Go back to school!')
    counter += 1




