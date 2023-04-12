cd /root/masm && git pull
python3 manage.py collectstatic --noinput
mysql -u masm -p46uR81KepdO7NXq7ZFu2d masm < data.sql
systemctl restart gunicorn

