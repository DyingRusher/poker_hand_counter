#here we are maintaing 2 list first for color and second value-p1
 
def detectHand(hand):
    suits=[]#color
    rank =[]#value
    
    for card in hand:
        # print(card[0],int(card[1:3]))
        suits.append(card[0])
        rank.append(card[1:])
       
    print(suits,rank)
    
    #flush
    
    if suits.count(suits[0])==5:  #counting color
        print("flush")
    return 0

if __name__ == "__main__": #it will only run if this main file is running if any other is calling then it will not run
    detectHand(['C01','C13','C12','C11','C10']) #Royal flush
    detectHand(['C09','C13','C12','C11','C10']) #Straight flush
    detectHand(['C09','S09','D09','H09','C10']) #Four of kind 
    