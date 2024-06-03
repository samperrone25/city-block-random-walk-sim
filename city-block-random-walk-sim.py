import random
import copy
import math

def probability_2p_meet(n):
    sum = 0
    for i in range(n+1): # i: 0 |--| n
        sum += ((math.factorial(n)/(math.factorial(n-i) * math.factorial(i))) ** 2)
    return sum/2**(2*n)

'''
4x4 square city grid
p1 starts bottom left, p2 starts top right
both random walking at same pace along block edges toward each others starting points
if meet, will do so along the diagonal halfway between them after each have walked 4 square edges
aim: simulate meets and non-meets 
'''

# Returns number of times all players met
def run_sims(n, players, player_moves, initial_coords, grid_len) -> int:
    num_met = 0
    for i in range(n):
        if run_sim(players, player_moves, initial_coords, grid_len):
            num_met += 1
    return num_met

# True if all players met, False if not 
def run_sim(players, player_moves, initial_coords, grid_len) -> bool:
    player_coords = copy.deepcopy(initial_coords) # avoid changing initial_coords
    num_moves = 0
    while num_moves < grid_len:
        move_players(players, player_moves, player_coords)
        num_moves += 1
    loc = player_coords[players[0]] # first player end location, assumes min 1 player
    print('locs after sim {}'.format(player_coords))
    for player in players:
        if player_coords[player] != loc:
            return False
    print('MET!')
    return True

def move_players(players, player_moves, player_coords):
    for player in players: # move for each player
        allowed_moves = player_moves[player]
        move_choice = allowed_moves[random.randint(0, len(allowed_moves)-1)]
        coords = player_coords[player]
        if move_choice == 'up':
            coords[1] += 1
        elif move_choice == 'right':
            coords[0] += 1
        elif move_choice == 'left':
            coords[0] -= 1
        elif move_choice == 'down':
            coords[1] -= 1

if __name__ == '__main__':

    num_sims = 100000

    players = [1,2]
    player_moves = {1:['up', 'right'], 2:['down', 'left']} # moves possible for players
    initial_coords = {1: [0,0], 2: [15,15]} # replace with vectors to make n-dimensional
    grid_len = 15

    num_met = run_sims(num_sims, players, player_moves, initial_coords, grid_len)
    print('With a grid of {} edges'.format(grid_len))
    print('Players {} met {} / {} times or P = {}'.format(players, num_met, num_sims, float(num_met)/num_sims))
    prob = probability_2p_meet(grid_len)
    print('Theoretical value  P = {}'.format(prob))
    '''
    players = [1,2,3,4]
    player_moves = {1:['up', 'right'], 2:['down', 'left'], 3:['up', 'left'], 4:['down','right']} # moves possible for players
    initial_coords = {1: [0,0], 2: [6,6], 3:[6,0], 4:[0,6]} # replace with vectors to make n-dimensional
    grid_len = 6

    num_met = run_sims(num_sims, players, player_moves, initial_coords, grid_len)
    print('Players {} met {} / {} times'.format(players, num_met, num_sims))
    '''

    
    