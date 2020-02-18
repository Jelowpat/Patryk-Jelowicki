#a function for creating a new funtest
def nowy_test(nazwa=""):
    licznik = 0
    if nazwa == "":
        nazwa = input("podaj nazwe testu(pliku)")+".txt"
    plik = open(nazwa, "a", encoding="utf-8")
    while True:
        a = 0
        pytanie_nowe = input("wpisz tekst swojego pytania, 'k' by zakonczyc")
        if pytanie_nowe == "k":
            if licznik > 0:
                break
            else:
                print("nie ma jeszcze żadnych pytań")
                continue
        elif len(pytanie_nowe) < 3:
            print("zadaj prawdziwe pytanie!")
            continue
        else:
            plik.write(f"{pytanie_nowe}\n")
            while a < 15:
                answer = input(f"podaj wariant {warianty[a]}) lub wcisnij 'k' jesli to wszystkie warianty")
                if answer == "k":
                    if a > 1:
                        while True:
                            poprawna = input("podaj poprawna odpowiedz")
                            if poprawna in warianty[:a] and len(poprawna) == 1:
                                plik.write(f"{poprawna}\n")
                                break
                            else:
                                print("podaj literkę poprawnej odpowiedzi")
                        break
                    else:
                        print("podaj przynajmniej 2 odpowiedzi")
                        continue
                elif len(answer) == 0:
                    print("podaj prawdziwy wariant!")
                    continue
                else:
                    plik.write(f"{warianty[a]}) {answer}\n")
                    a += 1
        licznik += 1
    plik.close()


warianty = "abcdefghijklmno"            # a string for options
chwilowa = []                           # initiating a variable for appending a list

# main program loop
while True:

    pytania = []                        # a list for questions, options and answers

    print("witaj w FUNteście")
    o_kim = input("wpisz nazwę testu(pliku) lub naciśnij 'n' by stworzyć nowy test\n")+".txt"
    if o_kim == "n.txt":
        nowy_test()
        continue
    try:
        f = open(o_kim, "r", encoding="utf-8")
        pass
    except IOError:
        nowy = input("nie ma takiego pliku, czy chciałbyś/chciałabyś stworzyć funtest o takiej nazwie? ('t')")
        if nowy == "t":
            nowy_test(nazwa=o_kim)
        continue

    f1 = f.readlines()
    for x in f1:
        if x != "":
            chwilowa.append(x.strip())
        if len(x) == 2:
            chwilowa[-1] = x[0]
            pytania.append(chwilowa)
            chwilowa = []
    f.close()

    # a loop for answering the test
    while True:
        imie = input("podaj swoje imie by zacząć\n")
        numer = 0                                   # a variable holding the number of the question
        wynik = 0                                   # a variable holding the score of the user
        zle_odpowiedzi = []                         # a list of wrong answers
        highscores = []                             # a list for highscores

        for pytanie in pytania:
            numer += 1
            for x in pytanie[:-1]:
                print(x)
            odpowiedz = input().lower()
            while odpowiedz not in warianty[:len(pytanie)-2] or len(odpowiedz) != 1:
                print("nie ma takiej odpowiedzi")
                for x in pytanie[:-1]:
                    print(x)
                odpowiedz = input().lower()
            if odpowiedz == pytanie[-1]:
                wynik += 1
            else:
                zle_odpowiedzi.append([numer, odpowiedz])

        print(f"Twój wynik to {wynik}pkt", "BRAWO!!!" if wynik/len(pytania) > 0.75 else "cienko :/")
        high = imie + "-" + str(wynik) + "\n"
        with open(f"highscores.{o_kim}", "a", encoding="utf-8") as f:
            f.write(high)

        with open(f"highscores.{o_kim}", "r+", encoding="utf-8") as f:
            f1 = f.readlines()
            for x in f1:
                name, score = x.split(sep="-")
                score = int(score)
                highscores.append([name, score])
            highscores.sort(key=lambda s: s[1], reverse=True)

        f = open(f"highscores.{o_kim}", "w")
        f.close()

        with open(f"highscores.{o_kim}", "r+", encoding="utf-8") as f:
            for x in highscores:
                f.write(f"{x[0]}-{x[1]}\n")

        while True:
            co_dalej = input("nacisnij 'z' by poznac swoje bledne odpowiedzi, 'q' zeby wyjsc z programu,"
                             " 'd' by wyswietlic dobre odpowiedzi,\n'h' by wyswietlic najwyzsze wyniki,"
                             " 'n' by sprobowac jeszcze raz, cokolwiek innego by wrócić\n")
            if co_dalej == "q":
                exit()
            elif co_dalej == 'z':
                for x in zle_odpowiedzi:
                    print(x[0], "-", x[1])
            elif co_dalej == 'd':
                for x in range(numer-1):
                    print(x+1, "-", pytania[x][-1])
            elif co_dalej == 'h':
                najdluzszy = len(highscores[0][0])
                for x in highscores:
                    dlugosc = len(x[0])
                    if dlugosc > najdluzszy:
                        najdluzszy = dlugosc
                for x in highscores:
                    dlugosc = len(x[0])
                    if dlugosc > 20:
                        x[0] = x[0][:18]+"(...)"
                        dlugosc = 23
                    print(f"{x[0]}{'-' * (23 - dlugosc)}-{x[1]}")
            else:
                break
        if co_dalej == "n":
            continue
        break
