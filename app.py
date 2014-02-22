import os

from datetime import datetime, timedelta
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults = {'month': 0, 'day': 0})
@app.route('/<int:month>/<int:day>')
def showdate(month, day):
        if(month == 0 and day == 0):
            if datetime.now().year < 2014:
                return 'It is not 2014, yet. Bookmark this and return on the first of January'
            show = datetime.now()
        else:
            show = datetime(datetime.now().year, month, day)

        if datetime.now() < show:
            return 'This day is in the future, do not peek!'
        else:
            file_path = show.strftime('html/%m-%d.html')
            try:
                content = open(file_path).read()
            except IOError as e:
                content = "Day not found. Sorry! Try again later."
            
            date_next = show  + timedelta(days = 1)

            if datetime.now() < date_next:
                day_next = False
            else:
                day_next = date_next.strftime('%m/%d')

            return render_template('template.html', 
                daytext = content.decode('utf-8'),
                day_before = (show  - timedelta(days = 1)).strftime('%m/%d'),
                today = (datetime.now()).strftime('%m/%d'),
                day_next = day_next
            )

    

@app.route('/humans.txt')
def humans():
    return 'Finn @finnpauls, mokus @juliaguar'

# Development (Does not work in gunicorn production)
app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()