import re
class Email_chek:
    def __init__(self,email):
        Email_chek.validate(email)

    @classmethod
    def validate(cls,email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        else:
            print('Valid email address')



email_test = Email_chek('example@mail.com')