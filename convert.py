import os
from grip import render_content

# Compile markdown to html (this could exceed the github api rate limits)
for m in range(2,3):
	month = '0' + str(m) if m < 10 else str(m)
	days = os.listdir('months/' + month + '/')
	for day in days:
		from_path = 'months/' + month + '/' + day
		to_path = 'html/' + month + '-' + day[0:2] + '.html'
		print 'Converting ' + from_path + ' to ' + to_path + '...'

		html_output = render_content(open(from_path).read(), gfm = True)
		open(to_path, 'w').write(html_output.encode('utf-8'))