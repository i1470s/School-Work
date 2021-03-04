Python 3.8.2 (default, Feb 26 2020, 02:56:10)
 players = [29, 5 , 1, 2]
 players[2]
1
 players[2]= 68
 players
[29, 5, 68, 2]
 players + [90, 91, 92]
[29, 5, 68, 2, 90, 91, 92]
 players
[29, 5, 68, 2]
 players[:2]
[29, 5]
 players[:7] = [0, 0]
 players
[0, 0]
 players[:2] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
 
KeyboardInterrupt
 
KeyboardInterrupt
 players[:2] = []
 players
[]