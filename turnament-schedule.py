def generate_tournament_schedule(v):
    teams = v
    schedule = []

    for r in range(1, teams):
        round_matches = []
        for x in range(1, teams):
            y = (r - x) % (teams - 1)
            if y == 0:
                y = teams - 1
            if x < y:
                round_matches.append((x, y))
            elif x == y:
                round_matches.append((x, teams))
        schedule.append(round_matches)

    return schedule

def print_schedule(schedule):
    for r, round_matches in enumerate(schedule):
        print(f"Runde/Tag {r + 1}")
        for match in round_matches:
            print(f"{match[0]} gegen {match[1]}")
        print()


# Beispiel für v = 8 (v= wie viele Teams)
v = 8
schedule = generate_tournament_schedule(v)
print_schedule(schedule)