#here we are maintaing 2 list first for color and second value-p1
 
def detectHand(hand):
    suits=[]#color
    rank =[]#value
    
    for card in hand:
        # print(card[0],int(card[1:3]))
        suits.append(card[0])
        rank.append(int(card[1:]))
       
    rank = sorted(rank)
    print(suits,rank)
    hand = 1
    #flush
    
    unique_cards = list(set(rank))
    if suits.count(suits[0])==5:  #counting color
        if 1==rank[0] and 10==rank[1] and 11==rank[2] and 12==rank[3] and 13==rank[4]:#Royal flush
            hand = 10
        elif rank[0]==rank[1]-1 and rank[0]==rank[1]-1 and rank[1]==rank[2]-1 and rank[2]==rank[3]-1:#Stright flush
        # elif all(rank[i] == rank[i+1]-1 for i in range(0,3)):  #Stright flush method 2
            hand = max(hand,9)
        else:
            hand = max(hand,6) #flush
            
    #count freq
    
    elif len(unique_cards)==2:
        for val in rank:
            if rank.count(val)==4:
                hand = max(hand,8)#four of kind
            if rank.count(val)==3:
                hand = max(hand,7)#Full house
    
    elif len(unique_cards)==3:
        for val in rank:
            if rank.count(val)==3:
                hand = max(hand,4)#three of kind
            if rank.count(val)==2:
                hand = max(hand,3)#two pair

    elif rank[0]==rank[1]-1 and rank[0]==rank[1]-1 and rank[1]==rank[2]-1 and rank[2]==rank[3]-1:#flush
        hand=max(hand,5)
    elif len(unique_cards)==4:
        hand=max(hand,2)
    # print(unique_cards)
    
    map_hand = {10:"Royal flush",9:"Stright Flush",8:"Four of kind",7:"Full house",6:"Flush",5:"Stright",4:"Three of kind",3:"Two pair",2:"Pair",1:"High card",0:"Testing"}
    print("rank",map_hand[hand])
    return 0

if __name__ == "__main__": #it will only run if this main file is running if any other is calling then it will not run
    detectHand(['C01','C13','C12','C11','C10']) #Royal flush
    detectHand(['C09','C13','C12','C11','C10']) #Straight flush
    detectHand(['C09','S09','D09','H09','C10']) #Four of kind 
    detectHand(['C09','S09','D09','H10','C10']) #Full house 
    detectHand(['C09','S10','D11','H12','C13']) #flush 
    detectHand(['S09','D10','C11','H12','H07']) #straight 
    detectHand(['S09','D09','H09','H12','H06']) #Three of kind
    detectHand(['S10','D09','H09','H06','H06']) #two pair
    detectHand(['S10','D09','H05','H06','H06']) #pair
    detectHand(['S10','D09','H05','H06','H01']) #high card
     
    