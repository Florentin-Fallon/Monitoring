# Voici le rendu du projet Monitoring ou j'ai bien galérer :)

## Voici la commande pour le lancement :

```bash
sudo systemctl start backup.service
```

## Le status du service backup.service:

```bash
[florentinfallon@TPLinux-TP1 ~]$ sudo systemctl status backup.service
● backup.service - Monit Backup Service
     Loaded: loaded (/etc/systemd/system/backup.service; disabled; preset: disabled)
     Active: activating (auto-restart) since Fri 2024-01-26 11:33:23 CET; 6s ago
    Process: 2344 ExecStart=/usr/bin/python3 /home/florentinfallon/bin/monit.py check (code=exited, status=0/SUCCESS)
    Process: 2345 ExecStartPost=/bin/sh -c /usr/bin/python3 /home/florentinfallon/bin/monit.py check >> '/var/monit/monit_report.json' 2>&1 (code=exited, status=0/SUCCESS)
   Main PID: 2344 (code=exited, status=0/SUCCESS)
        CPU: 81ms

Jan 26 11:33:23 TPLinux-TP1 systemd[1]: backup.service: Deactivated successfully.
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: cpu_usage: 14.885714285714286
Jan 26 11:33:23 TPLinux-TP1 systemd[1]: Started Monit Backup Service.

```

## Voici la commande pour voir les messages du journal backup :

```
sudo journalctl -u backup.service
```

## Le résultat pour le journal du backup.service :

```bash
[florentinfallon@TPLinux-TP1 ~]$ sudo journalctl -xeu backup.service
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263246.968635.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263246.971192.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263307.242476.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263307.242475.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263367.475024.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263367.476704.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263427.728986.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263487.972206.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263487.973143.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263548.234948.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263548.23495.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263608.478258.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263608.478524.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263817.030354.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263860.171533.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706263947.996207.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706264180.645788.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706264220.831539.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706264248.612517.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: - report_1706265203.765202.json
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: Last report:
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: id: 1706265203.765202
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: date: 2024-01-26 11:33:23.765206
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: ram_usage: 13.4
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: disk_usage: 14.7
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: cpu_usage: 100.0
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: open_ports: []
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: Averages for the last 24 hours:
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: ram_usage: 13.162500000000009
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: disk_usage: 14.700000000000014
Jan 26 11:33:23 TPLinux-TP1 systemd[1]: backup.service: Deactivated successfully.
░░ Subject: Unit succeeded
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ The unit backup.service has successfully entered the 'dead' state.
Jan 26 11:33:23 TPLinux-TP1 python3[2344]: cpu_usage: 14.885714285714286
Jan 26 11:33:23 TPLinux-TP1 systemd[1]: Started Monit Backup Service.
░░ Subject: A start job for unit backup.service has finished successfully
░░ Defined-By: systemd
░░ Support: https://access.redhat.com/support
░░ 
░░ A start job for unit backup.service has finished successfully.
░░ 
░░ The job identifier is 9511.

```

## Vérification des ressources

Pour vérifier les ressources du système, utilisez la commande suivante dans votre terminal :

```bash
sudo python3 ~/bin/monit.py check
```

## Le résultat :

```bash
[florentinfallon@TPLinux-TP1 ~]$ sudo ~/bin/monit.py check
[sudo] password for florentinfallon: 
List of reports:
- report_1706262194.540858.json
- report_1706262254.720522.json
- report_1706262254.721367.json
- report_1706262314.988336.json
- report_1706262375.220647.json
- report_1706262375.220776.json
- report_1706262435.473644.json
- report_1706262435.474559.json
- report_1706262495.72293.json
- report_1706262495.723566.json
- report_1706262555.971235.json
- report_1706262555.971786.json
- report_1706262610.1694.json
- report_1706262616.226498.json
- report_1706262616.227119.json
- report_1706262676.472489.json
- report_1706262676.473231.json
- report_1706262693.212846.json
- report_1706262704.892641.json
- report_1706262704.893759.json
- report_1706262764.984638.json
- report_1706262764.987371.json
- report_1706262825.223663.json
- report_1706262825.223664.json
- report_1706262885.471662.json
- report_1706262885.472985.json
- report_1706262945.728105.json
- report_1706262945.728107.json
- report_1706263005.9689.json
- report_1706263005.969158.json
- report_1706263066.223486.json
- report_1706263066.224162.json
- report_1706263126.486166.json
- report_1706263126.486168.json
- report_1706263186.722605.json
- report_1706263186.722607.json
- report_1706263246.968635.json
- report_1706263246.971192.json
- report_1706263307.242476.json
- report_1706263307.242475.json
- report_1706263367.475024.json
- report_1706263367.476704.json
- report_1706263427.728986.json
- report_1706263487.972206.json
- report_1706263487.973143.json
- report_1706263548.234948.json
- report_1706263548.23495.json
- report_1706263608.478258.json
- report_1706263608.478524.json
- report_1706263817.030354.json
- report_1706263860.171533.json
- report_1706263947.996207.json
- report_1706264180.645788.json
- report_1706264220.831539.json
- report_1706264248.612517.json
- report_1706265203.765202.json
- report_1706265203.765843.json
- report_1706265263.980486.json
- report_1706265263.980518.json
- report_1706265324.241431.json
- report_1706265324.241434.json
- report_1706265384.472409.json
- report_1706265384.473026.json
- report_1706265444.747904.json
- report_1706265504.957928.json
- report_1706265504.958869.json
- report_1706265565.221248.json
- report_1706265565.221493.json
- report_1706265603.772901.json

Last report:
id: 1706265603.772901
date: 2024-01-26 11:40:03.772905
ram_usage: 13.2
disk_usage: 14.7
cpu_usage: 0.0
open_ports: []

Averages for the last 24 hours:
ram_usage: 13.194202898550726
disk_usage: 14.700000000000019
cpu_usage: 15.946376811594206

```