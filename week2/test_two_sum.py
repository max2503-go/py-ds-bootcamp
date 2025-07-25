from day5_twosum import two_sum #imports function writen day before

def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_another_pair():
    assert two_sum ([3, 2, 4], 6) # [1, 2, 3[ 1+5 not present, but 1+2=3 -> [3, 2, 4,]

    #Änderungen müssen gespeichert werden, bevor sie getestet werden können