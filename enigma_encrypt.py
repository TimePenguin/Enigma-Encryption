# Sorry for the bad variable naming and no commenting, this was done a year ago and one of my first big python projects
# Before running this program, one must make a enigma_encrypt.in file to input text to encrypt, as well as an enigma_encrypt.out file 
# where the encrypting text will be displayed
def open_files():
    counter = open("counter_encrypt.py", "a" )
    counter.write("0")
    lists = open("lists_encrypt.py", "w" )
    for i in range (3):
        lists.write("abcdefghijklmnopqrstuvwxyz\n")
        i = i
    lists.close()
    counter.close()
try:
    open("counter_encrypt.py", "r")
except:
    open_files()
aa_read = open("lists_encrypt.py")
file_to_write = open("enigma_encrypt.out", "a")
aaa = list(aa_read.readline())
bbb = list(aa_read.readline())
ccc = list(aa_read.readline())
aaa.pop(26)
bbb.pop(26)
aa = {'n' : 'e', 'e' : 'n', 'j' : 'h', 'h' : 'j', 't' : 'k', 'k' : 't', 'i' : 'q', 'q' : 'i', 'x' : 'w', 'w' : 'x', 'b' : 'y', 'y' : 'b', 'f' : 'v', 'v' : 'f', 'o' : 'u', 'u' : 'o', 's' : 'g', 'g' : 's', 'l' : 'd', 'd' : 'l', 'r' : 'm', 'm' : 'r', 'a' : 'z', 'z' : 'a', 'c' : 'p', 'p' : 'c', }
bb = {'a' : 'u', 'u' : 'a', 'n' : 'w', 'w' : 'n', 't' : 'x', 'x' : 't', 'l' : 'f', 'f' : 'l', 'p' : 's', 's' : 'p', 'o' : 'z', 'z' : 'o', 'k' : 'm', 'm' : 'k', 'j' : 'g', 'g' : 'j', 'e' : 'i', 'i' : 'e', 'y' : 'h', 'h' : 'y', 'v' : 'b', 'b' : 'v', 'q' : 'r', 'r' : 'q', 'd' : 'c', 'c' : 'd', }
cc = {'r' : 's', 's' : 'r', 'w' : 'n', 'n' : 'w', 'b' : 'x', 'x' : 'b', 'c' : 'k', 'k' : 'c', 'q' : 'y', 'y' : 'q', 'l' : 'g', 'g' : 'l', 'v' : 'p', 'p' : 'v', 'z' : 'a', 'a' : 'z', 'u' : 'f', 'f' : 'u', 'h' : 'o', 'o' : 'h', 't' : 'e', 'e' : 't', 'j' : 'm', 'm' : 'j', 'i' : 'd', 'd' : 'i', }
dd = {'r' : 'd', 'd' : 'r', 'a' : 'b', 'b' : 'a', 'g' : 'k', 'k' : 'g', 'p' : 'y', 'y' : 'p', 'h' : 'l', 'l' : 'h', 'e' : 'w', 'w' : 'e', 'm' : 'n', 'n' : 'm', 'q' : 'c', 'c' : 'q', 'f' : 'i', 'i' : 'f', 'o' : 'x', 'x' : 'o', 'u' : 'v', 'v' : 'u', 's' : 't', 't' : 's', 'z' : 'j', 'j' : 'z', }
ee = {'y' : 'w', 'w' : 'y', 'm' : 'b', 'b' : 'm', 'e' : 'u', 'u' : 'e', 'g' : 'l', 'l' : 'g', 'p' : 'q', 'q' : 'p', 'd' : 'a', 'a' : 'd', 'x' : 'r', 'r' : 'x', 'j' : 's', 's' : 'j', 'i' : 'k', 'k' : 'i', 'c' : 't', 't' : 'c', 'n' : 'v', 'v' : 'n', 'z' : 'h', 'h' : 'z', 'f' : 'o', 'o' : 'f', }
zz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = open("enigma_encrypt.in", "r").readline().replace(" ", "").lower()
counter_read = open("counter_encrypt.py", "r")
a = (counter_read.readlines()[0]) 
a = int(a)
def switch(hello, dkj):
    global x
    x = ""
    gg = []
    for thing in hello:
        gg.append(dkj[thing])
    for i in range (len(gg)):
        x = x + gg[i]
switch(text, aa)
lis = []
lis.extend(text)
final_string = ""
for i in lis:
    a = a + 1
    x = i
    switch(x, aa)
    x = zz.index(x)
    x = aaa[x]
    switch(x, bb)
    x = aaa.index(x)
    x = bbb[x]
    switch(x, cc)
    x = bbb.index(x)
    x = ccc[x]
    switch(x, dd)
    x = ccc.index(x)
    x = zz[x]
    switch(x, ee)
    x = zz.index(x)
    x = ccc[x]
    switch(x, dd)
    x = ccc.index(x)
    x = bbb[x]
    switch(x, cc)
    x = bbb.index(x)    
    x = aaa[x]
    switch(x, bb)
    x = aaa.index(x)
    x = zz[x]
    switch(x, aa)
    final_string += x
    aaa.append(aaa[0])
    aaa.pop(0)
    if a % 26 == 0:
        bbb.append(bbb[0])
        bbb.pop(0)
    if a % 676 == 0:
        ccc.append(ccc[0])
        ccc.pop(0)
counter_writ = open("counter_encrypt.py", "w")
counter_writ.write(str(a))
lists_write = open("lists_encrypt.py", "w")
f = ""
d = ""
v = ""
for i in aaa:
    f = f + i
for i in bbb:
    d = d + i
for i in ccc:
    v = v + i    
lists_write.write(f + "\n" + d + "\n" + v)
open("enigma_encrypt.out", "w").write(final_string)
counter_writ.close()
lists_write.close()
file_to_write.close()