from tkinter import *
from tkinter.ttk import *

import clipboard


def clicked():
    eingabe = txtURL.get()

    startSession = eingabe.find(sessionStringAnker)
    startSession += len(sessionStringAnker)

    startUser = eingabe.find(userStringAnker)
    startUser += len(userStringAnker)

    startPortal = eingabe.find(portalStringAnker)

    sessionID = eingabe[startSession: (startUser - len(userStringAnker))]
    userID = eingabe[startUser: startPortal]

    txtStgLength = len(txtStg.get())
    txtStgString = txtStg.get()
    txtStgString = txtStgString[txtStgLength-2:txtStgLength]

    if len(sessionID) != 50:
        messagebox.showinfo('Warnung', 'Session unstimmig')
        return

    if len(userID) != 11:
        messagebox.showinfo('Warnung', 'ID unstimmig')
        return

    if len(txtStgString) != 2:
        messagebox.showinfo('Warnung', 'Studiengang unstimmig')
        return

    if len(txtPruefNR.get()) != 3:
        messagebox.showinfo('Warnung', 'Pruefungsnummer unstimmig')
        return

    lblSessionEingabe.configure(text=sessionID)
    lblIDEingabe.configure(text=userID)

    notenSpiegelURL = "https://www3.primuss.de/cgi-bin/pg_Notenbekanntgabe/nsajax.pl?Language=de" \
                      + sessionStringAnker + sessionID \
                      + userStringAnker + userID \
                      + "&FH=fhm&Stg=" + txtStgString \
                      + "&Ancode=" + txtPruefNR.get() \
                      + "&Aaspf=" + combo_stg.get()

    clipboard.copy(notenSpiegelURL)


