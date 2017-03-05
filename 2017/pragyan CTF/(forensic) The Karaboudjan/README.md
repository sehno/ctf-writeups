# The Karaboudjan - Forensics - 150 pts

## Désignation

Captain Haddock is on one of his ship sailing journeys when he gets stranded off the coast of North Korea . He finds shelter off a used nuke and decides to use the seashells to engrave a message on a piece of paper . Decrypt the message and save Captain Haddock.

->-.>-.---.-->-.>.>+.-->--..++++.  
.+++.  
.->-.->-.++++++++++.+>+++.++.-[->+++<]>+.+++++.++++++++++..++++[->+++<]>.--.->--.>.

NOTE :- Please enclose the flag in the format pragyanctf{<flag>}.

Example :- If the flag is 'HelloWorld' (without quotes) , input it as pragyanctf{HelloWorld}
If the flag is {HelloWorld}, input it as pragyanctf{HelloWorld}
If the flag is pragyanctf{HelloWorld}, input it as pragyanctf{HelloWorld}.

clue.zip

90d22c3a959a914dc7b4dea981623ff4

## Solution

On a donc ceci à déchiffrer :  

    ->-.>-.---.-->-.>.>+.-->--..++++.  
    .+++.  
    .->-.->-.++++++++++.+>+++.++.-[->+++<]>+.+++++.++++++++++..++++[->+++<]>.--.->--.>.

On reconnait que c'est un "Brainfuck", mais le résultat nous retourne des caractères bizarres...  
On a également un fichier `clue.zip` . A l'intérieur, on trouve un fichier `clue.pcap` .  
On tente l'extraction, mais celui-ci est protégé par un mot de passe .  
Essayons de le cracker !  
On récupère le hash en faisant : `zip2john clue.zip > hash.txt` .  
Ensuite on lance john . Après quelques tentatives sans résultats avec des listes de passwords, on finit par lancer un brute force : `john hash.txt` puis on fait un `--show` pour l'afficher et obtient :

    clue.zip:dissect:::::clue.zip

    1 password hash cracked, 0 left

On extrait le fichier `clue.pcap` avec le password `dissect` .  
Un `strings clue.pcap` nous affiche :

    $JACKPOT$theflagis-{5n00p_d099}

Le flag est donc : pragyanctf{5n00p_d099} .
