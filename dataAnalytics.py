import pandas as p
import xlrd

df1 = p.read_excel("icup.xlsx", sheet_name="sales")
df2 = p.read_excel("icup.xlsx", sheet_name="ticket types")
df3 = p.read_excel("icup.xlsx", sheet_name="theaters")
df4 = p.read_excel("icup.xlsx", sheet_name="movies")

#problem statement 1
print('PROBLEM STATEMENT 1')
print('The required merged data is:')
df0=p.merge(df1,df2)
df0=p.merge(df0,df3)
df0=p.merge(df0,df4)

print(df0)


# problem statement 2
print('PROBLEM STATEMENT 2')
a=[]
'''for i in df1.movie_title:
    if i=='The Seaborn Identity':
        a.append(True)
    else:
        a.append(False)
b=p.Series(a)'''
x=df0[df0['movie_title']=='The Seaborn Identity']
print(x.head())
#seaborn=df1[b]
merge1=p.merge(seaborn,df2,on="ticket_type")
merge1.drop("movie_title", axis=1, inplace=True)
gk=merge1.groupby('theater_name')

#frame
theframe=gk.get_group('The Frame')
aaa1=list(theframe['ticket_quantity'])
bbb1=list(theframe['ticket_price'])
ccc1=[]
for i in range(len(aaa1)):
    ccc1.append(aaa1[i]*bbb1[i])
eee1=sum(ccc1)

#riche
riche=gk.get_group("Richie's Famous Minimax Theatre")
aaa2=list(riche['ticket_quantity'])
bbb2=list(riche['ticket_price'])
ccc2=[]
for i in range(len(aaa2)):
    ccc2.append(aaa2[i]*bbb2[i])
eee2=sum(ccc2)

#sumdance
sumdance=gk.get_group("Sumdance Cinemas")
aaa3=list(theframe['ticket_quantity'])
bbb3=list(theframe['ticket_price'])
ccc3=[]
for i in range(len(aaa3)):
    ccc3.append(aaa3[i]*bbb3[i])
eee3=sum(ccc3)

#emper
emper=gk.get_group("The Empirical House")
aaa4=list(theframe['ticket_quantity'])
bbb4=list(theframe['ticket_price'])
ccc4=[]
for i in range(len(aaa1)):
    ccc4.append(aaa4[i]*bbb4[i])
eee4=sum(ccc4)

f=[eee1,eee2,eee3,eee4]
g=list(set(f))
g.remove(max(g))
k=max(g)

if k==eee1:
    z='The Frame'
elif k==eee2:
    z="Richie's Famous Minimax Theatre"
elif k==eee3:
    z='Sumdance Cinemas'
elif k==eee4:
    z='The Empirical House'
print("The theatre thatmade the second-highest sales for the movie ‘The Seaborn Identity’ is", z)

#problem3
print('PROBLEM STATEMENT 3')
a0=[]
for i in df1.ticket_type:
    if i=='senior':
        a0.append(True)
    else:
        a0.append(False)
b0=p.Series(a0)
senior0=df1[b0]
#senior0.drop("ticket_type", axis=1, inplace=True)
gk0=senior0.groupby('theater_name')

#frame
theframe0=gk0.get_group('The Frame')
sum01=sum(theframe0['ticket_quantity'])

#riche
riche0=gk0.get_group("Richie's Famous Minimax Theatre")
sum02=sum(riche0['ticket_quantity'])

#sumdance
sumdance0=gk0.get_group('Sumdance Cinemas')
sum03=sum(sumdance0['ticket_quantity'])

#emper
emper0=gk0.get_group('The Empirical House')
sum04=sum(emper0['ticket_quantity'])

z0=list(set([sum01,sum02,sum03,sum04]))
z0.remove(max(z0))
z0.remove(max(z0))
max0=max(z0)

if max0==sum01:
    y='The Frame'
elif max0==sum02:
    y="Richie's Famous Minimax Theatre"
elif max0==sum03:
    y='Sumdance Cinemas'
elif max0==sum04:
    y='The Empirical House'
m0=list(df3['theater_name'])
n0=list(df3['theater_location'])
in0=m0.index(y)
print("The city of the theatre that made the third-highest sales only with ‘senior’ is", n0[in0])



#problem4
print('PROBLEM STATEMENT 4')
df1.drop("theater_name", axis=1, inplace=True)
df1=p.merge(df1,df2,on="ticket_type")