stg_list = ["Advanced Design - Master - DS",
            "Advanced Nursing Practice - Master - PF",
            "Allgemeiner Ingenieurbau - Master - BI",
            "Allgemeinwissenschaften (Fakultät 13) - kein Abschluss - AW",
            "Angewandte Forschung in der Sozialen Arbeit - Master - SF",
            "Angewandte Geodäsie und Geoinformatik - Bachelor - GD",
            "Applied Research in Engineering Sciences - Master - RS",
            "Architektur - Bachelor - AR",
            "Architektur - Master - AR",
            "Augenoptik/Optometrie - Bachelor - AO",
            "Bauingenieurwesen - Bachelor - BI",
            "Bauingenieurwesen - Master - BN",
            "Betriebliche Steuerlehre - Master - BS",
            "Betriebswirtschaft - Bachelor - BW",
            "Betriebswirtschaft - Master - BW",
            "Betriebswirtschaftslehre und Unternehmensführung - Bachelor - UB",
            "Bildung und Erziehung im Kindesalter-BEKI - Bachelor - SK",
            "Bioingenieurwesen - Bachelor - BO",
            "Chemische Technik - Bachelor - CH",
            "Computational Engineering - Master - TB",
            "Courses in English - Zertifikat - CE",
            "Data Science  - DC",
            "Design - Bachelor - DS",
            "Diagnostik, Beratung und Intervention - Master - SD",
            "Druck- und Medientechnik - Bachelor - DR",
            "Elektrotechnik - Elektromobilität - Bachelor - EM",
            "Elektrotechnik - Master - EL",
            "Elektrotechnik und Informationstechnik - Bachelor - EI",
            "Energie- und Gebäudetechnik - Bachelor - VS",
            "Entrepreneurship and Digital Transformation - Master - DT",
            "Fahrzeugmechatronik - Master - FE",
            "Fahrzeugtechnik - Bachelor - FA",
            "Fahrzeugtechnik - Master - FA",
            "Gebäudetechnik - Master - GT",
            "Gemeinwesenentwicklung, Quartiersmanagement und Lokale Ökonomie - Master - GW",
            "Geoinformatik und Navigation - Bachelor - GN",
            "Geoinformatik und Satellitenpositionierung - Bachelor - GI",
            "Geomatik - Master - GO",
            "Geotelematik und Navigation - Bachelor - GO",
            "Gesellschaftlicher Wandel und Teilhabe - Master - GE",
            "Gründung eines eigenen Start-ups - Zertifikat - GS",
            "Hospitality Management - Master - TH",
            "Informatik - Bachelor - IF",
            "Informatik - Master - IG",
            "Interkulturelle Kommunikation und Kooperation - Master - IK",
            "Interkulturelle Kommunikation und Kooperation - Zertifikat - IK",
            "Internationales Projektmanagement - Bachelor - PI",
            "IT-Sicherheit - Master - IT",
            "Kartographie|Geomedientechnik - Bachelor - KG",
            "Luft- und Raumfahrttechnik - Bachelor - LR",
            "Luft- und Raumfahrttechnik - Master - LR",
            "Management Sozialer Innovationen - Bachelor - SI",
            "Maschinenbau - Bachelor - MB",
            "Maschinenbau - Diplom (FH) - MB",
            "Maschinenbau - Master - MB",
            "MBA Management  - MS",
            "Mechatronik/Feinwerktechnik - Bachelor - MF",
            "Mechatronik/Feinwerktechnik - Master - MF",
            "Mechatronik/Feinwerktechnik (Teilzeitstudium) - Bachelor - MT",
            "Mental Health (Psychische Gesundheit) - Master - SY",
            "Mikro- und Nanotechnik - Master - MN",
            "Paper Technology (konsekutiv) - Master - PK",
            "Paper Technology (Weiterbildung) - Master - PW",
            "Papier- und Verpackungstechnik - Bachelor - VF",
            "Pflege - Bachelor - PF",
            "Photonik - Master - PO",
            "Physikalische Technik - Bachelor - PH",
            "Printmedien, Technologie und Management - Master - PR",
            "Produktion und Automatisierung - Bachelor - PN",
            "Produktion und Automatisierung (international) - Bachelor - PA",
            "Produktion und Automatisierung (international) - Master - PA",
            "Psychotherapie mit Schwerpunkt Verhaltenstherapie - Master - PY",
            "Regenerative Energien - Elektrotechnik - Bachelor - RE",
            "Scientific Computing - Bachelor - IC",
            "Sonderstudium - Bachelor - ZA",
            "Soziale Arbeit - Bachelor - SW",
            "Soziale Arbeit BASA-Online - Bachelor - SB",
            "Soziale Arbeit (Teilzeitstudium) - Bachelor - SR",
            "Sozialmanagement - Master - SO",
            "Stochastic Engineering in Business and Finance - Master - IS",
            "Systems Engineering - Master - SM",
            "Technische Redaktion und Kommunikation - Bachelor - TN",
            "Technische/r Redakteur/in - Zertifikat - TK",
            "Tourismus-Management - Bachelor - TR",
            "Tourismus-Management - Master - TR",
            "Verpackungstechnik - Master - VF",
            "Verpackungstechnik und Verfahrenstechnik Papier - Bachelor - VV",
            "Wirtschaftsinformatik - Bachelor - IB",
            "Wirtschaftsinformatik - Master - IN",
            "Wirtschaftsingenieurwesen Automobilindustrie - Bachelor - AU",
            "Wirtschaftsingenieurwesen - Bachelor - WI",
            "Wirtschaftsingenieurwesen (konsekutiv) - Master - WI",
            "Wirtschaftsingenieurwesen Logistik - Bachelor - LM",
            "Wirtschaftsingenieurwesen (Weiterbildung) - Master - WW"]

sessionStringAnker = "&Session="
userStringAnker = "&User="
portalStringAnker = "&Portal"


window = Tk()
window.title("FHM Notenspiegel Tool v1.2")
window.geometry('700x200')


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
lblSessionEingabe = Label(window, width=90, text="Session")
lblSessionEingabe.grid(column=1, row=5)

lblIDEingabe = Label(window, width=90, text="ID")
lblIDEingabe.grid(column=1, row=6)

# Eingabe der Daten
txtURL = Entry(window, width=90)  # URL
txtURL.grid(column=1, row=0)

txtStg = Combobox(window, width=86)  # Stg
txtStg['values'] = stg_list
txtStg.grid(column=1, row=2)

txtPruefNR = Entry(window, width=90)  # Pruefungsnummer
txtPruefNR.grid(column=1, row=3)

combo_stg = Combobox(window, width=86)  # Studiengang also B/M
combo_stg['values'] = (" ", "B", "M")
combo_stg.current(0)  # set the selected item
combo_stg.grid(column=1, row=4)

btn = Button(window, text=" URL in Zwischenablage ", command=clicked)
btn.grid(column=0, row=7)

window.mainloop()
