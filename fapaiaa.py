"""this is my second time to do this """
class Card():
     RANKS =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
     SUITS =["梅","方","红","黑"]
     def __init__(self,rank,suit,face_up =True):
         self.rank =rank
         self.suit = suit
         self.is_face_up =face_up
     def __str__(self):
         if self.is_face_up:
              rep = self.suit +self.rank
         else:
              rep="XX" 
         return rep
     def pic_order(self):
         if self.rank=="A":
              FaceNum=1
         if self.rank=="J":
              FaceNum=11
         if self.rank=="Q":
              FaceNum=12
         if self.rank=="K":
              FaceNum=13
         else:
              FaceNum=int(self.rank)
         if self.suit=="梅":
              Suit=1
         if self.suit=="方":
              Suit=2
         if self.suit=="红":
              Suit=3
         if self.suit=="黑":
              Suit=4
         return (Suit-1)*13_+FaceNum
     def flip(self):
          self.is_face_up=not self.is_face_up
class Hand():
      def __init__(self):
           self.cards=[]
      def __str__(self):
           if self.cards:
                rep = ""
                for card in self.cards:
                 rep +=str(card) + "\t"
           else:
                rep="无牌"
           return rep
      def clear(self):
           self.cards =[]
      def add(self,card):
           self.cards.append(card)
      def give(self,card,other_hand):
           self.cards.remove(card)
           other_hand.add(card)
class Poke():
      def populate(self):
           for suit in Card.SUITS:
                for rank in Card.RANKS:
                     self.add(Card(rank,suit))
      def shuffle(self):
           import random
           random.shuffle(self.cards)
      def deal(self,hands,per_hand =13):
           for rounds in range(per_hand):
                for hand in hands:
                     if self.cards:
                          top_card=self.cards[0]
                          self.cards.remove(top_card)
                          hand.add(top_card)
                     else:
                          print("不能继续啊，没牌了@发牌员")       
#主程序
if __name__ =="__main__":
     print("this is a module with classes for playing cards.")
     players =[Hand(),Hand(),Hand(),Hand()]
     poke1 = Poke()
     poke1.populate()
     poke1.shuffle()
     poke1.deal(players,13)
     n=1
     for hand in players:
          print("牌手",n,end=":")
          print(hand)
          n=n+1
input("\nPress the key to exit.")
    