def  filter_tweets(emps, a):
	filtered = []
	for em in emps:
		for ch in em['children']:
		    if ch['age'] >= a:
		    	filtered.append(em['name'])
		    	break
	return filtered

 
ivan = {
   "name" : "ivan",
   "age" : 34,
   "children" : [{
       "name" : "vasja" ,
       "age" : 12,
   }, {
       "name" : "petja" ,
       "age" : 10,
   }],
   }
darja = {
   "name" : "darja" ,
   "age" : 41,
   "children" : [{
       "name" : "kirill" ,
       "age" : 21,
   }, {
       "name" : "pavel" ,
       "age" : 15,
   }],
}
    
emps = [ivan, darja]

   # call our function
print(filter_tweets(emps, 18))
