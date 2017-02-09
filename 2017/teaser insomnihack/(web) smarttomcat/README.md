# Smarttomcat - web - 50 pts - created by xel/grimmlin

***

*Cette épreuve n'a pas été réalisée pendant la durée du CTF, mais ayant été bloqué sur un détail (l'authentification), il est intéressant de savoir comment il a pu être validé.*

## Désignation

    Normal, regular cats are so 2000 and late, I decided to buy this allegedly smart tomcat robot
    Now the damn thing has attacked me and flew away. I can't even seem to track it down on the broken search interface... Can you help me ?
    Search interface

## Solution

Donc c'est parti, on clic sur `Search interface` et on atterrit sur cette page :

![Smarttomcat](smarttomcat.png)

Essayons de comprendre le fonctionnement .  

Nous avons deux champs en haut à droite qui correspondent à des coordonnées à entrer . En gros, on rentre des coordonnées GPS et on retrouve notre chat killer d'humains . On essaye n'importe quoi pour tester (12.5 et 4.8 par exemple) et on a un message qui nous dit que notre chat n'est pas à cet endroit .  
Il est temps de regarder la source !  
extrait :

    var request;
    $('#findcatbycoord').submit(function(event){
    event.preventDefault();
    if (request) {
        request.abort();
    }
    var cat_coords = 'http://localhost:8080/index.jsp?x=' + parseFloat($('#xcoord').val()) + '&y=' + parseFloat($('#ycoord').val());
    var $form = $(this);
    var $inputs = $form.find('input, select, button, textarea');
    $inputs.prop('disabled', true);

Plus précisemment, notre attention se porte sur ceci :

    'http://localhost:8080/index.jsp?x=' + parseFloat($('#xcoord').val()) + '&y=' + parseFloat($('#ycoord').val());

Qu'est ce qui se passe ?   
Nos coordonnées sont donc x et y et envoyées par un POST.  
Si on reprend notre test que l'on a fait plus haut, il s'est en fait passé ceci :

    u=http://localhost:8080/index.jsp?xcoord12.5&ycoord=4.8

On va maintenant chercher à modifier cette requète.  
On peut le faire de différentes façons : hackbar, burp, curl, etc .  

On essayant quelques modifications du post, on comprend rapidement qu'on a à faire à une faille de type SSRF .  
Si vous souhaitez plus de détails sur ce genre de failles => [c'est ici](http://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/) .

Après quelques recherches sur google afin de connaitre un peu mieux le fonctionnemet de tomcat, il s'avère qu'un fichier devrait pouvoir nous intéresser : il s'agit du fichier /manager/html .

On essaye donc le post suivant :

    u=http://localhost:8080/manager/html

Une erreur nous est renvoyée. En effet, le serveur demande une authentification HTTP .  
Voici donc l'authentification qu'il fallait rentrer:

    u=http://tomcat:tomcat@localhost:8080/manager/html

et on obtient ceci :

    We won't give you the manager, but you can have the flag : INS{th1s_is_re4l_w0rld_pent3st}

Flag !
