# Gramatika za definisanje rodoslova
###### JSD 2017

## Pokretanje modela i aplikacije
Implementacija je radjena u PyCharm Community Edition 2016.3.2 za Windows.

#### Instalacija Python-a za Windows
Za instalaciju na Windows platformi potrebno je preuzeti .exe fajl sa sajta: 
https://www.python.org/downloads/release/python-353/

Na dnu stranice su ponuđene verzije koje su dostupne. Izabrati jednu od dve opcije:
- Windows x86-64 executable installer
- Windows x86 executable installer

Verzija koja se skida zavisi od verzije operativnog sistema da li je 32-bitna ili 64-bitna verzija. Za 32-bitni operativni sistem potrebno je skinuti fajl sa x86 u nazivu, a za 64-bitni fajl sa x86-64 u nazivu.

Duplim klikom na skinuti fajl pokrenuće se instalacija i potrebno je ispratiti sledeće korake.
- Ukoliko nije čekirano, čekirati Install launcher for all users, i odabrati Customize installation.
- Na sledećem prozoru(Optional Features) čekirati Documentation, pip, tcl/tk and IDLE, Python test suite, py laucher for all users. Kliknuti Next.
- Na sledećem prozoru(Advanced Options) čekirati Install for all users, Associate files with Python, Create shortcuts for installed applications, Add Python to enviroment variables, Precompile standard library. Kliknuti Install.

#### Instalacija pip i virtuelenv alata
Za instalaciju pip alata potrebno je preuzeti skriptu get-pip.py sa sajta:
https://pip.pypa.io/en/stable/installing/

Na link get-pip.py treba pritisnuti desni klik miša->Save Link as. Kada se sačuva skripta potrebno je otvoriti Command Pompt i preći u folder gde je skripta sačcuvana. Odatle se može pokrenuti instalacija pokretanjem get-pip.py skripte sa komandom: python get-pip.py.

Za instalaciju virtualenv alata potreban je instaliran pip alat i za instalaciju treba pokrenuti komandu: pip install virtualenv.
- Otvoriti Command Pompt kao administrator.
- Ukucati python -V. Ispis u konzoli: Python 3.5.3
- Ukucati pip -V. Ispis u konzoli: pip 9.0.1 form neka putanja.
- Ukucati pip install virtualenv.

#### Instalacija PyCharm

##### Instalacija Jave

Za pokretanje PyCharmokruženja potrebno je instalirati Javu. Za instalaciju na Windows platformi treba prvo da preuzmete .exe fajl sa sajta:
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

Ponuđene su dve verzije:
- jdk-8u121-windows-i586.exe (za 32- bitnu verziju operativnog sistema)
- jdk-8u121-windows-x64.exe (za 64- bitnu verziju operativnog sistema)

Da se omogućilo skidanje, na sajtuje potrebno selektovati opciju Accept License Agreement. Duplim klikom na skinuti fajl pokreće se instalacija i potrebno je ispratiti instalacioni wizard. Instalacioni folder Jave za Windows operativne sisteme zavisi od njegove verzije (x86 ili x64) i najčešće je nalik:
- C:\Program Files\Java\jdk1.8.0_XY\
- C:\Program Files (x86)\Java\jdk1.8.0_XY\

Kad se završi instalacija potrebno je postaviti JAVA_HOME i PATH sistemsku varijablu, na sledeći način:
- Za Windows 7
1. Desni klik miša naMy Computer ikonu sa desktopa i selekcija stavke Properties.
2. Klik na Advanced karticu.

- Za Windows 10
1. Klik na Control Panel
2. Klik na System
3. Klik na Advanced System Settings

- Klik na Environment Variables dugme.
- Pod stvakom System Variables, kliknuti dugme New.
- Uneti naziv nove varijable JAVA_HOME.
- Uneti vrednost varijable kao putanje do instalacionog foldera Java Development Kit. (kao na primer C:\Program Files (x86)\Java\jdk1.8.0_XY\)
- Dugme potvrde OK.
- Izmeniti vrednost sistemske varijable Path tako da se na kraju doda vrednost %JAVA_HOME%\bin;(; je separator vrednosti unutar varijable)
- Dugme potvrde Apply Changes
- Ponovo porenuti Windows. (obavezno)

##### Instalacija PyCharm

Potrebno je skinuti odgovaraju'i fajl sa adrese:
https://www.jetbrains.com/pycharm/download/

Na toj stranici je potrebno skineti Community verziju koja je besplatna i izabereti za koji operativni sistem se skida. Za Windows se skida .exe fajl.

Kada se preuzme pycharm-community-Y.Y.Y.exe fajl, gde će Y.Y.Y biti brojevi koji prestavljaju verziju, može se odmah duplim klikomna taj fajl pokrenuti instalaciju. Potrebno je da ispratite sve korake i instaliraćee se IntelliJ na Windows-u. Nakon instalacije trebalo bi da se poajvi ikonica sa nazivom JetBrains PyCharm Community Edition sa kojom je moguće pokreneti razvojno okruženje PyCharm.

##### Inicijalna podešavanja

Kada se prvi put pokrene PyCharm razvojno okruženje potrebno je postaviti početna podešavanja. Na prvom prozoru koji se pojavi potrebno je označiti: I do not have a previous version of PyCharm or I do not want to import my settings. Kliknuti OK.

Zatim će se pojaviti novi prozor, na kojem se postavljaju početna podešavanja za najbitnije stavke.
- Keymap scheme: Default for XWin
- IDE theme: IntelliJ
- Editor colors and fonts: Default
- označiti:
1. Create desktop entry(integrate in system menu)
2. For all users
- Kliknuti OK

#### Pokretanje projekta

- Sa ovog sajta http://www.graphviz.org/download/ skinuti Stable 2.38 Windows install packages (nalazi se u Windows sekciji)
- Raspakuj arhivu u posebnom folderu.
- Dodati putanju do bin direktorijuma Graphviz-a na PATH varijablu.
- Kreirati folder virtualenviroments.
- Pokrenuti command prompt kao administrator. Ispratiti sledeće korakre:
1. Pozicionirati se iz komandne linije u folder virtualenviroments.
2. kucati: virtualenv virtualJSD
3. kucati: virtualJSD\Scripts\activate
4. kucati: pip install setuptools
5. kucati: pip install Arpeggio
6. kucati: pip install textx
7. kucati: pip install pydotplus
8. kucati: pip install jinja2
