# Ogrewatch - Forensics - 100 pts

## Désignation

Forensics

Written by neptunia

My friend was out watching ogres when he heard a strange sound. Could you figure out what it means? ogreman

Hint : If you're having trouble with the file format, Gary Kessler might help.

fichier : 132ea90b28084ca59d251988faeecf40e4879b98_ogreman

## Solution

On lance un `strings 132ea90b28084ca59d251988faeecf40e4879b98_ogreman` .  
Un extrait est intéressant :

    0,0,Default,,0,0,0,,e\N
    1,0,Default,,0,0,0,,a\N
    2,0,Default,,0,0,0,,s\N
    3,0,Default,,0,0,0,,y\N
    4,0,Default,,0,0,0,,c\N
    Lavc55.34.1
    5,0,Default,,0,0,0,,t\N
    6,0,Default,,0,0,0,,f\N
    7,0,Default,,0,0,0,,{\N
    8,0,Default,,0,0,0,,s\N
    9,0,Default,,0,0,0,,u\N
    10,0,Default,,0,0,0,,b\N
    11,0,Default,,0,0,0,,s\N
    12,0,Default,,0,0,0,,_\N
    13,0,Default,,0,0,0,,r\N
    14,0,Default,,0,0,0,,_\N
    15,0,Default,,0,0,0,,b\N
    @_]+
    g7zp
    .ZZ"FH
    z,g{8
    16,0,Default,,0,0,0,,3\N
    17,0,Default,,0,0,0,,t\N
    18,0,Default,,0,0,0,,t\N
    19,0,Default,,0,0,0,,3\N
    20,0,Default,,0,0,0,,r\N
    21,0,Default,,0,0,0,,_\N
    22,0,Default,,0,0,0,,t\N
    23,0,Default,,0,0,0,,h\N
    24,0,Default,,0,0,0,,@\N
    25,0,Default,,0,0,0,,n\N
    26,0,Default,,0,0,0,,_\N
    27,0,Default,,0,0,0,,d\N
    28,0,Default,,0,0,0,,u\N
    29,0,Default,,0,0,0,,b\N
    30,0,Default,,0,0,0,,5\N
    31,0,Default,,0,0,0,,}\N

Et oui, tout simplement, on voit le flag : easyctf{subs_r_b3tt3r_th@n_dub5} .  

Une autre méthode consiste à extraire les sous-titres.
Il est possible de le faire avec les deux commandes suivantes (par exemple) :

    mkvmerge -i 132ea90b28084ca59d251988faeecf40e4879b98_ogreman
    mkvextract tracks 132ea90b28084ca59d251988faeecf40e4879b98_ogreman 2:soustitres.srt
