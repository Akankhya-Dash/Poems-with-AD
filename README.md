# 🌙 Poems With AD

A modern, minimal poetry platform where words breathe softly and stories linger. Built with Django and designed with a cinematic, editorial aesthetic.

---

## ✨ Features

### 👤 User Experience

* Secure authentication (Login / Signup)
* Write and submit original poems
* Browse poems from multiple authors
* Filter poems by mood
* Personal profile page

### 📚 Archive

* Dedicated archive page with all poems
* Editorial-style reading layout
* Mood-based filtering system

### 🛠️ Admin (Superuser Only)

* Approve or remove users (grant writer access)
* Publish / Unpublish poems
* Feature / Unfeature poems
* Full moderation dashboard

---

## 🧠 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, Tailwind CSS
* **Database:** SQLite
* **Authentication:** Django Auth System

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/Akankhya-Dash/Poems-with-AD.git
cd Poems-with-AD

### 2. Create Virtual Environment

python -m venv venv

Activate:

* Windows: venv\Scripts\activate
* Mac/Linux: source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Apply Migrations

python manage.py migrate

### 5. Create Superuser

python manage.py createsuperuser

### 6. Run Server

python manage.py runserver

---

## 🔐 Admin Access

Superusers are automatically redirected to the **Admin Dashboard**, where they can:

* Approve writers
* Moderate poem submissions
* Feature selected poems

---

## 🧩 Project Structure

Poems-with-AD/
│
├── templates/
│   ├── home.html
│   ├── archive.html
│   ├── profile.html
│   ├── admin_dashboard.html
│
├── models.py
├── views.py
├── urls.py
├── static/
└── manage.py

---

## 🎯 Future Improvements

* ❤️ Like & save poems
* 🔍 Advanced search (author, tags)
* 📱 Better mobile responsiveness
* 🌐 Deployment (Render / Railway)

---

## 💫 Author

**Akankhya Dash**
GitHub: https://github.com/Akankhya-Dash
LinkedIn: https://www.linkedin.com/in/akankhya-dash-b370ba240

---

## 🌌 Vision

A quiet corner of the internet where poetry doesn’t compete — it simply exists, gently waiting to be discovered.
