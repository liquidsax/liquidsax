                                             #在chatgpt的帮衬下完成一个发牌游戏！
"""1.创建一个列表，包含52张牌，每张牌用一个字符串表示，例如："A♠"表示黑桃A，"K♥"表示红心K。"""
import random
class Card:
    def __init__(self,suit,value) :
        self.suit = suit  #花色
        self.value = value   #大小

    def __repr__(self):
        return f"{self.value}{self.suit}" #repr是一个帮助我们输出字符串的方法
    
class Deck:
    def __init__(self):
        self.cards = [Card(suit,value) for suit in ['♠', '♣', '♡', '♢']for value in ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']]  #用于创建一个循环
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()         #pop用于删除取出的卡
    
class Player:                           #定义玩家
    def __init__(self,name):
        self.name = name 
        self.cards = []
        self.score = 0

    def get_score(self):
        self.score = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.score += int(card.value)
            elif card.value in ['J','Q','k']:
                self.score += 10
            else:
                has_ace = True
                self.score += 11
        if has_ace and self.score>21:
            self.score -= 10            #如果你在循环中有多张A，则每个A都会被计为11分，直到点数超过21或者没有A可用。如果点数超过21，则所有的A都被计为1分，直到点数小于或等于21。

        def hit(self,card):
            self.cards.append(card)     #这是一个方法，用于将参数card添加到实例变量self.cards所表示的列表中，相当于将一张牌加入到庄家或玩家的手牌中。
            self.get_score()

        def show_hand(self):
            print(f"{self.name}'s hand:")
            for card in self.cards:
                print(card)

class Dealer(Player):                   #庄家可以继承来自玩家的规则
    def __init__(self):
        super().__init__('Dealer')      #通过super()关键字来调用父类的方法和属性。
        self.deck =Deck()
        self.deck.shuffle()

    def deal_initial_cards(self,player):
        player.hit(self.deck.deal())
        self.hit(self.deck.deal())
        player.hit(self.deck.deal())
        self.hit(self.deck.deal())

    def play(self):
        while self.score <17:
            self.hit(self.deck.deal())
        if self.score >21:
            print("Dealer busts")
        else:
            print("Dealer stands")
"""
    到目前为止，我们完成了
    第一部分

    遗憾的是，在2023年4月4日chatgpt结束了在亚洲的服务
    所以这一部分我暂时无法完成
    ————2023.3.4
"""
        