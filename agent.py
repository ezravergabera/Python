PERCEPTS = ['antipolo', 'cubao', 'pup']
ACTIONS = ['do_nothing', 'go to antipolo', 'go to cubao', 'go to pup']
RULES = {
    0: 'do_nothing',
    1: 'go to antipolo',
    2: 'go to cubao',
    3: 'go to pup'
}

def agent_with_memory(percept):
    global state

    if state is None:
        state = 1
        if percept == 'antipolo' and state != 1:
            state = 1
            action = 1
        elif percept == 'antipolo' and state == 1:
            state = 1
            action = 0
        elif percept == 'cubao' and state != 2:
            state = 2
            action = 2
        elif percept == 'cubao' and state == 2:
            state = 2
            action = 0
        elif percept == 'pup' and state != 3:
            state = 3
            action = 3
        elif percept == 'pup' and state == 3:
            state = 3
            action = 0
        else:
            action = 0
    else:
        if percept == 'antipolo' and state != 1:
            state = 1
            action = 1
        elif percept == 'antipolo' and state == 1:
            state = 1
            action = 0
        elif percept == 'cubao' and state != 2:
            state = 2
            action = 2
        elif percept == 'cubao' and state == 2:
            state = 2
            action = 0
        elif percept == 'pup' and state != 3:
            state = 3
            action = 3
        elif percept == 'pup' and state == 3:
            state = 3
            action = 0
        else:
            action = 0

    return ACTIONS[action]

def simulate_environment():
    global state
    state = None

    while True:
        percept = input("Where would you want to go? (antipolo, cubao, pup): ")
        if percept not in PERCEPTS:
            print("Invalid location. Please try again.")
            continue

        action = agent_with_memory(percept)
        print(f"Percept: {percept}, Action: {action}")

simulate_environment()