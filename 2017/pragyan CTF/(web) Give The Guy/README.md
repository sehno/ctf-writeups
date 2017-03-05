# Give The Guy - Web - 100 pts

## Désignation

Hacker G has a website. Can you use it to decipher this cipher text ?

Cipher text :- dobrjtuojxagbqhd

Link : http://139.59.62.216/give_the_guy/

NOTE :- Please enclose the flag in the format pragyanctf{<flag>}.
Example :- If the flag is 'HelloWorld' (without quotes) , input it as pragyanctf{HelloWorld}
If the flag is {HelloWorld}, input it as pragyanctf{HelloWorld}
If the flag is pragyanctf{HelloWorld}, input it as pragyanctf{HelloWorld}.

## Solution

On lance Firefox et on entre l'url, ce qui nous donne :  

![give_the_guy](give_the_guy.png)

La page n'est pas trouvé ! Bon, essayons autrement .  
On éxecute un `curl -v http://139.59.62.216/give_the_guy/` , et on obtient :

    *   Trying 139.59.62.216...
    * Connected to 139.59.62.216 (139.59.62.216) port 80 (#0)
    > GET /give_the_guy/ HTTP/1.1
    > Host: 139.59.62.216
    > User-Agent: curl/7.47.0
    > Accept: */*
    >
    < HTTP/1.1 404 Not Found
    < Date: Sat, 04 Mar 2017 13:41:16 GMT
    < Server: Apache/2.4.7 (Ubuntu)
    < X-Powered-By: PHP/5.5.9-1ubuntu4.20
    < Content-Length: 541
    < Content-Type: text/html
    <

    <!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html><head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252">
    <title>404 Not Found</title>
    </head><body>
    <h1>Not Found</h1>
    <p>The requested URL /index.php was not found on this server.</p>
    <hr>
    <address>Apache/2.4.7 (Ubuntu) Server at localhost Port 80</address>

    <form action='' method='POST'>
    <input type="text" maxlength='1' name="v" style='border:0px solid white; background-color: white; margin-left: 800px; margin-top: 200px;'><br>
    </form>

    </body></html>
    * Connection #0 to host 139.59.62.216 left intact

Rien de particulier . On test d'envoyer en donnée le cipher text `curl -v http://139.59.62.216/give_the_guy/ --data 'v=dobrjtuojxagbqhd` , on sait jamais !  
La même page est renvoyée à un détail prêt, cette fois un cookie est ajouté :

    < Set-Cookie: this=kQTvVPMzw

On test de flag avec la valeur du cookie mais ce n'est pas ça .  
Essayons maintenant d'envoyer une donnée à la fois .  
On fait donc `curl -v http://139.59.62.216/give_the_guy/ --data 'v=a'` .  
Cette fois le cookie a pour valeur :

    < Set-Cookie: this=tLiB

Essayons `curl -v http://139.59.62.216/give_the_guy/ --data 'v=b'` .  
Le cookie a pour valeur :

    < Set-Cookie: this=zfnzYdfiElqteIOjwyyPioi

Le cookie renvoyé n'a pas la même taille et surtout pas la même valeur.  
On va donc tester toutes les lettres et on obtient ceci :  

    v=a; len:04; this=oYJd
    v=b; len:23; this=JQKNXPUjPNXogIXZXRBOyAW
    v=c; len:16; this=zitSEsNvXtqllfLc
    v=d; len:09; this=irNXAjZCJ
    v=e; len:02; this=Sg
    v=f; len:21; this=OycnUqBruTbNbjEWQDOie
    v=g; len:14; this=sKJnKrtoXDXTRg
    v=h; len:07; this=rdcyahB
    v=i; len:26; this=SrKQwWMKnlWTEAhZjVgVffArNg
    v=j; len:19; this=LrXBUcovViLnCztcINU
    v=k; len:12; this=uEfxWNDnRiWB
    v=l; len:05; this=vcGHG
    v=m; len:24; this=pqcsVKTKYrywtMqJnIehJSiT
    v=n; len:17; this=WscjecfvlFDaPDfUY
    v=o; len:10; this=FfhIZEGGEX
    v=p; len:03; this=Hce
    v=q; len:22; this=ngIIdcZpofbqQsnrnqFIlO
    v=r; len:15; this=TQxsafqRPgBCerx
    v=s; len:08; this=xeJaTSfi
    v=t; len:01; this=u
    v=u; len:20; this=AqyFBpJfksImITkoaXQn
    v=v; len:13; this=rgXIQNfNzPaLL
    v=w; len:06; this=tzqTTs
    v=x; len:25; this=utuSLufnvnZHfhSnFJORZCmJu
    v=y; len:18; this=iiBdSuOQLnnfaDPnmT
    v=z; len:11; this=CzqKiSiGxZo

Après analyse des différents this, aucun résultat n'est trouvé .  
En regardant attentivement cette liste précédente, une idée apparaît : et si la longueur des samples correspondait à un décalage .  
On aurait donc "a" décalé de 4 caractère donc "d", puis "b" décalé de 23 caractères donc "w" etc.  
L'alphabet "abcdefghijklmnopqrstuvwxyz" devient donc "dwpibungzslexqjcvohatmfyrk" .

En reprenant le cipher text "dobrjtuojxagbqhd" et en le convertissant avec notre nouvel alphabet décalé, on obtient : areyoufromthensa .  

Le flag est donc : pragyanctf{areyoufromthensa} . 
