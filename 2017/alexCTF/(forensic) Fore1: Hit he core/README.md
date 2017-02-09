# Fore1: Hit the core - forensic - 50pts

## Désignation

    Fore1: Hit the core
    50

    fore1.core

## Solution

On télécharge le fichier `fore1.core` .  
Ne sachant pas à quel type de fichier nous avons à faire, nous faisons un `file` .  
Voici la réponse :

    core.1719: ELF 64-bit LSB core file x86-64, version 1 (SYSV), SVR4-style, from 'mutt', real uid: 0, effective uid: 0, real gid: 0, effective gid: 0, execfn: '/usr/bin/mutt', platform: 'x86_64'

On continue en essayant un `strings` pour voir si on peut trouver une chaine de caractères intéressante .  
Ayant toujours à l'esprit que le flag que nous cherchons est de type ALEXCTF{flag}, une chaine de caractère attire notre attention à cause des parenthèses ouvrante et fermante:

    cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}

En ouvrant bien les yeux, on s'aperçoit rapidement qu'il y a 7 lettres en majuscules avant la paranthèses : ALEXCTF . C'est un bon début !  
On continue à l'intérieur des parenthèses, ce qui nous donne : KPHD . On aurait donc ALEXCTF{KPHD} ... ce qui n'est pas le flag!  
En s'intéressant au positionnement des lettres ALEXCTF avant les parenthèses, on se rend comptes qu'il y a 4 caractères entre chaques lettres. Essayons de reproduire ceci à l'interieur des parenthèses, ce qui nous donne :  
ALEXCTF{K33P_7H3_g00D_w0rk_up}

Flag !
