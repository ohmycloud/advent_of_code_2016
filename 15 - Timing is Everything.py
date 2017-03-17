import re

with open('./sources/15 - Timing is Everything.txt', 'r') as infile:
    instructions = infile.read().split('\n')

discs = []
for i, line in enumerate(instructions, 1):
    settings = re.search(r'(\d+) positions; .+ (\d+)', line)
    slots = int(settings.group(1))
    position = int(settings.group(2)) + i
    discs.append((slots, position))


def wait_a_sec(discs):
    time = 0
    while True:
        state = [(position+time)%slot for (slot, position) in discs]
        if sum(state) == 0:
            return time
        time += 1

first = wait_a_sec(discs)

# a new disc with 11 positions and starting at position 0 has appeared
# exactly one second below the previously-bottom disc
discs.append((11, 0+7))
second = wait_a_sec(discs)

print("What a nice arrangement of rotating discs!")
print("I should wait {} seconds for the perfect arrangement.".format(first))
print("That's only {} hours! I have plenty of time.".format(first//3600))
print("....")
print("A new disc? Let's do this all over again.")
print("Waiting and waiting and waiting for {} seconds.".format(second))
print("That's {} days! Ain't nobody got time fo' dat!".format(second//86400))
