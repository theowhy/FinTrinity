from re import sub, findall
from json import dumps


class Game:
    def __init__(self):
        self.id = ""
        self.title = ""
        self.path = ""
        self.image = ""

    def set_id(self, game_id):
        self.id = game_id

    def set_path(self, path):
        self.path = f"{path}/{self.id}"
        self.image = f"{self.path}/sce_sys/icon0.png"
        self.set_title()

    def set_title(self):
        with open(f'{self.path}/sce_sys/param.sfo', encoding="UTF-8", errors="ignore") as fp:
            clean = sub(".u[0-9a-f]{4}", "", dumps(fp.read()))
            self.title = findall("([A-Za-z -]{5,})", clean)[-1]


game = Game()
game.path = r"C:\Users\bamhm\Documents\PS Vita\PGAME\5a600646483f8d6d\NPUG80318"
game.set_title()