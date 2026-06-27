# Required things to run the project

* Python
* Node.js
* Redis server
* Mailhog

# Virtual Environtment

Run the below commands to create python virtual environment

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate # Windows
source venv/bin/activate # linux
```

```bash
pip install -r requirements.txt
```

if you want to add new package then after installing run this to update requirements.txt

```bash
pip freeze > requirements.txt
```

# How to start backend

```bash
python app.py
```

# How to start celery worker

```bash
celery -A celery_app worker --loglevel=INFO \\ only for windows keep "--pool=solo"
```

# How to start celery beat

```bash
celery -A celery_app beat --loglevel=INFO
```

# How to start frontend

```bash
cd frontend
npm install
npm run dev
```