GREY= 220,220,220
WHITE =255,255,255
class NajlepszeWyniki:
    def __init__(self, screen):
        self.screen = screen
        self.najlepsze_wyniki = []
        self.wynik = 0
        self.nazwa = ''
        self.kolor_nowego = GREY
        with open('wyniki.txt', 'r') as file:
            for line in file:
                if len(line) <2:
                    continue
                split_line = line.split()
                self.najlepsze_wyniki.append((split_line[0], int(split_line[1])))

    def ustaw_wynik(self,wynik):
        self.wynik = wynik

    def exit(self):
        self.najlepsze_wyniki.append(self.nazwa, self.wynik)
        self.najlepsze_wyniki.sort(key=lambda x:x[-1])
        if len(self.najlepsze_wyniki) > 10:
            self.najlepsze_wyniki.pop()
        lines = []
        for nazwa , wynik in self.najlepsze_wyniki:
            lines.append(f'{nazwa} {wynik}\n')
        with open ('wyniki.txt', 'w') as file:
            file.writelines(lines)


    def exit2(self):
        if self.kolor_nowego == GREY:
            self.kolor_nowego = WHITE
            return  'ok'
        else:
            self.exit()
            return 'exit'


    def przypisanie(self,key):
        if key.nazwa == 'BACKSPACE' and self.nazwa:
            self.nazwa = self.nazwa[:-1]
        elif key.nazwa[:2] == 'K_':
            self.nazwa +=key.nazwa[-1]
        elif len(key.nazwa) == 1:
            self.nazwa += key.nazwa


    def draw(self):
        lepszy_od = 0
        for i, line in enumerate(self.najlepsze_wyniki):
            nazwa, wynik = line
            if wynik < self.wynik:
                lepszy_od = i
                break
            self.screen.draw.text(f'{nazwa}', color=WHITE, fontsize=32, fontname='Tahoma',topleft=(100,100+40*i))
            self.screen.draw.text(f'{wynik}', color=WHITE, fontsize=32, fontname='Tahoma', topleft=(400, 100 + 40 * i))

        if not self.nazwa:
            self.screen.draw.text(f'_', color=self.kolor_nowego, fontsize=32, fontname='Tahoma', topleft=(400, 100 + 40 * lepszy_od))
        else:
            self.screen.draw.text(f'{self.nazwa}', color=self.kolor_nowego, fontsize=32, fontname='Tahoma',
                                  topleft=(400, 100 + 40 * lepszy_od))
        self.screen.draw.text(f'{self.wynik}', color=self.kolor_nowego, fontsize=32, fontname='Tahoma',
                              topleft=(400, 100 + 40 * lepszy_od))

        for i, line in enumerate(self.najlepsze_wyniki[lepszy_od:]):
            nazwa, wynik = line
            self.screen.draw.text(f'{nazwa}', color=WHITE, fontsize=32, fontname='Tahoma', topleft=(100, 100 + 40 * (i+lepszy_od+1)))
            self.screen.draw.text(f'{wynik}', color=WHITE, fontsize=32, fontname='Tahoma', topleft=(400, 100 + 40 * (i+lepszy_od+1)))
