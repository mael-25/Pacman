import json




class Highscore():
    def __init__(self, txt="highscores.json") -> None:
        self.highscoresfile = txt

    def read(self, txt="highscores.json", debug=False):
        f = open(txt)
        self.highscores = json.load(f)
        if debug: print(f, self.highscores)
        return self.highscores.copy()

    def convertLstToJson(self, debug=False):  
        dictionary = dict()
        for x in range(len(self.highscoreslst)):
            dictionary[str(x+1)] = {"score":self.highscoreslst[x][0], "name":self.highscoreslst[x][2]}

        self.highscores = dictionary

        if debug: print(self.highscores)
        f = open("highscores.json", "w")
        json.dump(self.highscores, f, indent=4)
        f.close()

    def convertJsonToLst(self, debug=False):##Completed
        lst = list()
        for x in range(len(self.highscores)):
            lst.append((self.highscores[str(x+1)]["score"], 10-x, self.highscores[str(x+1)]["name"])) 
        
        self.highscoreslst = lst
        if debug: print(self.highscoreslst)

    def load_score(self):  ##Completed
        self.read(debug=False)
        self.convertJsonToLst(debug=False)


    def findScore(self, pos):
        return self.highscores[str(pos)]["score"]

    def findYourRank(self, score, name="Robert"):  ##Completed
        highscores2 = self.highscoreslst.copy()
        highscores2.append((score, 0, name))
        highscores2.sort(reverse=True)
        rank = highscores2.index((score, 0, name))
        return rank+1


    def editScores(self, score, name, debug=False):
        highscores2 = self.highscoreslst.copy()
        highscores2.append((score, 0, name))
        highscores2.sort(reverse=True)
        if debug:print("The tenth person+score is",highscores2[10])
        del highscores2[10] 
        self.highscoreslst = highscores2
               
    def edit(self, current_score, current_name):
        if current_score > self.findScore(10):
            pos = self.findYourRank(current_score)
            self.editScores(current_score, current_name)
            self.convertLstToJson()

            f = open("highscores.json", "w")
            json.dump(self.highscores, f, indent=4)
            f.close()

        