import csv
players = [["name", "runs", "wickets"],
           ["Maxwell", 45, 12],
           ["Virat", 120, 2],
           ["AB", 130, 5],
           ["Bumrah", 10, 55]]
def seperate_underperformers(input_file, output_file):
    try:
        with open(input_file, mode="r", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
    except FileNotFoundError:
        print(f"{input_file} not found! Creating it with sample data.")
        with open(input_file, mode="w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(players)
        data = players[:]
    header = data[0]
    rows = data[1:]
    underperformed = [row for row in rows if int(row[1]) < 50 and int(row[2]) <20]
    with open(output_file, mode="w", newline="") as f2:
        writer = csv.writer(f2)
        writer.writerow(header)
        writer.writerows(underperformed)
    print(f"Underperformed players written to {output_file}")
    ch = input('would you like to view the underperformers (y/n)? ')
    if ch.lower() in ['yes', 'y']:
        with open(output_file, 'r') as f3:
            reader = csv.reader(f3)
            data = list(reader)
            for player in data:
                print(player)
    else:
        print('Great! All done.')
seperate_underperformers("playersatistics.csv", "underperformed_player.csv")
