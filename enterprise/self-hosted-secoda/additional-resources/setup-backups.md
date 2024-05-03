# Setup Backups

To configure daily backups, create an S3 bucket (or GCP/Azure's equivalent) and run the [.](https://github.com/secoda/docker-compose)`/quick-start.sh` script. It will automatically configure your backups. Always confirm your backups are running properly, by checking if there is a backup archive in the bucket within in 24 hours.
