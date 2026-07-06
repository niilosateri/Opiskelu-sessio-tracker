# Opiskelu-sessio-tracker
Tallentaa opiskelusessiot tietokantaan sisältäen aiheen, aloitusajan ja lopetusajan. 
Toimii Apple Automatorin avulla, jolloin session voi aloittaa avaamalla valikon painamalla aihetta ja valitsemalla ok. Sessio päättyy heti kun seuraavan kerran avaa valikon.


<img width="465" height="516" alt="Näyttökuva 2026-07-06 kello 12 24 33" src="https://github.com/user-attachments/assets/80e1be1e-7771-4a32-9746-a318afbe9c23" />




Aiheet voi nimetä tyyliin Opiskelu; fysiikka; termodynamiikka, jotta myöhemmin on helppo erottaa sessiot niiden aiheen mukaan, sekä alakategoriat, että yläkategoriat.

Koodi järjestää automatorin valikkoon aiheet siinä järjestyksessä, että ylimpänä on viimeisimpänä tietokantaan tallennetun session aihe.

Mikäli sessio on alle 3min tai yli 6 tuntia se automaattisesti poistaa session, estääkseen vahingossaa päällee jääneet sessiot sekä liian lyhyet sessiot

Kun sessiot tallentuu tietokantaa se näyttää tältä:


<img width="577" height="897" alt="Näyttökuva 2026-07-06 kello 12 27 15" src="https://github.com/user-attachments/assets/ea10e58b-4b65-4150-80dd-0f57f8799315" />
