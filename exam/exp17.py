#Sort dictionary in ascending and descending order.
d={"a":1,"b":2,"c":4,"e":5,"d":3}
d1=sorted(d.items())
print(d1)
d2=sorted(d.items(),reverse=True)
print(d2)