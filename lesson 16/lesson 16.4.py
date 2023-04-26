class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        file = open('logs.txt', 'a+')
        file.write(self.msg + '\n')
        file.close()

raise CustomException('Erorr')
