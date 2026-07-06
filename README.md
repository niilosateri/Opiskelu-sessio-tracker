# Opiskelu-sessio-tracker
Tallentaa opiskelusessiot tietokantaan sisältäen aiheen, aloitusajan ja lopetusajan. 
Toimii Apple Automatorin avulla, jolloin session voi aloittaa avaamalla valikon painamalla aihetta ja valitsemalla ok. Sessio päättyy heti kun seuraavan kerran avaa valikon.

Aiheet voi nimetä tyyliin Opiskelu; fysiikka; termodynamiikka, jotta myöhemmin on helppo erottaa sessiot niiden aiheen mukaan, sekä alakategoriat, että yläkategoriat.

Koodi järjestää automatorin valikkoon aiheet siinä järjestyksessä, että ylimpänä on viimeisimpänä tietokantaan tallennetun session aihe.

Mikäli sessio on alle 3min tai yli 6 tuntia se automaattisesti poistaa session, estääkseen vahingossaa päällee jääneet sessiot sekä liian lyhyet sessiot
