import google

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query="facebook"

for j in search(query,tld="com", num=10, stop=1, pause=2):
      print (j)