
cyberguenza = [4,0,0,2,0,13,4,17,0,5,16,0,6,18,0,7]
s1 >> space (
    cyberguenza, 
    dur=PDur(8,8)*1, 
    pan=(1, -1), 
    oct=3, 
    amp=[.5,.5,.5,.4,.3,0,0,0,0,0,0,0,.6,.8], 
    formant=0)

cyberguenza2 = [0,0,0,2,0,0,4,0,0,5,0,0,6,0,0,7]
s3 >> soprano (
    cyberguenza2, 
    dur=PDur(8,8).reverse(), 
    pan=(1, -1), 
    oct=5, 
    amp=[.5,.5,.5,.4,.3,0,0,0,0,0,0,0,.6,.8], 
    mix=.8, 
    room=.6,
    formant=1, 
    vib=0,
    hpf=0)

s2 >> dirt (
     dur=PDur(3,8),
     pan=(-1,0),
     amp=1.3,
     oct=5,
     formant=0)

p1 >> play (
    " |g0|", 
    dur=PDur(7,8), 
    delay=.5, 
    mix=.3, 
    room=.3, 
    amp=[1.5,1.5,1.5,.4,.3,0,3,0,1.6,0,0,0,1.6,.8])

p2 >> play (
    " |n2|", 
    dur=1/2, 
    amp=3)

p3 >> play (
    " |=3|", 
    dur=1/2, 
    amp=0)

p4 >> play (
    "  |E2|", 
    chop=0 , 
    amp=0, 
    dur=PDur(6,8).reverse(), 
    mix=.1, 
    room=.1)

p7 >> play (" [|e0||e0|] [|e0||e0|] ", 
    amp=[.5,.5,.5,.4,.3,2,0,0,3,0,0,0,.6,.8],
    dur=PDur(7,8))

p5 >> play (
    " |o2|", 
    dur=2/2, 
    amp=.7)

gh >> play (
    "|x4| ",
    amp=1, dur=PDur(4,8))
    
    
    
    #TRACK 2

bh >> play ("  |Z0|", chop=0, amp=0.4, formant=PRand(0,3),dur=PDur(4,8),hpf=var([2000,500])).stutter(5)
hr >> play ("|x4| ", dur=PDur(4,8), amp=1.4)

jo >> play (" |o2|", dur=2/2, amp=.6)

j3 >> play (" [****]", dur=1/2, amp=[.5,0,2,4,0,0,0,0,.1,0,0,.3,0])
yj >> bass (dur=PDur(5,8), amp=1)

lp >> play ("--", sample=PRand(0,3), amp=0)

yh >> play ("[::]", amp=3)

jk >> play (" |n2|", amp=4)


Clock.bpm=128
