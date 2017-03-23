# Petty Difference - forensic - 75pts

## Désignation

Forensics

Written by dududum561

I found two files in a secret room. They look like jumbled letters with no patterns. I mean look at it! file1 is identical to file2, right?

file1 : 4b44b334ac0ff0a281597fb66c6f78bc8f5d537e_file1.txt
file2 : d1de718973b070b1c12b78cef89d21ded505f9f0_file2.txt

## Solution

Après un rapide `file` sur les fichiers, nous avons donc deux fichiers au format `ASCII text` .
En regardant rapidement l'intérieur des fichiers, nous avons une quantité de caractères assez ressemblant .      
Cependant, l'intitulé nous aiguille en nous demandant si le premier fichier est identique au second fichier .  
Etant donné la longueur du fichier, un script écrit en python sera plus rapide.  
Dans un premier temps, la méthode sera de comparer chaque caractère un par un . Si les caractères sont identiques, le script continue, si les caractères sont différents, alors on garde le caractère du premier fichier. Quand tous les caractères sont passés, on affiche les caractères du fichier 1 .  

Ce qui donne ceci :

    }4_gn1k00l_3r3w_u0y_3cn3r3ff1d_3ht_3b_y4m_s1ht{ftcysae

Intéressant ! Nous avons donc trouvé le flag, mais à l'envers.

Voici le script final qui permet d'avoir le flag dans le bon sens :

    file1=open("4b44b334ac0ff0a281597fb66c6f78bc8f5d537e_file1.txt", "r").read()
    file2=open("d1de718973b070b1c12b78cef89d21ded505f9f0_file2.txt", "r").read()

    u=zip(file1,file2)
    flag=""
    for i,j in u:
	    if i==j:
    		continue
    	else:
    		flag=flag+i

    print flag[::-1]

Flag : easyctf{th1s_m4y_b3_th3_d1ff3r3nc3_y0u_w3r3_l00k1ng_4}
