import redis




r = redis.Redis()
test=int(r.get("curl"))
test=test+1;
r.mset({"curl": test})

r.mset({"curl": 2000})
print(test);

