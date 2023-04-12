cd /root/masm
PULL=$(git pull)

if [ "$PULL" = "Bereits aktuell." ]; then
    echo "Already up-to-date"
else
    python3 manage.py collectstatic --noinput
    mysql -u masm -p46uR81KepdO7NXq7ZFu2d masm < data.sql
    systemctl restart gunicorn
fi
