 def range(start,end=None,diff=None):
     if end==None and diff==None:
         end=start
         start=0
         diff=1
     elif diff==None:
         diff=1
     if start>=end:
         return []
     a=range(start+diff,end,diff)
     a.insert(0,start)
     return a
 print(range(5,10))


        




