# Naziv projekta(izmeniti)
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
