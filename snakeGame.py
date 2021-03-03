import random
import time
import os
import keyboard

def show(arr):
	for row in arr:
		print(''.join(row))

def putApple(arr):
	x, y = [], []
	for row in range(len(arr)):
		for col in range(len(arr[row])):
			if arr[row][col] == '⬛':
				x += [row]
				y += [col]
			elif arr[row][col] == '🍎':
				arr[row][col] = '⬛'

	arr[random.choice(x)][random.choice(y)] = '🍎'
	return arr

def key():
	time.sleep(0.2)
	start = time.time()
	while time.time() - start < 0.2:
		if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
			return 'W'
		if keyboard.is_pressed('a') or keyboard.is_pressed('left'):
			return 'A'
		if keyboard.is_pressed('s') or keyboard.is_pressed('down'):
			return 'S'
		if keyboard.is_pressed('d') or keyboard.is_pressed('right'):
			return 'D'
	return 0

def go(arr, head, tail):
	global score

	if head[2] == 'W':
		if arr[head[0]-1][head[1]] == '🍎':
			arr[head[0]-1][head[1]] = '🟩'
			head[0] -= 1
			score += 1
			return putApple(arr), tail

		elif arr[head[0]-1][head[1]] == '🟩':
			return 0, 0

		else:
			arr[head[0]-1][head[1]] = '🟩'
			arr[tail[0][0]][tail[0][1]] = '⬛'
			
			tail = tail[1:]
			head[0] -= 1
			return arr, tail
		
	elif head[2] == 'S':
		if arr[head[0]+1][head[1]] == '🍎':
			arr[head[0]+1][head[1]] = '🟩'
			head[0] += 1
			score += 1
			return putApple(arr), tail

		elif arr[head[0]+1][head[1]] == '🟩':
			return 0, 0

		else:
			arr[head[0]+1][head[1]] = '🟩'
			arr[tail[0][0]][tail[0][1]] = '⬛'
			
			tail = tail[1:]
			head[0] += 1
			return arr, tail

	elif head[2] == 'A':
		if arr[head[0]][head[1]-1] == '🍎':
			arr[head[0]][head[1]-1] = '🟩'
			head[1] -= 1
			score += 1
			return putApple(arr), tail

		elif arr[head[0]][head[1]-1] == '🟩':
			return 0, 0

		else:
			arr[head[0]][head[1]-1] = '🟩'
			arr[tail[0][0]][tail[0][1]] = '⬛'
			
			tail = tail[1:]
			head[1] -= 1
			return arr, tail

	elif head[2] == 'D':
		if arr[head[0]][head[1]+1] == '🍎':
			arr[head[0]][head[1]+1] = '🟩'
			head[1] += 1
			score += 1
			return putApple(arr), tail

		elif arr[head[0]][head[1]+1] == '🟩':
			return 0, 0
			
		else:
			arr[head[0]][head[1]+1] = '🟩'
			arr[tail[0][0]][tail[0][1]] = '⬛'
		
			tail = tail[1:]
			head[1] += 1
			return arr, tail

arr = [['⬛']*10 for row in range(10)]
arr[4][4] = '🟩'
arr = putApple(arr)
head, tail = [4,4,'D'], []
score = 0

while True:
	print(f'Score: {score}')
	show(arr)
	
	tail += [[head[0], head[1]]]

	keyDir = key()
	if keyDir != 0:
		head[2] = keyDir

	arr, tail = go(arr, head, tail)
	if arr == 0:
		break
	
	os.system('cls')

print('\nGame Ended!')
print(f'Final Score: {score}')
