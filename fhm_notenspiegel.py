from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import clipboard

sessionStringAnker = "&Session="
userStringAnker = "&User="
portalStringAnker = "&Portal"

window = Tk()
window.title("FHM Notenspiegel Tool")
window.geometry('500x200')

# Labels fuer alle Sachen
lbltxtURL = Label(window, text="URL: ")
lbltxtURL.grid(column=0, row=0)

lbl = Label(window, text="Studiengang: ")
lbl.grid(column=0, row=2)

lbl = Label(window, text="Prüfung: ")
lbl.grid(column=0, row=3)

lbl = Label(window, text="B/M: ")
lbl.grid(column=0, row=4)

lbl = Label(window, text="Session: ")
lbl.grid(column=0, row=5)

lbl = Label(window, text="ID: ")
lbl.grid(column=0, row=6)

# Labels die Daten zeigen
lblSessionEingabe = Label(window, width=50, text="Session")
lblSessionEingabe.grid(column=1, row=5)

lblIDEingabe = Label(window, width=50, text="ID")
lblIDEingabe.grid(column=1, row=6)

# Eingabe der Daten
txtURL = Entry(window, width=50)  # URL
txtURL.grid(column=1, row=0)

txtStg = Entry(window, width=50)  # Stg
txtStg.grid(column=1, row=2)

txtPruefNR = Entry(window, width=50)  # Pruefungsnummer
txtPruefNR.grid(column=1, row=3)

combo = Combobox(window, width=46)  # Studiengang also B/M
combo['values'] = ("B", "M")
combo.current(0)  # set the selected item
combo.grid(column=1, row=4)


def clicked():
    eingabe = txtURL.get()

    startSession = eingabe.find(sessionStringAnker)
    startSession += len(sessionStringAnker)

    startUser = eingabe.find(userStringAnker)
    startUser += len(userStringAnker)

    startPortal = eingabe.find(portalStringAnker)

    sessionID = eingabe[startSession: (startUser - len(userStringAnker))]
    userID = eingabe[startUser: startPortal]

    if len(sessionID) != 50:
        messagebox.showinfo('Warnung', 'Session unstimmig')
        return

    if len(userID) != 11:
        messagebox.showinfo('Warnung', 'ID unstimmig')
        return

    if len(txtStg.get()) != 2:
        messagebox.showinfo('Warnung', 'Stuediengang unstimmig')
        return

    if len(txtPruefNR.get()) != 3:
        messagebox.showinfo('Warnung', 'Pruefnummer unstimmig')
        return

    lblSessionEingabe.configure(text=sessionID)
    lblIDEingabe.configure(text=userID)

    notenSpiegelURL = "https://www3.primuss.de/cgi-bin/pg_Notenbekanntgabe/nsajax.pl?Language=de" \
                      + sessionStringAnker + sessionID \
                      + userStringAnker + userID \
                      + "&FH=fhm&Stg=" + txtStg.get() \
                      + "&Ancode=" + txtPruefNR.get() \
                      + "&Aaspf=" + combo.get()

    clipboard.copy(notenSpiegelURL)


btn = Button(window, text=" URL in Zwischenablage ", command=clicked)
btn.grid(column=0, row=7)

window.mainloop()
