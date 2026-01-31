## Daily Expenses Tracker API

A Django REST Framework-based backend application for tracking daily expenses. This project supports user authentication, expense CRUD operations, and analytics reporting.


## 🚀 Features

* User registration & authentication (JWT-based)
* Add, update, delete, and view expenses
* Category-wise expense tracking
* Date-wise and monthly analytics
* Secure environment configuration using `.env`
* RESTful APIs with proper validation and error handling

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite
* **Authentication:** JWT (djangorestframework-simplejwt)
* **Environment Management:** python-dotenv
* **API Testing:** Postman 

---

## 📁 Project Folder Structure
```
Daily Expenses Tracker/
├── expenses_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   ├── admin.py
│   └── tests.py
├── expenses/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── exceptions.py
│   ├── urls.py
│   ├── apps.py
│   ├── admin.py
│   └── tests.py
├── analytics/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── apps.py
│   ├── admin.py
│   └── tests.py
├── postman/
│ └── daily_expenses_tracker.postman_collection.json
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

# 1. Clone the Repository
```
git clone https://github.com/your-username/Daily-Expenses-Tracker.git
cd Daily-Expenses-Tracker
```

# 2. Create Virtual Environment
```
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows
```

# 3. Install Dependencies
```
pip install -r requirements.txt
```

# 4. Configure Environment Variables
Create a `.env` file in the project root and add below:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

# 5. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

# 6. Run Server
```
python manage.py runserver
```

---

## 🔐 API Authentication
* Uses JWT authentication.
* Obtain token via:
```
POST /api/users/login/
```

---

## 📡 API Endpoints

# 🔐 Authentication
```
POST   /api/users/register/    -> Register new user
POST   /api/users/login/       -> Login user & get token
```

# 💰 Expenses
```
POST    /api/expenses/add/                                              -> Create new expense
PUT     /api/expenses/update/{id}/                                      -> Update expense
DELETE  /api/expenses/delete/{id}/                                      -> Delete expense
GET     /api/expenses/list/                                             -> List all expenses
GET     /api/expenses/list/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD   -> Monthly total expenses
GET     /api/expenses/list/?category=Food                               -> Category-wise breakdown
```

# 🗒️ Analytics
```
GET    /api/analytics/monthly-total/          -> Monthly expense total
GET    /api/analytics/category-breakdown/     -> Category-wise analytics
```
---

## 🧪 Testing APIs with Postman
A Postman collection is included for easy API testing.
📁 Path:
postman/daily_expenses_tracker.postman_collection

# How to use:
1. Open Postman
2. Click Import
3. Upload the JSON file
4. Set the access_token variable after login
5. Start testing all endpoints

---

## 📄 requirements.txt 
```
Django==6.0.1
djangorestframework==3.16.1
djangorestframework_simplejwt==5.5.1
python-dotenv==1.2.1
```

---

## 🔒 Security & Best Practices

* No hardcoded credentials
* Environment variables for secrets
* Proper error handling and validations
* Clean, modular code structure
---

