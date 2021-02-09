""" Automatically create tournaments"""

import json
import requests
import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

URL = 'https://lichess.org/api/tournament'
TOKEN = 'OfP36RvsUPC6RT3L'
TOURNAMENT = datetime.datetime.combine(datetime.date.today() + datetime.timedelta((2-datetime.date.today().weekday())%7), datetime.time(hour=22))
DATA = {
    'name': 'Umich Weekly Arena',
    'clockTime': 5,
    'clockIncrement': 0,
    'minutes': 120,
    'startDate': int(TOURNAMENT.timestamp())*1000,
    'conditions.teamMember.teamId': 'umich-chess-club'
}
fil = open('key.txt')
OPEN = json.loads(requests.post(URL, data=DATA, headers={'Authorization': f'Bearer {TOKEN}'}).content)


DATA['name'] = 'Umich U1800 Weekly Arena'
DATA['clockIncrement'] = 3
DATA['startDate'] = int((TOURNAMENT + datetime.timedelta(days=1)).timestamp())*1000
DATA['conditions.maxRating.rating'] = 1800
U1800 = json.loads(requests.post(URL, data=DATA, headers={'Authorization': f'Bearer {TOKEN}'}).content)

DATA['name'] = 'Umich U1200 Weekly Arena'
DATA['clockTime'] = 10
DATA['clockIncrement'] = 5
DATA['startDate'] = int((TOURNAMENT + datetime.timedelta(days=-1)).timestamp())*1000
DATA['conditions.maxRating.rating'] = 1200
DATA['beserkable'] = False
U1200 = json.loads(requests.post(URL, data=DATA, headers={'Authorization': f'Bearer {TOKEN}'}).content)

message = Mail(
    from_email='silversteinjonathan00@gmail.com',
    to_emails='chess.club@umich.edu',
    subject='Weekly Chess Arenas',
    html_content=f'''<p>Hello,</p>
    <div>The chess arenas for this week are posted below:
        <ul>
            <li>Tuesday U1200 6-8pm 10+5 (No Beserk): https://lichess.org/tournament/{U1200['id']}</li>
            <li>Wednesday Open 6-8pm 5+0: https://lichess.org/tournament/{OPEN['id']}</li>
            <li>Thursday U1800 6-8pm 5+3: https://lichess.org/tournament/{U1800['id']}</li>
        </ul>
    Best, Jonathan</div>''',
)
SEND_KEY = fil.read().strip()
sg = SendGridAPIClient(SEND_KEY)
response = sg.send(message)
