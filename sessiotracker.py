import sqlite3
from datetime import datetime
import subprocess
import os

kotihakemisto = os.path.expanduser("~")
tietokantakansio = os.path.join(kotihakemisto, "tietokannat")

if not os.path.exists(tietokantakansio):
    os.makedirs(tietokantakansio)

db_polku = os.path.join(tietokantakansio, "kvantifioitu.db")

def sorttaus():
    vaihtoehdot = [
                    'Opiskelu;Fysiikka;Termodynamiikka',
                    'Opiskelu',
                    'Projekti',
                    'Projekti;Opiskelutracker'
                   ]

    conn = sqlite3.connect(db_polku)
    cursor = conn.cursor()

    query = """
    SELECT kategoria 
    FROM sessiot 
    GROUP BY kategoria 
    ORDER BY MAX(id) DESC
    """
    cursor.execute(query)
    jarj = [rivi[0] for rivi in cursor.fetchall()]

    conn.close()

    puuttuvat = sorted(list(set(vaihtoehdot) - set(jarj)))

    sortattu = jarj + puuttuvat

    return sortattu

def valitse_kategoria():

    vaihtoehdot = sorttaus()

    lista_str = '", "'.join(vaihtoehdot)
    script = f'choose from list {{"{lista_str}"}} with title "Sessio data" with prompt ""'

    try:
        tulos = subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()
        return tulos if tulos != "false" else None
    except:
        return None

def ilmoitus(otsikko, viesti):
    script = f'display alert "{otsikko}" message "{viesti}" as informational buttons {{"OK"}} default button "OK" giving up after 2'
    subprocess.run(['osascript', '-e', script])

def opiskelu_toggle():

    conn = sqlite3.connect(db_polku)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessiot(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aloitus TIMESTAMP DEFAULT (datetime('now', 'localtime')),
                lopetus TIMESTAMP,
                kategoria TEXT)''')


    c.execute("SELECT id, aloitus, kategoria FROM sessiot WHERE lopetus IS NULL")
    open_session = c.fetchone()

    if open_session is None:
        valittu = valitse_kategoria()

        if valittu:
            c.execute("INSERT INTO sessiot (kategoria) VALUES (?)", (valittu,))
            ilmoitus("aloitettu ÄLÄ YLITÄ 6 TUNTIA", valittu)
        else:
            ilmoitus("Virhe","Painoit cancel")

    else:
        session_id = open_session[0]
        aloitusaika_str = open_session[1]
        kategorian_nimi = open_session[2]

        aloitus_dt = datetime.strptime(aloitusaika_str, '%Y-%m-%d %H:%M:%S')
        nyt_dt = datetime.now()
        kesto = nyt_dt - aloitus_dt
        kesto_minuutteina = kesto.total_seconds() / 60

        if   kesto_minuutteina < 3:
            c.execute("DELETE FROM sessiot WHERE id = ?", (session_id,))
            ilmoitus("Sessio hylätty", f"Liian lyhyt sessio: {int(kesto_minuutteina)}min")

        elif kesto_minuutteina > 360:
            c.execute("DELETE FROM sessiot WHERE id = ?", (session_id,))
            ilmoitus("Sessio hylätty", f"Liian pitkä sessio: {int(kesto_minuutteina)}min. Unohdit lopettaa viime session")

        else:
            c.execute('''UPDATE sessiot 
                             SET lopetus = datetime('now', 'localtime') 
                             WHERE id = ?''', (session_id,))
            ilmoitus("Sessio lopetettu",f"{kategorian_nimi} {int(kesto_minuutteina)} min")

    conn.commit()
    conn.close()

opiskelu_toggle()

