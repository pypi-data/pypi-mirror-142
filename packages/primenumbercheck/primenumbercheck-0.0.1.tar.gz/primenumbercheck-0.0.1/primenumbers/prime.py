class Prime:
    def __init__(self, number) -> None:
        self.number = number

    def check(number):
        product = 1      
        list = []
        for num in range(number):
            list.append(num)

        list = [x for x in list if x != 0]

        for x in list:
            product *= x

        final = product + 1


        if final % number == 0: 
            return True
        else:
            return False



