import os
from grip import export

# Compile markdown to html (this could exceed the github api rate limits)
for m in range(1,12):
	month = '0' + str(m) if m < 10 else str(m)
	days = os.listdir('months/' + month + '/')
	for day in days:
		from_path = 'months/' + month + '/' + day
		to_path = 'html/' + month + '-' + day[0:2] + '.html'
		print 'Converting ' + from_path + ' to ' + to_path + '...'

		export(	path=from_path
				,gfm=True
				,out_filename=to_path
		)