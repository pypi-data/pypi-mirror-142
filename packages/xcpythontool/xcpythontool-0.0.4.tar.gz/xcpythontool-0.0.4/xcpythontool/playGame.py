import random
class PlayGame:

    def __init__(self, begin = True):
        if begin:
            self.money_play()
    #摇骰子猜大小
    def get_big_or_small(self,resultNum):
        if 11 < resultNum < 18:
            return '大'
        else:
            return '小'

    def get_answer(self,guess,arr):
        result = self.get_big_or_small(sum(arr))
        print(result,guess)
        win = False
        if guess == result:
            win = True
        return [win,arr,sum(arr),result]

    def play_dice(self,guess,num = 3):
        numArr = []
        while num > 0:
             numArr.append(random.randrange(1,7))
             num = num - 1
        else:
            return self.get_answer(guess,numArr)
    def money_play(self,money = 1000):

        while money > 0:
            guess = input('您当前的金额为1000元，输完为止，输入大或小:')
            result = self.play_dice(guess)
            if result[0] == True:
                money = money + 500
                print('骰子的结果是：',result[1],',',result[2],'点',result[3],'，您猜对了，当前金额为：',money)
            else:
                money = money - 500
                print('骰子的结果是：', result[1], ',', result[2], '点', result[3], '，您猜错了，当前金额为：', money)
        else:
            print('GAME OVER,您已经没有本金可以玩耍了！')

