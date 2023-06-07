bh >> play ("|m1|           ", dur=8, amp=2)



Scale.default="minor"; Clock.bpm=125
d1 >> play("G(:-)", rate=-1/2, pshift=var([0,3],[6,2])+(0.1,0), pan=(-1,1), room=1, amp=0)

d2 >> play("|x4|-", sample=2, amp=1.3).sometimes("stutter", 4, dur=3)

d3 >> play("  I ", sample=1, hpf=(0,2000), lpf=(300,0), hpr=0.5)

b1 >> dbass(var([0,6,5,2],[6,2]), dur=PDur(3,8,[0,2]), sus=2, chop=2, rate=1, amp=1)

p2 >> pasha([0,1,[[3,4],2]], dur=[4,3,1], amp=0, drive=PWhite(0.2,0.7), oct=linvar([4,5]), lpf=2000, room=1/2, echo=0.75, echotime=6, sus=1).penta().spread()

k1 >> klank(oct=6, lpf=0, lpr=0.5, amp=0)

ji >> play (" |o3|", dur=2/2, amp=0.5)

ju >> play ("[::]", amp=1)



# TRACK 2 


cyberguenza = [4,0,0,2,0,13,4,17,0,5,16,0,6,18,0,7]
s1 >> pluck (
    cyberguenza, 
    dur=PDur(7,8)*1, 
    pan=(1, -1), 
    oct=6.66, 
    amp=[2,.5,.5,.4,.3,1,1,2,1,1,1,1,.6,.8], 
    formant=0)

cyberguenza2 = [0,0,0,2,0,0,4,0,0,5,0,0,6,0,0,7]
s3 >> pluck (
    cyberguenza2, 
    dur=PDur(8,8).reverse(), 
    pan=(1, -1), 
    oct=5, 
    amp=[.5,.5,.5,.4,.3,1,1,1,1,1,1,1,.6,.8], 
    mix=.3, 
    room=.3,
    formant=1, 
    vib=0,
    hpf=0)

s2 >> dirt (
     dur=PDur(8,8),
     pan=(0,0),
     amp=1,
     oct=5,
     formant=0)

p1 >> play (
    " |g0|", 
    dur=PDur(5,8), 
    delay=.5, 
    mix=.3, 
    room=.3, 
    amp=[1.5,1.5,1.5,.4,.3,1,3,1,1.6,0,0,1,1.6,.8])

p2 >> play (
    " |n2|", 
    dur=1/2, 
    amp=2)

p3 >> play (
    " |=3|", 
    dur=1/2, 
    amp=1)

p4 >> play (
    "  |E2|", 
    chop=0 , 
    amp=1, 
    dur=PDur(6,8).reverse(), 
    mix=.1, 
    room=.1)

p7 >> play (" [|e0||e0|] [|e0||e0|] ", 
    amp=[1,2,2,.4,.3,2,2,4,3,4,1,2,.6,.8],
    dur=PDur(7,8))

p5 >> play (
    " |o2|", 
    dur=2/2, 
    amp=.6)

gh >> play ("|x4| ",   amp=0.6, dur=PDur(4,8))
    
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



# chicx Residual 



var.switch = var([1,1],[32])


p8 >> glass(oct=6, rate=linvar([-2,2],16), shape=0.5, amp=0, amplify=var([1,var.switch],64), room=0.5)



b1 >> dirt ([0,0,0.5], dur=PDur(3,8), sus=1, chop=0, drive=0.5, formant=1, oct=(5), room=0.2, amp=1)

p3 >> pasha (var([0,2,0.5],[3,1/2,1/2]), dur=PDur(5,8), amp=1, oct=6, sus=2, pan=PWhite(-1,1)).every(4, "dur.shuffle")

up >> play ("|x4| ", dur=PDur(4,8),amp=1)

c1 >> play("#", rate=-1/2, hpf=1000, dur=4, amp=4, room=1, coarse=16).spread()

c2 >> play (" |o2|", dur=2/2, amp=.5)




# Track 4 

#telefono
b3 >> play("{b[bb] }", amp=[1,1,1,1,0,0,0,00,0,0,0,0,0,0,0,])

t6 >> dirt(dur=PDur(7,8))

sw >> saw(P[var([-2, -3, -1, 0, 1, 2], 16), var([0, 1, 2, 3, 4], 32), var([3, 0], 8), 4, 0.5, 0.75], oct=5, dur=0.25, hpf=P[[800, 500], [200, 250, 300, 350], var([400, 200]), 900, var([350, 800], 8), 400, 500, 300], hpr=expvar([0.25, 1], 1/3), drive=0.15, amp=expvar([0.15, 1], 4) * var([1, .4], [28, 4]))


hr >> play ("|x4| ", amp=1.2, dur=PDur(4,8))

h4 >> play (" |o2|", dur=2/2, amp=.6)

t3 >> play("*-...[----]..*-...[nnnn]..", sample=2, amp=2)


#NR TRACK 


c2 >> play ("|m3| ", dur=8, amp=0)

t2 >> bass (amp=1, dur=PDur(4,8), root=[0,1,0] )
ty >> play ("|x4| ", amp=1.2)
ye >> pluck (dur=PDur(8,8), oct=[6,6,6,6,5,5,7,5,6,5,5,5,5,5,6,6,7], vib=0, amp=.8)
er >> pasha (oct=[4,4,4,4,6], dur=PDur(5,8), vib=2, amp=1 )
hu >> play (" |M0|   ", dur=PDur(5,8), amp=1)
us >> play ("|e1|", dur=PDur(5,8), amp=1)
ko >> play ("[::]", amp=[2,2,2,2,1,1,1,1,1,.3,.4,.6,.7]).stop()
ji >> play (" |o3|", dur=2/2, amp=.5)


#TRACK Ñ


bh >> play ("|m0|           ", dur=8, amp=2)


ll >> dbass (dur=PDur(1,8)*(1,2), echo=.5  ,shape=var([1,0.15],[28,2]), amp=.4, oct=5)
ju >> dirt (dur=PDur(3,8), amp=1, root=var([0,1]))
j5 >>play("F ", sample=4, chop=0,dur=PDur(1,8),amp=0,
     vib=0,vibdepth=0)
g2 >> arpy (amp=linvar([1,.3]), oct=5, dur=PDur(7,8), 
    sus=var([10,50]),
     chop=0, hpf=var([22, 4000]))
j2 >> play ("|x4| ", amp=1)
kk >>  play (" |n2|", amp=0)
jp >> play (" |=1|", amp=0, chop=0, dur=1)
nh >> play (" [::]", amp=3)
nl >> play (" |o2|", dur=2/2, amp=.0, mix=0, room=0)
nm >> play ("tre", dur=PDur(3,8), amp=1.5)




