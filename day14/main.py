from itertools import count
from operator import le
from re import match
from unittest import case


def main():
    # f = open("day14/example.txt", "r")
    f = open("day14/input.txt", "r")

    input = f.read().split('\n')

    maze = []
    for line in input:
        maze.append([ char for char in line])

    for i in range(1000):
        total = 0
        move_north(maze)
        move_west(maze)
        move_south(maze)
        move_east(maze)
        for i in range(len(maze)):
            total += maze[i].count('O') * (len(maze) - i)
        print(total)    

def move_north(maze):
    for x in range(len(maze)):
        for y in range (len(maze[0])):
            if (maze[x][y] == 'O'):
                roll_top(x, y, maze, 'N')

def move_west(maze):
    for x in range(len(maze)):
        for y in range (len(maze[0])):
            if (maze[x][y] == 'O'):
                roll_top(x, y, maze, 'W')

def move_south(maze):
    for x in range(len(maze)-1, -1,-1):
        for y in range (len(maze[0]) -1, -1, -1):
            if (maze[x][y] == 'O'):
                roll_top(x, y, maze, 'S')

def move_east(maze):
    for x in range(len(maze)-1,-1,-1):
        for y in range (len(maze[0])-1,-1, -1):
            if (maze[x][y] == 'O'):
                roll_top(x, y, maze, 'E')


def roll_top(x, y, maze, direction):
    match direction:
        case 'N':
            if x == 0:
                maze[x][y] = 'O'
                return
            if maze[x-1][y] == '.':
                maze[x-1][y], maze[x][y] = 'O', '.'
                roll_top(x-1, y, maze, direction)
        case 'W':
            if y == 0:
                maze[x][y] = 'O'
                return
            if maze[x][y-1] == '.':
                maze[x][y-1], maze[x][y] = 'O', '.'
                roll_top(x, y-1, maze, direction)
        case 'S':
            if x == len(maze) - 1:
                maze[x][y] = 'O'
                return
            if maze[x+1][y] == '.':
                maze[x+1][y], maze[x][y] = 'O', '.'
                roll_top(x+1, y, maze, direction)
            # elif maze[x+1][y] == 'O':
            #     roll_top(x+1, y, maze, direction)

        case 'E':
            if y == len(maze[0]) - 1:
                maze[x][y] = 'O'
                return
            if maze[x][y+1] == '.':
                maze[x][y+1], maze[x][y] = 'O', '.'
                roll_top(x, y+1, maze, direction)


def print_maze(maze):
    for line in maze:
        print(line)
    print('\n')
main()