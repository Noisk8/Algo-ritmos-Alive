s1 >> pasha ([0,0,8,5,4,8,9].reverse(), dur=PDur(8,8)*1, pan=(1, -1), oct=5)

s2 >> dirt (dur=PDur(5,8).reverse(), pan(-1,0), amp=0.6, oct=5, formant=0)

p1 >> play (" |g0|", dur=8/2, delay=.5, mix=.3, room=.3, amp=1)

p2 >> play (" |n2|", dur=1/2, amp=2)

p3 >> play (" |=3|", dur=2/2, amp=1)

p4 >> play ("  |E2|", chop=0 , amp=.6, dur=2/2)

