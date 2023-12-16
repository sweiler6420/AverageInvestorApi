from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text
from .. import models, schemas, utils, oauth2
from ..database import get_db
from uuid import UUID
from typing import List, Optional
import math
import requests

router = APIRouter(
    prefix="/v1/news",
    tags=['News']
)

@router.get("/")
def get_top_stories(db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user)): 

    response = {
        "status": "ok",
        "totalResults": 36,
        "articles": [
            {
            "source": {
                "id": "reuters",
                "name": "Reuters"
            },
            "author": "Reuters",
            "title": "Congress passes $886 billion defense policy bill, Biden to sign into law - Reuters",
            "description": None,
            "url": "https://www.reuters.com/world/us/congress-passes-886-billion-defense-policy-bill-biden-sign-into-law-2023-12-14/",
            "urlToImage": None,
            "publishedAt": "2023-12-14T22:09:00Z",
            "content": None
            },
            {
            "source": {
                "id": "nfl-news",
                "name": "NFL News"
            },
            "author": None,
            "title": "2023 NFL season, Week 15: Six things to watch for in Vikings-Bengals, Steelers-Colts, Broncos-Lions on NFL Network - NFL.com",
            "description": "NFL.com's Eric Edholm breaks down six things to watch for on Saturday's tripleheader featuring: Vikings-Bengals, Steelers-Colts and Broncos-Lions.",
            "url": "https://www.nfl.com/news/2023-nfl-season-week-15-six-things-to-watch-for-in-nfln-tripleheader",
            "urlToImage": "https://static.www.nfl.com/image/upload/t_editorial_landscape_12_desktop/league/hrmykhenfgpttx4rc9cy",
            "publishedAt": "2023-12-14T22:03:00Z",
            "content": "There currently are seven NFL teams with 7-6 records, all flirting with the playoffs as we hit the home stretch. Five of those teams will be in action on Saturday in NFL Network's tripleheader (also … [+1192 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "HuffPost"
            },
            "author": "Taiyler S. Mitchell",
            "title": "Cause Of Death Released For 'Brooklyn Nine-Nine' Actor Andre Braugher - HuffPost",
            "description": "The actor passed away earlier this week at the age of 61.",
            "url": "https://www.huffpost.com/entry/andre-braugher-lung-cancer_n_657b49b5e4b020f3b674325e",
            "urlToImage": "https://img.huffingtonpost.com/asset/657b622f240000330076a7aa.jpeg?cache=nS0SYAFI2n&ops=1200_630",
            "publishedAt": "2023-12-14T21:41:45Z",
            "content": "Actor Andre Braugher died from lung cancer on Monday, his publicist confirmed to HuffPost.\r\nBraugher was diagnosed with cancer just months before his death, according to the New York Times.\r\nBraugher… [+3299 chars]"
            },
            {
            "source": {
                "id": "cbs-news",
                "name": "CBS News"
            },
            "author": "Camilo Montoya-Galvez, Ed O'Keefe",
            "title": "Drastic border restrictions considered by Biden and the Senate reflect seismic political shift on immigration - CBS News",
            "description": "The president's willingness to support strict border policies reflects a seismic shift in the politics of immigration over the past several years.",
            "url": "https://www.cbsnews.com/news/immigration-biden-senate-us-mexico-border-restrictions/",
            "urlToImage": "https://assets3.cbsnewsstatic.com/hub/i/r/2023/12/14/504fefb1-947b-45db-aec8-a1086b3fe26b/thumbnail/1200x630g2/6def0a317a667ec435cda7d1f7cfe14b/gettyimages-1843493359.jpg?v=5382e209c94ee904b3a96a69f8ca0ce0",
            "publishedAt": "2023-12-14T21:34:00Z",
            "content": "Washington — Less than two weeks after he took office and halted border wall construction, announced a deportation pause and suspended a rule requiring migrants to await their court dates in Mexico, … [+5778 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "Yahoo Entertainment"
            },
            "author": "Antonio Losada",
            "title": "Fantasy Football Week 15: Los Angeles Chargers vs. Las Vegas Raiders start 'em, sit 'em, how to watch TNF and more - Yahoo Sports",
            "description": "Two division rivals starting backup quarterbacks square off at the start of a must-win fantasy week. Antonio Losada delivers his matchup breakdown.",
            "url": "https://sports.yahoo.com/fantasy-football-week-15-los-angeles-chargers-vs-las-vegas-raiders-start-em-sit-em-how-to-watch-tnf-and-more-171638775.html",
            "urlToImage": "https://s.yimg.com/ny/api/res/1.2/mjoHk3f6.QsE9uiYZpRs2g--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://s.yimg.com/os/creatr-uploaded-images/2023-12/cb0cb7f0-9a9f-11ee-befe-1512457ed92e",
            "publishedAt": "2023-12-14T21:33:20Z",
            "content": "You can watch \"Thursday Night Football,\" Chargers vs. Raiders, exclusively on Amazon Prime Video at 8:15 p.m. ET.\r\nThe Las Vegas Raiders host the Los Angeles Chargers on Thursday Night Football. Perh… [+11413 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "Nbcsportsbayarea.com"
            },
            "author": "Tristi Rodriguez",
            "title": "Nurkic still respects Draymond, has ‘no bad feelings' after incident - NBC Sports Bay Area",
            "description": "Jusuf Nurkić said he still has nothing but respect for Draymond Green despite the incident that unfolded during Tuesday night’s Golden State Warriors vs. Phoenix Suns game.",
            "url": "http://www.nbcsportsbayarea.com/nba/golden-state-warriors/draymond-green-jusuf-nurkic-suspension/1681511/",
            "urlToImage": "https://media.nbcsportsbayarea.com/2023/12/jusuf-nurkic-draymond-green-USATSI.jpg?quality=85&strip=all&resize=1200%2C675",
            "publishedAt": "2023-12-14T21:12:35Z",
            "content": "Jusuf Nurki still respects Draymond Green and doesn't view him any differently, even after taking a hit to the face from the Warriors' veteran forward Tuesday night.\r\nI have a lot of respect for him,… [+1826 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "Space.com"
            },
            "author": "Mike Wall",
            "title": "Sun unleashes monster X-class solar flare, most powerful since 2017 (video) - Space.com",
            "description": "The flare may have been accompanied by a plasma eruption aimed at Earth.",
            "url": "https://www.space.com/sun-x-flare-december-2023-most-powerful-since-2017",
            "urlToImage": "https://cdn.mos.cms.futurecdn.net/T9B26kRvyBn52rKAPVX4wn-1200-80.jpg",
            "publishedAt": "2023-12-14T21:04:03Z",
            "content": "Space is part of Future US Inc, an international media group and leading digital publisher. Visit our corporate site.\r\n©\r\nFuture US, Inc. Full 7th Floor, 130 West 42nd Street,\r\nNew York,\r\nNY 10036."
            },
            {
            "source": {
                "id": "ars-technica",
                "name": "Ars Technica"
            },
            "author": "Ron Amadeo",
            "title": "Four years after Apple, Google will finally kill third-party cookies in 2024 - Ars Technica",
            "description": "Google delayed long enough to secure its ad business with new tracking methods.",
            "url": "https://arstechnica.com/gadgets/2023/12/chrome-will-finally-kill-third-party-tracking-cookies-in-2024/",
            "urlToImage": "https://cdn.arstechnica.net/wp-content/uploads/2021/03/Chrome-Getty-760x380.jpg",
            "publishedAt": "2023-12-14T21:00:30Z",
            "content": "34\r\nChrome has finally announced plans to kill third-party cookies. It's been almost four years since third-party cookies have been disabled in Firefox and Safari, but Google, one of the world's larg… [+2394 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "247Sports"
            },
            "author": "Carter Bahns",
            "title": "College football bowl games: Matchups, storylines for Saturday's opening slate - 247Sports",
            "description": "The postseason gets underway with a loaded Saturday schedule.",
            "url": "https://247sports.com/longformarticle/college-football-bowl-games-matchups-storylines-for-saturdays-opening-slate-223141098/",
            "urlToImage": "https://s3media.247sports.com/Uploads/Assets/612/3/12003612.jpg",
            "publishedAt": "2023-12-14T20:48:45Z",
            "content": "Bowl season is here. Over the next three weeks, the 2023 college football season will close in style with matchups between some of its best teams, with everything culminating in the final four-team C… [+1039 chars]"
            },
            {
            "source": {
                "id": "fox-news",
                "name": "Fox News"
            },
            "author": "Brandon Gillespie",
            "title": "Karine Jean-Pierre blows up when pressed on Biden connection to Hunter's business dealings: 'No evidence!' - Fox News",
            "description": "White House press secretary Karine Jean-Pierre lashed out when pressed on President Biden's connection to his son's foreign business associates, claiming he didn't do anything wrong.",
            "url": "https://www.foxnews.com/politics/karine-jean-pierre-blows-up-pressed-biden-connection-hunter-business-dealings",
            "urlToImage": "https://static.foxnews.com/foxnews.com/content/uploads/2023/12/GettyImages-1848352538.jpg",
            "publishedAt": "2023-12-14T20:42:56Z",
            "content": "White House press secretary Karine Jean-Pierre blew up Thursday when pressed by a reporter on President Biden \"lying\" about past interactions with his son Hunter's business associates, declaring ther… [+3394 chars]"
            },
            {
            "source": {
                "id": "cbs-news",
                "name": "CBS News"
            },
            "author": None,
            "title": "Denmark, Germany arrest terror suspects, including alleged Hamas members, authorities say - CBS News",
            "description": "Denmark and Germany announced Thursday arrests of several terror suspects, including alleged Hamas members suspected of plotting attacks on Jews.",
            "url": "https://www.cbsnews.com/news/hamas-germany-denmark-terror-attacks-foiled-against-jewish-targets/",
            "urlToImage": "https://assets1.cbsnewsstatic.com/hub/i/r/2023/12/14/f39304af-28ed-49d5-ae1d-9779c90e2bec/thumbnail/1200x630/5cb6f8ac3f31aea311152fd84ae95423/gettyimages-1848353757.jpg?v=5382e209c94ee904b3a96a69f8ca0ce0",
            "publishedAt": "2023-12-14T20:34:52Z",
            "content": "Denmark and Germany announced Thursday the arrests of several terror suspects, including alleged Hamas members suspected of plotting attacks on Jews and Jewish institutions in Europe over the ongoing… [+4336 chars]"
            },
            {
            "source": {
                "id": "cbs-news",
                "name": "CBS News"
            },
            "author": "Sara Moniuszko, Tina Kraus",
            "title": "Scientists may have pinpointed morning sickness cause, sparking hope for potential cures - CBS News",
            "description": "Lowering or pre-exposing a pregnant person to the hormone GDF15 could help lessen morning sickness symptoms once pregnant, according to new research.",
            "url": "https://www.cbsnews.com/news/morning-sickness-cause-pregnancy-hormone-treatment/",
            "urlToImage": "https://assets2.cbsnewsstatic.com/hub/i/r/2023/12/14/a1df1ce2-71f8-4dfa-959b-0113ccfcc233/thumbnail/1200x630/923fc6e6c3f243e706990a1ac7a0af79/gettyimages-639375806.jpg?v=5382e209c94ee904b3a96a69f8ca0ce0",
            "publishedAt": "2023-12-14T20:19:00Z",
            "content": "Scientists may have discovered the exact cause of morning sickness, the nausea and vomiting that often accompanies pregnancy — and with the discovery, better treatment options could be on the horizon… [+3160 chars]"
            },
            {
            "source": {
                "id": "abc-news",
                "name": "ABC News"
            },
            "author": "Aaron Katersky",
            "title": "Ex-FBI counterintelligence chief Charles McGonigal sentenced to 50 months in prison for working with Russian oligarch - ABC News",
            "description": "McGonigal's lawyers had said he deserved no prison time.",
            "url": "https://abcnews.go.com/US/fbi-counterintelligence-chief-charles-mcgonigal-sentencing-begin/story?id=105642391",
            "urlToImage": "https://i.abcnewsfe.com/a/001eb2d9-4037-40b2-9247-c22f97549f78/charles-mcgonigal-1-rt-bb-231213_1702504529577_hpMain_16x9.jpg?w=992",
            "publishedAt": "2023-12-14T19:58:34Z",
            "content": "One of the highest-ranking FBI agents to ever face criminal charges was sentenced to over four years in prison on Thursday for secretly colluding with a Russian oligarch.\r\nCharles McGonigal, a former… [+3921 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "Rolling Stone"
            },
            "author": "Angie Martoccio",
            "title": "Taylor Swift Proposal Tears Pennsylvania Legislature Apart - Rolling Stone",
            "description": "Pennsylvania House Legislators argued — and then passed — a proposal to recognize 2023 as the \"Taylor Swift Era.\"",
            "url": "https://www.rollingstone.com/music/music-news/taylor-swift-pennsylvania-legislature-cringe-1234928841/",
            "urlToImage": "https://www.rollingstone.com/wp-content/uploads/2023/12/taylor-swift-pennsylvania-era.jpg?crop=0px%2C47px%2C1800px%2C1015px&resize=1600%2C900",
            "publishedAt": "2023-12-14T19:41:31Z",
            "content": "In case you forgot, government officials love to get cringey over Taylor Swift. Remember when the FBI encouraged narcing through her lyrics? We now have a new low: Pennsylvania House Legislators argu… [+2391 chars]"
            },
            {
            "source": {
                "id": "business-insider",
                "name": "Business Insider"
            },
            "author": "Eugene Kim",
            "title": "Nvidia Employees Are Now so Rich, They've Got a 'Semi-Retirement' Problem, Insiders Say - Business Insider",
            "description": "Nvidia's skyrocketing success and employee-centric culture has created a byproduct: \"semi-retired\" employees, insiders say.",
            "url": "https://www.businessinsider.com/nvidia-employees-rich-happy-problem-insiders-say-2023-12",
            "urlToImage": "https://i.insider.com/657a23ae0ec98e92f74f3104?width=1200&format=jpeg",
            "publishedAt": "2023-12-14T19:21:00Z",
            "content": "Nvidia's stratospheric rise this year has engendered an unusual problem: Some of the longer-tenured employees, sitting on a wealth of company stock, are no longer doing their fair share of work.It's … [+8813 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "Vox"
            },
            "author": "Li Zhou",
            "title": "Global support for a Gaza ceasefire is growing. The US is an outlier. - Vox.com",
            "description": "When it comes to the war in Gaza against Hamas, the US and Israel are becoming “increasingly isolated.”",
            "url": "https://www.vox.com/politics/2023/12/14/24001352/gaza-ceasefire-united-nations-israel-palestine",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/06XsICzj98zE6GITs5oQ02oKVbM=/0x0:8069x4225/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/25162662/1843519202.jpg",
            "publishedAt": "2023-12-14T19:10:00Z",
            "content": "The international community is increasingly turning against Israels ongoing military onslaught in Gaza, in large part due to a growing civilian death toll and humanitarian crisis. Thats putting new p… [+7632 chars]"
            },
            {
            "source": {
                "id": None,
                "name": "Science.org"
            },
            "author": "Science",
            "title": "Science's 2023 Breakthrough of the Year: Weight loss drugs with a real shot at fighting obesity - Science",
            "description": None,
            "url": "https://www.science.org/content/article/breakthrough-of-the-year-2023",
            "urlToImage": None,
            "publishedAt": "2023-12-14T19:00:00Z",
            "content": None
            },
            {
            "source": {
                "id": "wired",
                "name": "Wired"
            },
            "author": "Will Knight",
            "title": "OpenAI's Ilya Sutskever Has a Plan for Keeping Super-Intelligent AI in Check - WIRED",
            "description": "The Superalignment team led by OpenAI chief scientist Ilya Sutskever has devised a way to guide the behavior of AI models as they get ever smarter.",
            "url": "https://www.wired.com/story/openai-ilya-sutskever-ai-safety/",
            "urlToImage": "https://media.wired.com/photos/657a4dc7d50c518000e43e90/191:100/w_1280,c_limit/OpenAI-Superalignment-Business-1554148483.jpg",
            "publishedAt": "2023-12-14T18:44:45Z",
            "content": "OpenAI was founded on a promise to build artificial intelligence that benefits all of humanityeven when that AI becomes considerably smarter than its creators. Since the debut of ChatGPT last year an… [+2541 chars]"
            },
            {
            "source": {
                "id": "the-wall-street-journal",
                "name": "The Wall Street Journal"
            },
            "author": "Veronica Dagher",
            "title": "What Fed Rate Cuts Mean for Home Buyers in 2024 - The Wall Street Journal",
            "description": "Mortgage rates will likely lose some of their sting, giving home market a boost",
            "url": "https://www.wsj.com/personal-finance/mortgages/interest-rate-cuts-2024-mortgages-76172791",
            "urlToImage": "https://images.wsj.net/im-900204/social",
            "publishedAt": "2023-12-14T18:25:00Z",
            "content": None
            },
            {
            "source": {
                "id": "financial-times",
                "name": "Financial Times"
            },
            "author": None,
            "title": "EU leaders agree to start accession talks with Ukraine - Financial Times",
            "description": "Landmark decision comes after days of opposition from Hungary’s prime minister",
            "url": "https://www.ft.com/content/deb40df7-7832-4fee-a822-655ab0288c05",
            "urlToImage": None,
            "publishedAt": "2023-12-14T18:12:35Z",
            "content": "Keep abreast of significant corporate, financial and political developments around the world. Stay informed and spot emerging risks and opportunities with independent global reporting, expert comment… [+30 chars]"
            }
        ]
    }
    
    # response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey=37bad2311c404a92849d9452d40aafde')

    # response = response.json()

    return response

