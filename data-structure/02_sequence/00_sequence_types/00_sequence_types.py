"""
Python Sequence Types

Expeted Result:

<class 'list'>
<class 'str'>
<class 'tuple'>
<class 'bytearray'>
<class 'bytes'>

"""

l   = []
s   = ""
t   = ()
ba  = bytearray(b"")
b   = bytes([])

tl  = type(l)
ts  = type(s)
tt  = type(t)
tba = type(ba)
tb  = type(b)

print(tl)
print(ts)
print(tt)
print(tba)
print(tb)


