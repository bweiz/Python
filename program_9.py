def episodes_directed(dict, director):
    count = 0
    for x in dict.values():
        if x == director:
            count += 1
    print(director, "directed", count, "episodes")

stranger_things = {}
stranger_things["The Vanishing of Will Byers"] = "The Duffer Brothers"
stranger_things["The Weirdo on Maple Street"] = "The Duffer Brothers"
stranger_things["Holly, Jolly"] = "Shawn Levy"
stranger_things["The Body"] = "Shawn Levy"
stranger_things["The Flea and the Acrobat"] = "The Duffer Brothers"
stranger_things["The Monster"] = "The Duffer Brothers"
stranger_things["The Bathtub"] = "The Duffer Brothers"
stranger_things["The Upside Down"] = "The Duffer Brothers"

episodes_directed(stranger_things, "The Duffer Brothers")
episodes_directed(stranger_things, "Shawn Levy")
episodes_directed(stranger_things, "Kerri Cobb")




class Series:
    def __init__(self, title, creator, numS, numE):
        self.title = title
        self.creator = creator
        self.numS = numS
        self.numE = numE
        
    def addSeason(self):
        self.numS += 1
    
    def addEpisodes(self, num):
        self.numE += num
        
    def __str__(self):
        return str(self.title) + " has aired " + str(self.numE) + " episodes over " + str(self.numS) + " seasons"
# “Stranger Things” is the title of the series.
# “The Duffer Brothers” is the creator of the series.
# 1 is the number of seasons that the series has run.
# 8 is the number of episodes that the series contains.
stranger_things = Series("Stranger Things", "The Duffer Brothers", 1, 8)
print(stranger_things)
stranger_things.addSeason() # here comes the next season
stranger_things.addEpisodes(9) # there are now 9 more episodes
print(stranger_things)
