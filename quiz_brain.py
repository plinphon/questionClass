class Brain:

    def __init__(self,lis):
        self.question = lis[0]
        self.answer = lis[1]


    def check(self,num):
        self.Input = input('Q'+str(num)+' '+self.question + ' (true or false?): ')
        print(self.answer)
        if str(self.Input).lower() == str(self.answer).lower():
            return True
        else:
            return False


 
