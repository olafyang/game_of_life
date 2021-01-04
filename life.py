import random
import time


def init_dead_state(width, height):
	temp = [0] * width
	# board = [temp[:]] * height
	board = [temp[:] for i in range(height)]
	return board


def init_random_state(w, h):

	state = init_dead_state(w, h)
	for i in range(len(state)):

		for n in range(len(state[i])):
			rand_number = random.random()

			if rand_number < 0.5:
				state[i][n] = 0
			else:
				state[i][n] = 1

	return state


def calc_next_state(state):
	# check if current cell is alive
	for i in range(len(state)):
		for n in range(len(state[i])):
			# top row
			if i == 0:
				if n == 0:
					neighboring_cell_state_list = [
						state[i][n + 1], state[i + 1][n], state[i + 1][n + 1]
					]
				elif n == len(state[i]) - 1:
					neighboring_cell_state_list = [
						state[i][n - 1], state[i + 1][n], state[i + 1][n - 1]
					]
				else:
					neighboring_cell_state_list = [
						state[i][n - 1], state[i][n + 1],
						state[i + 1][n - 1], state[i + 1][n], state[i + 1][n + 1]
					]
			# bottom row
			elif i == len(state) - 1:
				if n == 0:
					neighboring_cell_state_list = [
						state[i][n + 1], state[i - 1][n], state[i - 1][n + 1]
					]
				elif n == len(state[i]) - 1:
					neighboring_cell_state_list = [
						state[i][n - 1], state[i - 1][n -1], state[i - 1][n]
					]
				else:
					neighboring_cell_state_list = [
						state[i][n - 1], state[i][n + 1],
						state[i - 1][n - 1], state[i - 1][n], state[i - 1][n + 1]
					]
			# middle
			else:
				if n == 0:
					neighboring_cell_state_list = [
						state[i - 1][n], state[i - 1][n + 1],
						state[i][n + 1],
						state[i + 1][n], state[i + 1][n + 1]
					]
				elif n == len(state[i]) - 1:
					neighboring_cell_state_list = [
						state[i - 1][n - 1], state[i - 1][n],
						state[i][n - 1],
						state[i + 1][n - 1], state[i + 1][n]
					]
				else:
					neighboring_cell_state_list = [
						state[i - 1][n - 1], state[i - 1][n], state[i - 1][n + 1],
						state[i][n - 1], state[i][n + 1],
						state[i + 1][n - 1], state[i + 1][n], state[i + 1][n + 1]
					]

			# calculate next state

			number_of_alive_neighboring_cell = neighboring_cell_state_list.count(1)

			if state[i][n] == 1:
				if number_of_alive_neighboring_cell <= 1:
					state[i][n] = 0
				elif number_of_alive_neighboring_cell > 3:
					state[i][n] = 0
				else:
					state[i][n] = 1
			else:
				if number_of_alive_neighboring_cell == 3:
					state[i][n] = 1

	return state


def pretty_print(state):
	for row in state:
		for cell in row:
			if cell == 1:
				print('#', end='')
			else:
				print(' ', end='')
		print()
	print('--------------------------')


def run():
	state = init_random_state(15, 15)
	pretty_print(state)
	while True:
		try:
			state = calc_next_state(state)
			pretty_print(state)
			time.sleep(1)
		except KeyboardInterrupt:
			break


if __name__ == '__main__':
	run()
