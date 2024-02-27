#here we are maintaing 2 list first for color and second value-p1
 
def detectHand(hand):
    suits=[]#color
    rank =[]#value
    
    for card in hand:
        # print(card[0],int(card[1:3]))
        suits.append(card[-1])
        if len(card) == 3:
            rank.append(10)
        else:
            if card[0]=='A':
                rank.append(14)
            elif card[0]=='K':
                rank.append(13)
            elif card[0]=='Q':
                rank.append(12)
            elif card[0]=='J':
                rank.append(11)
            else:
                rank.append(int(card[0]))
            # rank.append(card[0])
        # rank.append(int(card[1:]))
        
    # print(suits,rank,hand)
    
    rank = sorted(rank)
    print(suits,rank)
    hand = 1
    #flush
    
    unique_cards = list(set(rank))
    if suits.count(suits[0])==5:  #counting color
        if 10==rank[0] and 11==rank[1] and 12==rank[2] and 13==rank[3] and 14==rank[4]:#Royal flush
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
    detectHand(['AC','KC','QC','JC','10C']) #Royal flush
    detectHand(['9C','KC','QC','JC','10C']) #Straight flush
  
    detectHand(['9C','9S','9D','9H','10C']) #Four of kind 
    detectHand(['9C','9S','9D','10H','10C']) #Full house 
    detectHand(['9C','10S','JS','QH','KC']) #flush 
    detectHand(['9S','10D','JC','QH','8H']) #straight 
    detectHand(['9S','9D','9H','QH','6H']) #Three of kind
    detectHand(['10S','9D','9H','6H','6H']) #two pair
    #dsfgadfgsdfgsdfgxhgzdryh
    detectHand(['10S','9D','5H','6H','5H']) #pair
    detectHand(['2S','9D','5H','6H','10H']) #high card