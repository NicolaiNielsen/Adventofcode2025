def parse_instructions_from_file(path):
    with open(path, "r") as f:
        text = f.read()
    return parse_instructions(text)

def parse_instructions(text):
    instructions = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        turn = line[0]          # 'R' or 'L'
        distance = int(line[1:])  # the number following it
        instructions.append((turn, distance))
    return instructions

def find_code(instructions):
    current_dial = 50
    final_answer = 0
    
    for dir, ticks in instructions:
        if dir == "L":
            current_dial = (current_dial - ticks) % 100
        elif dir == "R":
            current_dial = (current_dial + ticks) % 100
        if current_dial == 0:
            final_answer += 1

    return final_answer 

def find_code2(instructions):
    current_dial = 50
    final_answer = 0
    
    for dir, ticks in instructions:
        for _ in range(ticks):
            if dir == "L":
                current_dial -= 1
                if current_dial == -1:
                    current_dial = 99

            elif dir == "R":
                current_dial += 1
                if current_dial == 100:
                    current_dial = 0
        
            if current_dial == 0:
                final_answer += 1

    return final_answer 



instruction = parse_instructions_from_file("day1/day1input.txt")
print(find_code2(instruction))


