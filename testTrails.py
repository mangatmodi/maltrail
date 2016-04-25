from core.settings import trails
import sys
from core.common import load_trails

trails.update(load_trails())
'''
trails contains blacklisted strings: domains and Ips
e.g.
mqbbsagabardinedazyx.com
dgj4gu1xmithip.net
moegestnessbiophysicalohax.com
rhmxancorml.com
115.28.7.221
jjcwgfwdyqje.pw
'''
for line in sys.stdin:
	try:
	  line = line.strip()
	  data = line.split(',')
	  if data[5] in trails or data[9] in trails:
		print str(data[6])+","+str(100)
	  else:
	        print str(data[6])+","+str(0)
	except:
	  print line