#m2
move=df1.groupby('movie_title')
m2=move.get_group('The Sumif All Fears')
aaa42=list(m2['ticket_quantity'])
bbb42=list(m2['ticket_price'])
ccc42=[]
for i in range(len(aaa42)):
    ccc42.append(aaa42[i]*bbb42[i])
eee42=sum(ccc42)

#m3
move=df1.groupby('movie_title')
m3=move.get_group('The Seaborn Identity')
aaa43=list(m3['ticket_quantity'])
bbb43=list(m3['ticket_price'])
ccc43=[]
for i in range(len(aaa43)):
    ccc43.append(aaa43[i]*bbb43[i])
eee43=sum(ccc43)

#m4
move=df1.groupby('movie_title')
m4=move.get_group('The Matrices')
aaa44=list(m4['ticket_quantity'])
bbb44=list(m4['ticket_price'])
ccc44=[]
for i in range(len(aaa44)):
    ccc44.append(aaa44[i]*bbb44[i])
eee44=sum(ccc44)

#m5
move=df1.groupby('movie_title')
m5=move.get_group("There's Something About Merging")
aaa45=list(m5['ticket_quantity'])
bbb45=list(m5['ticket_price'])
ccc45=[]
for i in range(len(aaa45)):
    ccc45.append(aaa45[i]*bbb45[i])
eee45=sum(ccc45)

#m6
move=df1.groupby('movie_title')
m6=move.get_group('Mamma Median!')
aaa46=list(m6['ticket_quantity'])
bbb46=list(m6['ticket_price'])
ccc46=[]
for i in range(len(aaa46)):
    ccc46.append(aaa46[i]*bbb46[i])
eee46=sum(ccc46)

#m7
move=df1.groupby('movie_title')
m7=move.get_group('Harry Plotter')
aaa47=list(m7['ticket_quantity'])
bbb47=list(m7['ticket_price'])
ccc47=[]
for i in range(len(aaa47)):
    ccc47.append(aaa47[i]*bbb47[i])
eee47=sum(ccc47)

#m8
move=df1.groupby('movie_title')
m8=move.get_group('Kung Fu pandas')
aaa48=list(m8['ticket_quantity'])
bbb48=list(m8['ticket_price'])
ccc48=[]
for i in range(len(aaa48)):
    ccc48.append(aaa48[i]*bbb48[i])
eee48=sum(ccc48)

#m9
move=df1.groupby('movie_title')
m9=move.get_group('While You Were Sorting')
aaa49=list(m9['ticket_quantity'])
bbb49=list(m9['ticket_price'])
ccc49=[]
for i in range(len(aaa49)):
    ccc49.append(aaa49[i]*bbb49[i])
eee49=sum(ccc49)

#m10
move=df1.groupby('movie_title')
m10=move.get_group('10 Things I Hate About Unix')
aaa410=list(m10['ticket_quantity'])
bbb410=list(m10['ticket_price'])
ccc410=[]
for i in range(len(aaa410)):
    ccc410.append(aaa410[i]*bbb410[i])
eee410=sum(ccc410)

list4=list({eee42, eee43, eee44, eee45, eee46, eee47, eee48, eee49, eee410})
max4=max(list4)
list4.remove(max4)
max4=max(list4)
list4.remove(max4)
max4f=max(list4)
z4=max4f

mov4=[]
if z4==eee42:
    k2='The Sumif All Fears'
    mov4.append(k2)
if z4==eee43:
    k3='The Seaborn Identity'
    mov4.append(k3)
if z4==eee44:
    k4='The Matrices'
    mov4.append(k4)
if z4==eee45:
    k5="There's Something About Merging"
    mov4.append(k5)
if z4==eee46:
    k6='Mamma Median!'
    mov4.append(k6)
if z4==eee47:
    k7='Harry Plotter'
    mov4.append(k7)
if z4==eee48:
    k8='Kung Fu pandas'
    mov4.append(k8)
if z4==eee49:
    k9='While You Were Sorting'
    mov4.append(k9)
if z4==eee410:
    k10='10 Things I Hate About Unix'
    mov4.append(k10)

zxc=list(df4['movie_title'])
zxv=list(df4['movie_length'])
be=[]
for i in mov4:
    vin=zxc.index(i)
    be.append(zxv[vin])
ab=max(be)
bein=be.index(ab)
final=mov4[bein]
print('The longest movie that made third-maximum sales is', final)

#print(m3)
