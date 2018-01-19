# --------------------------------------
# CSCI 127, Lab 6
# October 10, 2017
# Benton Weizenegger
# --------------------------------------

# Change 1: The process_season parameters include output_file 

def process_season(output_file, season, games_played, points_earned):
    
    
    output_file.write("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned) + "\n")
    output_file.write("Possible Win-Tie-Loss Records" + "\n")
    output_file.write("-----------------------------" + "\n")
     
    for win in range(0, games_played + 1, 1):
        for tie in range(0, games_played + 1, 1):
            for loss in range(0, games_played + 1, 1):
                if ((3 * win) + tie == points_earned and win + tie + loss == games_played):
                    output_file.write(str(win) + " - ")
                    output_file.write(str(tie) + " - ")
                    output_file.write(str(loss) + "\n")
                    
    output_file.write("\n")
    
# --------------------------------------

# Change 2: The process_seasons parameters are input_file (e.g. "soccer-in.txt") and output_file (e.g. "soccer-out.txt")

def process_seasons(input_file, output_file):
    soccer_seasons = open("soccer-in.txt", "r")
    output_file = open(output_file, "w")
    S = 0
    for szn in soccer_seasons:
        szn = szn.split()
    
        S = S + 1
        GP = int(szn[0])
        PE = int(szn[1])
        process_season(output_file, S, GP, PE)
    
# --------------------------------------

# Change 3: The function process_seasons is called with "soccer-in.txt" and "soccer-out.txt" 
input_file = open("soccer-in.txt", "r")
output_file = open("soccer-out.txt", "w")

process_seasons("soccer-in.txt", "soccer-out.txt")

input_file.close()
output_file.close()






