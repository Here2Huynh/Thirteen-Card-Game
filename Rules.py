#Rules

rules = """
Thirteen is a Vietnamese Poker card game.
The game have 4 players.
Using a standard 52 card deck.
Deal each player 13 card.

----------HOW TO WIN-----------
Be the first to get rid of the cards in your hand first.

----------AWARDS----------
First place gets $2.
Second place gets $1.
Third place pays second place winner $1.
Fourth place pays first place $2.

******Shortcut Key******
Spades      = S
Clovers     = C
Diamonds    = D
Hearts      = H

Jack        = J
Queen       = Q
King        = K
Ace         = A

******Card View******
3H (3 of Hearts)
JC (Jack of Clovers)
QD (Queen of Diamonds)
KS (King of Spades)
AD (Ace of Diamonds)
2C (2 of Clovers)

******Suit Order******
Spades(S) < Clovers(C) < Diamonds(D) < Hearts(H)

******Number Order******
Lowest -> Highest
3,4,5,6,7,8,9,10,Jack(J),Queen(Q),King(K),Ace(A),2
3S being the lowest in game.
2H being the highest in game.

----------Game Play----------
*In the very first round, the player with the
three of spades(3S) goes first.
*Any continuing rounds after that the winner will go first.
*In the event where the winner won because of instant win condition,
then in the next round the player with the three of spades(3S) goes first.
*The turn rotation is counter clockwise.
*Player that start the round first can play any type of move and
the players following the move has to match the type of move and
beat the move in card value or suite.
*Once every other player has pass on that move. The player that played
the winning move can clear the table and start a new round playing any
move they want again.

Example:
Player 1 plays [3S].
Player 2 plays [4S].
Player 3 plays [5H].
Player 4 plays [6D].
Player 1 plays [2S].
Player 2 plays [passes].
Player 3 plays [passes].
Player 4 plays [passes].
Player 1 plays [4D].
...


******Special Rules******
If you don’t have any playable combinations, you have to pass.
You can choose to pass for strategic reasons.
But by passing, you will be locked out of play until someone wins the round.

Example:
Player 1 plays [3S].
Player 2 plays [4S].
Player 3 plays [5H].
Player 4 plays [6D].
---
Player 1 plays [2S].
Player 2 [passes]. -> are locked out
Player 3 [passes]. -> are locked out
Player 4 plays [2C].
---
Player 1 plays [2D].
Player 2 is [locked out].
Player 3 is [locked out].
Player 4 plays [2H].
---
Player 1 [passes].
Player 2 is [locked out].
Player 3 is [locked out].
Player 4 wins round.
---
Player 4 plays [4D].
...


******Move Types******

[Singles]
[3S] or [4D] or [KC] or [AH]

[Doubles]
(has to be matching number and the value is decided on the highest suit)
[3S,3H] or [AC,AD] or [2H,2D]
[5S,5H] > [5D,5C] or [9C,9S] < [9H,9D]

[Triples]
[4S,4D,4H] or [8D,8C,8D]
[4S,4D,4H] < [8D,8C,8D]

[Straights]
(minimum of three cards plus and 2's are not allowed to in straights,
the value of the straight is decided on the highest number and suit,
the straights has to match in terms of length)

Valid:
[3H,4S,5C] or [8C,9C,10S,JH,QD,KS] or [JC,QH,KH,AD]

Not Valid:
[2C,3S,4C] vs [QD,KH,AS,2H]
(2 is not allowed to be in a straight)
(three cards straight vs a four card straight)

[3H,4S,5C] < [8C,9C,10S]
(highest card in straight 5C and 10S in which 5c < 10S)
[8C,9C,10S] < [8C,9H,10D]
(highest card in straight 10S and 10D in which 10s < 10D)
[JC,QH,KH,AD] > [5H,6D,7S,8H]
(highest card in straight AD and 8H in which AD > 8H)


[Bombs]
Bombs are used to beat 2's.
A single 2 or a pair of 2's can be beaten.
Triple 2's can not be beaten.

(4 of a kind)
Example:
(3 or 4 consecutive doubles)
The only thing that can beat this is a higher combination of the same
type and number of cards.


******Instant Win Conditions******
*Instant win conditions are conditions where if the player has that
combination in hand they will instantly win.
*Winner gets $2 from everyone
*Next round player with 3S starts

[All four 2's in hand]
Have [2S, 2C, 2D, 2H] in your hand
The other 9 cards does not matter.

[Dragon]
Have a 12 card straight from 3 to A [3S,4D,5C,6H,7H,8S,9D,10D,JS,QC,KC,AC]
The 13th card does not matter what it is.
Suits does not matter.
Example hand: [3H,4D,5C,6C,7S,8H,9H,10S,JC,QD,KC,AD,2D]

[6 Pairs]
Have 6 pairs of doubles (12 cards)
The 13th card does not matter what it is.
Suits does not matter.
Order does not matter.
Example hand: [3S,3C,5H,5D,6C,6H,KD,KS,JC,JS,10D,10H,9C]
"""
