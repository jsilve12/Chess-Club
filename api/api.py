""" File to store API Endpoints related to accounts """
from fastapi import Depends, FastAPI, APIRouter


router = APIRouter()


@router.get('/navbar/pages')
async def navbar():
    return [
            {'url': '/', 'name': 'Home'},
            {'url': '/about', 'name': 'About'},
            {'url': '/tournaments', 'name': 'Tournaments'},
            {'url': '/learning', 'name': 'Learning'},
            # {'url': '/calendar', 'name': 'Calendar'},
        ]


@router.get('/navbar/name')
async def name():
    return 'Michigan Chess'


@router.get('/tournaments/weekly')
async def weekly_tournaments():
    return {
        'Title': 'Weekly Tournaments',
        'Cards': [
            {
                'Title': 'U1200 Tournament',
                'Subtitle': 'Tuesday 6-8pm EST',
                'Body': 'This tournament is 10+5 with no beserk option, making it a good choice for people who want to try out chess, or who usually play slower time controls.',
            },
            {
                'Title': 'Open Tournament',
                'Subtitle': 'Wednesday 6-8pm EST',
                'Body': 'Our main, weekly event, open to all players. This is a 5+0 Lichess arena, with lots of high paced, competitive chess. Do you have what it takes to take home the gold?',
            },
            {
                'Title': 'U1800 Tournament',
                'Subtitle': 'Thursday 6-8pm EST',
                'Body': 'This weekly tournament is great for newer, or more casual chess players. With a 5+3 time control, you also have more time to think about moves.',
            },
        ]
    }


@router.get('/tournaments/other')
async def other_tournaments():
    return {
        'Title': 'Other Resources',
        'Cards': [
            {
                'Title': 'Lichess 4545',
                'Body': 'A great place to sharpen your classical chess skills, you get placed on a team of 8 people and then, you get to play one 45+45 game per week against a very serious opponent. You can find out more <a href=https://www.lichess4545.com/team4545/>here</a>.',
            },
            {
                'Title': 'Michigan Chess Association',
                'Body': 'The Michigan Chess Association runs a number of chess tournaments in the state of Michigan, as well as weekly arenas on Lichess. They also serve to compile lists of tournaments in Michigan, and can be a great resource, if you are looking for tournaments. They can be found <a href=https://www.michess.org/>here</a>.',
            },
            {
                'Title': 'US Chess Federation',
                'Body': 'The US Chess Federation is the governing body for chess in the United States. They maintain fairly accurate lists of clubs and tournaments around the country, as well as coordinating national ratings. To participate in most in person tournaments you need a USCF membership. More information can be found <a href=https://www.lichess4545.com/team4545/>here</a>.'
            }
        ]
    }


@router.get('/learning/club')
async def club_learning():
    return {
        'Title': 'Club Learning Opportunities',
        'Cards': [
            {
                'Title': 'Lessons',
                'Body': 'Starting in Winter Semester 2021, we are going to be rolling out a series of lessons. The goal to begin with, is to have three introductory lessons, with the potential for more, depending on how successful those are.'
            },
            {
                'Title': 'Books',
                'Body': 'Good books to start with include <i>How to Reassess Your Chess</i>, <i>Understanding Chess Endgames</i>, and <i>My System</i>. To get the most out of books, we recommend reading with a chess board on hand to help play out variations. Many of the more experienced players have decent sized libraries, and are willing to lend out books or pdfs. If you have a specific book feel free to contact us.'
            }
        ],
    }


@router.get('/learning/other')
async def other_learning():
    return {
        'Title': 'Other Recommendations and Resources',
        'Cards': [
            {
                'Title': 'Tactics Trainers',
                'Body': 'One of the best ways to improve at chess is to study tactics. There are a number of websites that have strong tactics trainers, but we recommend either Lichess or Chess Tempo.'
            },
            {
                'Title': 'Have a regular chess regimen',
                'Body': 'This should be a series of things you do daily that are chess oriented, other than playing games. Everyone is different, however a reasonable sample schedule might be 20 minutes of tactics, 20 minutes of reading, and 1-2 games a day.'
            },
            {
                'Title': 'Saint Louis Chess Club',
                'Body': 'The Saint Louis Chess Club includes some great education videos. They have targeted content for players of all levels. Find out more at their <a href=https://saintlouischessclub.org/>website</a>.'
            },
            {
                'Title': 'Coaches',
                'Body': 'Getting a coach can be a big step in your chess development, however it can also be fairly expensive. We recommend having a regular chess regimen before doing this, so you get the most out of it.'
            }
        ],
    }


@router.get('/about/officers')
async def about_officers():
    return {
        'Title': 'Officers',
        'Cards': [
            {
                'Title': 'Jonathan Silverstein',
                'Image': '/static/img/Jonathan.jpg',
                'Body': 'Jonathan is the 2020 Michigan Class C champion, currently a Class B player, and a Michigan alumni. He is currently working in Ann Arbor. He is in charge of web development for chess club.'
            },
            {
                'Title': 'Ali Darwiche',
                'Image': '/static/img/Ali.png',
                'Body': 'Hi! My name is Ali Darwiche and I am a senior studying Interdisciplinary Chemistry and Comparative Studies through the College of Literature, Science, and the Arts. I have been playing chess actively since high school. In my free time, I like learning about religion, practicing mixed martial arts, and, as you may have guessed, playing chess! Currently, I am working on teaching underserved students the life-changing game of chess in a virtual format!',
            },
            {
                'Title': 'Quinn Baker',
                'Image': '/static/img/Quinn.jpg',
                'Body': 'Quinn is a former board 1 at Oak Park and River Forest High School, coached by William Aramil, and was the 2016 Chicago West Suburban Conference Champion. He played for Michigan\'s A team at the 2019 PanAm Chess Championships. He is currently a senior studying Computer Science and Spanish. Quinn is also the President of the Michigan Table Tennis Club and represented the University of Michigan at the 2018 National Collegiate Championships.',
            },
        ]
    }


@router.get('/main')
async def main():
    return {
        'Cards': [
            {
                'Title': 'About Us',
                'Body': f'''<p>The Michigan Chess Club organizes recreational and competitive opportunities for University of Michigan students to share and develop their interest in chess. We provide a fun and open opportunity for our members to learn and play chess in a friendly environment. The club meets every Wednesday from 6-8 p.m. at Maizie's cafe in the Michigan League.</p>
                        <p class='d-lg-block d-none'>In addition, we host online tournaments and compete in local and national chess tournaments to represent the University of Michigan. In 2016 and 2018, we won two division titles and a mixed doubles award at the Pan-American Intercollegiate Team Chess Championship.</p>
                        <p class='d-lg-block d-none'>Beyond the University, our members are involved in various outreach activities in the Ann Arbor area, including teaching after-school chess classes for elementary schools, acting as arbiters in scholastic chess tournaments, and summer chess camps.</p>'''
            },
            {
                'Title': 'Daily Puzzle',
                'Iframe': "https://lichess.org/training/frame?theme=wood&bg=dark",
            },
            {
                'Title': 'Watch a master',
                'Iframe': "https://lichess.org/tv/frame?theme=wood&bg=dark",
            }
        ]
    }
