# Get movie information from rottentomates 
====================================
Show movie information from rottentomatoes and atmovies in terminal

![image](https://github.com/Ray0907/movie/blob/master/screenshot/screenshot.png )
![image](https://github.com/Ray0907/movie/blob/master/screenshot/screenshot_2.png)
![image](http://recordit.co/WISLRIy8cv.gif )

------------------
# Requirements
- Python 3.6
- [Urwid](https://github.com/urwid/urwid)
- Requests
- BeautifulSoup
- lxml
- [six](https://github.com/benjaminp/six)

# Usage
Display movie infomation in terminal
```
$ rottentomatoes 'mission impossible'
```

```
$ atmovies 'mission impossible'
```
Output
```
===============   RottenTomatoes   ====================
Title: Mission: Impossible
TOMATOMETER: 63%
AUDIENCE SCORE: 71%
Year: 1996
Casts: Tom Cruise, Jon Voight, Emmanuelle Béart, 
Introduction: 
    After he is framed for the death of several colleagues and falsely branded a traitor, a secret agent embarks on a daring scheme to clear his name in this spy adventure. Though it drew its name from the familiar television series, director Brian DePalma's big-budget adaptation shares little more with the original show than the occasional self-destructing message and the name of team leader Jim Phelps (Jon Voight). The film focuses not on Phelps but his protégé, Ethan Hunt (a reserved Tom Cruise), who becomes a fugitive after taking the blame for a botched operation. He responds by banding together with a group of fellow renegades, and he is soon maneuvering his way through a twisted series of double crosses that mainly serve as excuses for spectacular high-tech action sequences. Much of the activity revolves around a missing computer disk, with the film's most famous scene depicting Hunt's delicate efforts to retrieve the disk from a secure, well-alarmed room in CIA headquarters. ~ Judd Blaise, Rovi
=====================================================
```

```
===============   開眼電影   ====================
Title: 不可能的任務：全面瓦解 Mission: Impossible - Fallout 
上映日期：2018/07/25
Introduction: 

 劇情簡介
                        
                         這次《不可能的任務：全面瓦解》的最強看點，一窺拚命阿湯哥如何挑戰這集不可能的任務，所有特技皆親自上陣（包括機車追逐被撞、近身搏擊入危機！前所未見的極大危機與威脅，即將全面瓦解你所知道的一切？《不可能的任務：全面瓦解》伊森韓特與他的IMF隊員們（亞歷鮑德溫、賽門佩格和文雷姆斯飾演）以及府恐怖組織「辛迪加」的領導人連恩後，接下新任務是阻止餘黨、以約翰拉克為首的12個「使徒」的瘋狂計畫，伊森韓特得早一步比「使徒」先拿到鈽元素，避免讓「使徒」團隊，並且借助盟友伊爾莎(蕾貝卡弗格森 飾演)的消息，合力再找回鈽元素。這一集更加入重量級卡司：亨利卡維爾、安琪拉貝瑟與凡妮莎寇比，導演是由執導《不可能的任務：失控國度》克里斯多弗麥奎里再度擔綱。  
 
=====================================================

```

Show the list of the movie

```
$ rottentomatoes 'mission impossible' -l
```

```
$ atmovies 'mission impossible' -l
```
