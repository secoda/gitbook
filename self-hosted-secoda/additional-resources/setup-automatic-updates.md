# Setup Automatic Updates

1. Change `VERSION` in `.env` to be the major version you want to pin. i.e

```sql
VERSION=7
```

2. Set a cronjob to run `update_secoda.sh` once a week (we do weekly deploys for onprem)

```sql
crontab -e

# Add this line to to crontab editor
0 5 * * * /home/ubuntu/<YOUR_ON_PREMISE_PATH>/update-secoda.sh
```

3. Secoda will now be updated each day at 12:00am EST to the latest version
