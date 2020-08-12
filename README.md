# fhm_notenspiegel
Kleines Programm um den Notenspiegel-Link einer Prüfung zu bekommen. 
Folgende Infos braucht das Programm
- URL von Primuss nach dem Einloggen
- Studiengang Kürzel. Zweistellig.
  - Beispiele
    - BI = BauIngenieur Bachelor
    - MF = Mechatronik Master
    - WI = Wirtschaftsingenieur Bachelor
- Prüfungsnummer -> Aus der Anmeldung. Ist dreistellig.
- Angabe ob Bachelor oder Master

Danach auf den Button und der Link ist in der Zwischenablage.
Das Programm sollte solange gehen bis die HM iwas am URL ändert.
Mein erstes Python Programm also safe gut was zu korrigieren.

HowTo:
1. Normal in Primuss einloggen. Die URL ist dann iwas wie \
https://www3.primuss.de/cgi-bin/sesam/index.pl?FH=fhm&Session=XXXX&User=YYYYY&Portal=1 \
Die XXX stehen für random Buchstaben die der Session Key sind. Die YYY sind die Magnetkartennummer.
2. Den URL wie aus der URL Leiste in das Programm einfügen.
3. Einstellen welche Prüfungsnummer (-> Prüfungsanmeldung -> Dreistellige Nummer), Studiengangskürzel, Angabe ob Bachelor oder Master.
4. Den Button klicken und dann im selben Browser aufrufen. Da Shibbaloth (Login-Server) Cookies setzt muss es der selbe Browser wie beim Login sein.
