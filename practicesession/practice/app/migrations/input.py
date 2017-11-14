import re
e = 'Abc1.@example.com'
if re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', e):
	print 'Successful match'
else:    
	print 'Match attempt failed'
	    
