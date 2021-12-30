import json


def read(txt="highscores.json"):
    f = open(txt)
    data = json.load(f)
    return data

class Highscore():
    def __init__(self, txt="highscores.json") -> None:
        self.highscores = read(txt)

    def findScore(self, pos):
        return self.highscores[str(pos)]["score"]

    def findMaxScore(self, score):
        pos = []
        for x in range(1, len(self.highscores)+1):
            if score < self.highscores[str(x)]["score"]:
                pos.append(x)

        m = 0
        for x in pos:
            m = max(x, m)

        return m+1

    def editScores(self, pos):
        for x in range(10-pos):
            self.highscores[str(10-(pos+x-1))] = self.highscores[str(10-(pos+x))]
               
    def edit(self, current_score, current_name):
        if current_score > self.findScore(10):
            del self.highscores["10"]
            pos = self.findMaxScore(current_score)
            self.editScores(pos)
            self.highscores[str(pos)] = {"name": current_name, "score": current_score}
            f = open("highscores.json", "w")
            json.dump(self.highscores, f, indent=4)
            f.close()

        