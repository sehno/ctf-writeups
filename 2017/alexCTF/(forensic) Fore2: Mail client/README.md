# Fore2: Mail client - forensic - 100pts

## Désignation

    Fore2: Mail client
    100

    I am not sure what version of thunderbird was that...
    Have fun

    nc 195.154.53.62 2222
    core.1719

## Solution

On télécharge le fichier `core.1719` .  
Comme pour le précédent challenge, on essaye déja de savoir quel est le type du fichier avec un `file` .  
On obtient :

    core.1719: ELF 64-bit LSB core file x86-64, version 1 (SYSV), SVR4-style, from 'mutt', real uid: 0, effective uid: 0, real gid: 0, effective gid: 0, execfn: '/usr/bin/mutt', platform: 'x86_64'

Ok, on continue donc notre investigation . En relisant la désignation de l'épreuve, on a `nc 195.154.53.62 2222` .  
En essayant de nous connecter, on a ceci :

    root@kali:~/Documents/alexctf# nc 195.154.53.62 2222
    Email: test
    Password: 1234
    Invalid Email or password

Deux choses sont donc à renseigner : l'Email (on met "test")et le Password (on met "1234").  
Allons donc trouver les bons Email et Password !  
Grâce à la commande `strings`, nous faisons ceci :

    strings core.1719 | grep mail

Rapidement on tombe sur : `alexctf@example.com` .

Trouvons maintenant le Password !  
On tente :

    strings core.1719 | grep password

Un ligne attire notre attention :

    tp_pass = "e. en kv,dvlejhgouehg;oueh fenjhqeouhfouehejbge ef"

Le password semble bizarre, mais essayons quand même de nous connecter avec ses informations . Malheureusement, on a droit à un beau `Invalid Email or password` .  
En faisant tout simplement un `strings core.1719`, aucune autre adresse mail n'est trouvée . On reste donc sur celle-ci, mais il nous faut quand même chercher un autre mot de passe.  
En relisant, toujours avec la commande `strings core.1719`, un détail attire notre attention . On trouve ces deux lignes :

    dksgkpdjg;kdj;gkje;gj;dkgv a enpginewognvln owkge  noejne
    e. en kv,dvlejhgouehg;oueh fenjhqeouhfouehejbge ef

La deuxième ligne contient les mêmes caractères que la variable `tp_pass`, et les caractères affichés au dessus y ressemblent .  
Par chance, on essaye avec le password `dksgkpdjg;kdj;gkje;gj;dkgv a enpginewognvln owkge  noejne` :

    root@kali:~/Documents/alexctf# nc 195.154.53.62 2222
    Email: alexctf@example.com
    Password: dksgkpdjg;kdj;gkje;gj;dkgv a enpginewognvln owkge  noejne
    1 new unread flag
    ALEXCTF{Mu77_Th3_CoRe}

Flag !
