# Tic Tac Toe - on the terminal
Built using python and unicode!

<br>

## Table of contents
* [How to Play](#How-to-Play)
* [Features](#Features)
* [Coming Soon](#Coming-Soon)
* [Setup](#Setup)


## How to Play

```
Score:
 O: 0     X: 0
 
 1 ┃ 2 ┃ 3  
━━━╋━━━╋━━━
 4 ┃ 5 ┃ 6 
━━━╋━━━╋━━━
 7 ┃ 8 ┃ 9 

Choose spot: to select a square, input the number of the corresponding square
```


## Features
- Keeps track of player score
- alternates start player
- can ctrl+c out of most inputs nicely

## Coming Soon:
- [ ] Custom player name
- [ ] Custom Player symbol
- [ ] Add automatic platform detector for clear_screen 
- [ ] Game Over screen


## Setup:
```python

''' This game depends on console clear function '''

# Windows
def clear_screen(): 
    os.system('cls')

# Linux
def clear_screen(): 
    os.system('clear')

# no clear
def clear_screen(): 
    return

```


