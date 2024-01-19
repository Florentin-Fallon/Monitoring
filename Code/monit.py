Un programme monit.py qui monitore certaines ressources de la machine et peut effectuer des rapports au format JSON.
Autrement dit, le programme check la valeur de certains trucs (genre combien de RAM il reste de dispo ?) et les enregistre. Il est ensuite possible d'appeler le programme en ligne de commande pour obtenir le résultat des derniers checks.
➜ Utilisation du programme monit.py

toutes les actions doivent générer au moins une ligne de logs indiquant que la commande a été appelée

monit.py check

il check la valeur de certaines ressources du système
il enregistre ces données dans un fichier dédié

🚩 cette commande doit être appelée dans le service backup.service




monit.py list

il affiche la liste des rapports qui ont été effectués



monit.py get last

il sort le dernier rapport



monit.py get avg X

il calcule les valeurs moyennes des X dernières heures



➜ Ce que votre programme doit surveiller

RAM
utilisation disque
activité du CPU
est-ce que certains ports sont ouverts et dispos en TCP

➜ Le fichier de conf

on précise la liste des ports TCP à surveiller
si la connexion TCP fonctionne, c'est que le port est actif, on retourne True
sinon False

➜ Enregistrer les données

vous enregistrerez les rapports dans le path standard pour les données des applications sous les OS Linux : /var/

il faut un sous-dossier monit

s'il n'existe pas, votre programme le crée au premier lancement


un fichier pour chaque rapport généré avec monit.py check


➜ Contenu d'un rapport

format JSON
contenu

l'heure et la date où le check a été effectué, dans un format standard
un ID unique pour chaque check
toutes les valeurs récoltées (RAM, etc)