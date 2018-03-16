def sort_hand(hand):
    """
    sortHand is a function that sorts that hand based on 13's rules
    2 are highest 3 are lowest value wise,
    S<C<D<H suit wise,
    :param hand: list of dict
    :return: list of dict 
    """
    #makes new list for sorted hand
    sortedHand = []
    #get # of cards in hand
    count = len(hand)
    for i in range(count):
        if '3S'in hand['display']:
            hand.remove('3S')
            sortedHand.append('3S')
        elif '3C' in hand:
            hand.remove('3C')
            sortedHand.append('3C')
        elif '3D' in hand:
            hand.remove('3D')
            sortedHand.append('3D')
        elif '3H' in hand:
            hand.remove('3H')
            sortedHand.append('3H')
        elif '4S' in hand:
            hand.remove('4S')
            sortedHand.append('4S')
        elif '4C' in hand:
            hand.remove('4C')
            sortedHand.append('4C')
        elif '4D' in hand:
            hand.remove('4D')
            sortedHand.append('4D')
        elif '4H' in hand:
            hand.remove('4H')
            sortedHand.append('4H')
        elif '5S' in hand:
            hand.remove('5S')
            sortedHand.append('5S')
        elif '5C' in hand:
            hand.remove('5C')
            sortedHand.append('5C')
        elif '5D' in hand:
            hand.remove('5D')
            sortedHand.append('5D')
        elif '5H' in hand:
            hand.remove('5H')
            sortedHand.append('5H')
        elif '6S' in hand:
            hand.remove('6S')
            sortedHand.append('6S')
        elif '6C' in hand:
            hand.remove('6C')
            sortedHand.append('6C')
        elif '6D' in hand:
            hand.remove('6D')
            sortedHand.append('6D')
        elif '6H' in hand:
            hand.remove('6H')
            sortedHand.append('6H')
        elif '7S' in hand:
            hand.remove('7S')
            sortedHand.append('7S')
        elif '7C' in hand:
            hand.remove('7C')
            sortedHand.append('7C')
        elif '7D' in hand:
            hand.remove('7D')
            sortedHand.append('7D')
        elif '7H' in hand:
            hand.remove('7H')
            sortedHand.append('7H')
        elif '8S' in hand:
            hand.remove('8S')
            sortedHand.append('8S')
        elif '8C' in hand:
            hand.remove('8C')
            sortedHand.append('8C')
        elif '8D' in hand:
            hand.remove('8D')
            sortedHand.append('8D')
        elif '8H' in hand:
            hand.remove('8H')
            sortedHand.append('8H')
        elif '9S' in hand:
            hand.remove('9S')
            sortedHand.append('9S')
        elif '9C' in hand:
            hand.remove('9C')
            sortedHand.append('9C')
        elif '9D' in hand:
            hand.remove('9D')
            sortedHand.append('9D')
        elif '9H' in hand:
            hand.remove('9H')
            sortedHand.append('9H')
        elif '10S' in hand:
            hand.remove('10S')
            sortedHand.append('10S')
        elif '10C' in hand:
            hand.remove('10C')
            sortedHand.append('10C')
        elif '10D' in hand:
            hand.remove('10D')
            sortedHand.append('10D')
        elif '10H' in hand:
            hand.remove('10H')
            sortedHand.append('10H')
        elif 'JS' in hand:
            hand.remove('JS')
            sortedHand.append('JS')
        elif 'JC' in hand:
            hand.remove('JC')
            sortedHand.append('JC')
        elif 'JD' in hand:
            hand.remove('JD')
            sortedHand.append('JD')
        elif 'JH' in hand:
            hand.remove('JH')
            sortedHand.append('JH')
        elif 'QS' in hand:
            hand.remove('QS')
            sortedHand.append('QS')
        elif 'QC' in hand:
            hand.remove('QC')
            sortedHand.append('QC')
        elif 'QD' in hand:
            hand.remove('QD')
            sortedHand.append('QD')
        elif 'QH' in hand:
            hand.remove('QH')
            sortedHand.append('QH')
        elif 'KS' in hand:
            hand.remove('KS')
            sortedHand.append('KS')
        elif 'KC' in hand:
            hand.remove('KC')
            sortedHand.append('KC')
        elif 'KD' in hand:
            hand.remove('KD')
            sortedHand.append('KD')
        elif 'KH' in hand:
            hand.remove('KH')
            sortedHand.append('KH')
        elif 'AS' in hand:
            hand.remove('AS')
            sortedHand.append('AS')
        elif 'AC' in hand:
            hand.remove('AC')
            sortedHand.append('AC')
        elif 'AD' in hand:
            hand.remove('AD')
            sortedHand.append('AD')
        elif 'AH' in hand:
            hand.remove('AH')
            sortedHand.append('AH')
        elif '2S' in hand:
            hand.remove('2S')
            sortedHand.append('2S')
        elif '2C' in hand:
            hand.remove('2C')
            sortedHand.append('2C')
        elif '2D' in hand:
            hand.remove('2D')
            sortedHand.append('2D')
        elif '2H' in hand:
            hand.remove('2H')
            sortedHand.append('2H')
        else:
            print "Sorting Error"
    return sortedHand
