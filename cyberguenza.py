cyberguenza = [4,0,0,2,0,13,4,17,0,5,16,0,6,18,0,7]
s1 >> space (cyberguenza, dur=PDur(8,8)*1, pan=(1, -1), oct=5, amp=1.8, formant=0)

cyberguenza2 = [0,0,0,2,0,0,4,0,0,5,0,0,6,0,0,7]
s3 >> soprano (cyberguenza2, 
    dur=PDur(8,8).reverse(), 
    pan=(1, -1), 
    oct=5, 
    amp=.8, 
    mix=.8, 
    room=.6,
    formant=1, 
    vib=0,
    hpf=0)

s2 >> dirt (dur=PDur(3,8), pan=(-1,0), amp=1, oct=5, formant=0)

p1 >> play (" |g0|", dur=PDur(7,8), delay=.5, mix=.3, room=.3, amp=3)

p2 >> play (" |n2|", dur=1/2, amp=2)

p3 >> play (" |=3|", dur=2/2, amp=1)

p4 >> play ("  |E2|", chop=2 , amp=3, dur=PDur(6,8).reverse(), mix=.6, room=.6)

p7 >> play (" [|e0||e0|] [|e0||e0|] ", amp=5,dur=PDur(7,8))

p5 >> play (" |o2|", dur=2/2, amp=1)

gh >> play ("|x4| ",amp=1.2)
