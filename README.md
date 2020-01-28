# O aplikacji
> Checklistfinder to program, który jest wykorzystywany przeze mnie w pracy. Jego głownym zadaniem to znajdowanie unikatowych numerów i sortowanie stron według klucza w pliku PDF. Program przyśpiesza oraz ułatwia moją pracę podczas układania list kontrolnych na urządzeniach. 

<p align="center">
  <img src="https://i.imgur.com/cHcoHlI.png">
</p>

# Opis problemu
> Urządzenia podczas importowania są układane losowo co utrudnia mi pracę. Gdy listy kontrolne są wydrukowane, moim zadaniem jest ułożenie odpowiednich list na urzadzenia. Podczas generowania pliku PDF z checklistami, nie jestem w stanie generować w taki sposób jak są ułożone urządzenia (są rozłożone bez jakiegokolwiek klucza).

# Działanie programu
> Program zczytuje z pliku reqlist.txt wszystkie requesty na których będzie operował, lista jest sortowana względem importu urządzeń. Następnie program analizuje PDF i sprawdza czy każdy request z reqlist.txt zgadza się z tym w PDF. Gdy program stwierdzi, że wszystko działa przechodzi do sortowania. Powstaje nowy plik PDF, do którego są dodawane strony zaczerpniete poprzednio z pliku PDF, który został wygenerowany. Strony oczywiście są posortowane w takiej kolejności jak w pliku reqlist.txt. Na samym końcu program zamyka sie, a my otrzymujemy gotowy plik PDF, który jest posortowany względem importu. Po wydrukowaniu można rozłożyć checklisty w bardzo szybki sposób nie tracąc przy tym kilku godzin na szukanie w przypadku kiedy jest ponad 100 urządzeń.

# Cele
-  stworzenie uniwersalnego systemu pod wszystkie projekty,
-  optymalizacja programu.

# Podsumowanie
> Mój projekt zlikwidował jeden z większych problemów w firmie. Otrzymałem rekomendację od menegera za stworzenie programu i przyśpieszeniu procesu drukowania list kontrolnych.