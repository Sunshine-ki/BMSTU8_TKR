export FLASK_APP=controller.py
flask run --host 67.205.130.22 --port 5001 >> out.log 2>> err.log &
disown