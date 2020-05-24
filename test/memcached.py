import memcache

mc = memcache.Client(["127.0.0.1:11211"],debug=True)

# mc.set("username","tlj",time=5)
value = mc.get("username")
print(value)