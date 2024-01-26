# Moniteur de Ressources (monit.py)

## Installation

1. **Téléchargement :** Clonez ce dépôt.

    ```bash
    git clone https://github.com/Florentin-Fallon/Monitoring.git
    ```

2. **Déplacement :** Placez le fichier `monit.py` dans un répertoire de votre choix.

    ```bash
    mv monit.py /chemin/vers/votre/dossier/
    ```

3. **Permissions d'exécution :** Assurez-vous que le fichier est exécutable.

    ```bash
    chmod +x /chemin/vers/votre/dossier/monit.py
    ```

4. **Ajout au PATH (optionnel) :** Pour exécuter le script de n'importe où, ajoutez le répertoire à votre PATH.

    ```bash
    echo 'export PATH=$PATH:/chemin/vers/votre/dossier/' >> ~/.bashrc
    source ~/.bashrc
    ```

## Configuration

Le fichier de configuration `config.json` peut contenir une liste de ports TCP à surveiller.

    ```json
    {
    "tcp_ports": [80, 443, 22]
    }
    ```

    **Note** : Assurez-vous d'avoir les permissions nécessaires pour exécuter les commandes et accéder aux répertoires et fichiers spécifiés dans le script. En cas d'erreur de permission, vous pouvez utiliser **sudo** pour exécuter le script avec des privilèges élevés.


## Usage

1. **Lancement du Service :** Pour lancer le service Monit Backup, utilisez la commande suivante dans le terminal :

    ```bash
    sudo systemctl start backup.service
    ```

2. **Assurez-vous que le service a démarré avec succès en vérifiant son statut :**

    ```bash
    sudo systemctl status backup.service
    ```

    **Note :** Cette commande affichera des informations détaillées sur l'état actuel du service. Si le service a démarré correctement, vous devriez voir une ligne indiquant "Active: active (running)".


## Journal des Messages


1. **Afficher tous les messages du journal pour le service Monit Backup :**

    ```bash
    sudo journalctl -u backup.service
    ```

2. **Afficher les derniers messages du journal en temps réel :**

    ```bash
    sudo journalctl -u backup.service -f
    ```

    Ces commandes vous permettent de consulter les messages liés au service Monit Backup dans le journal système.

### Vérification des ressources

1. **Pour vérifier les ressources du système, utilisez la commande suivante dans votre terminal :**

    ```bash
    sudo python3 ~/bin/monit.py check
    ```

