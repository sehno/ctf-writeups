# Comming Soon!! - Web - 150 pts

## Désignation

Coming Soon!!
175

Hello I am Zafer . Beşir puts Izzettin in to a coma and I need help to get Avatar 2 DVD . Can you help me to get it?

http://138.197.41.168/ctf1/login.html

Note: For none Turkish players; if you have any issue with language contact hatMadder on irc

hint: take carefull look at names ;)

## Solution

On clique sur le lien et on arrive à une page d'authentification :

![authentification](authentification.png)

On essaye une authentification de base :  
Username : admin '  
Password : OR 1=1 #

Ca passe ! Nous voici dans l'interface admin :

![admin](admin.png)

On a apparemment un fichier Avatar en 6 parties . En cliquant sur le premier lien, on ne voit qu'un morceau de l'image . En cliquant sur les autres liens, on peut voir qu'il s'agit de base64 .  
On récupère donc les 6 morceaux de base64, puis on les decode via le site https://www.base64decode.org/ .  
On concatène les 6 fichiers dans un dossier via la commande `cat * >> flag.jpg` ce qui nous donne :

![flag](flag.jpg)

Flag !
