# solver.py
import random
import builtins
from centipede import solved_centipede, n, generate_moves, swap_positive, swap_negative, scramble

def solve(centipede, solved):
    """Find the sequence of moves to solve the centipede."""
    state = centipede.copy()
    moves_tried = 0
    move_sequence = []

    while state != solved:
        moves = generate_moves(n)
        i, sign = random.choice(moves)
        if sign == "+":
            swap_positive(state, i)
        else:
            swap_negative(state, i)
        move_sequence.append(f"{i+1}{sign}")
        moves_tried += 1
        if moves_tried % 1000 == 0:
            print(f"[Solver] Tried {moves_tried} moves...")

    print(f"[Solver] Found solution in {moves_tried} moves.")
    return move_sequence

# monkey-patch scramble so we intercept the scrambled state
import centipede

original_scramble = centipede.scramble
solution_moves = []

def patched_scramble(solved_centipede, n):
    scrambled = original_scramble(solved_centipede, n)
    print(f"[Solver] Intercepted scrambled state: {scrambled}")
    print(f"[Solver] Solving...")
    global solution_moves
    solution_moves = solve(scrambled, solved_centipede)
    print(f"[Solver] Ready to feed {len(solution_moves)} moves into the game.")
    return scrambled

centipede.scramble = patched_scramble

# monkey-patch input so solver feeds moves into the game loop
original_input = builtins.input

def patched_input(prompt=""):
    original_input(prompt)  # still shows the prompt
    if solution_moves:
        move = solution_moves.pop(0)
        print(f"[Solver] Feeding move: {move}")
        return move
    return original_input(prompt)  # fall back to real input if solution runs out

builtins.input = patched_input

# now run the game — it will use our patched scramble and input
import runpy
runpy.run_module("centipede", run_name="__main__")