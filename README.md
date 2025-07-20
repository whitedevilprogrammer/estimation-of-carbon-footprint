# 🌱 Estimation of Carbon Footprint using Django

This project is a **Django-based web application** that allows users to estimate their **carbon footprint** based on personal habits such as transportation, electricity usage, and lifestyle choices. It helps raise awareness of environmental impact and provides actionable insights to reduce carbon emissions.

---

### 🎥 Demo Video 1 - User Dashboard
[Click to watch](https://drive.google.com/file/d/112oxG5AahfOLndzVCSQCZCVFfGq_XDgR/view?usp=drive_link)

### 🎥 Demo Video 2 - Carbon Footprint Calculation
[Click to watch](https://drive.google.com/file/d/1qibswkiELLISUvLlkkekjaaCxy9gmhdq/view?usp=drive_link)

---

## 📁 Project Structure

```
ESTIMATIONOFCARBONFOOTPRINT/
├── carbon_footprint/          # Django app with views, models, routes
│   ├── migrations/
│   ├── static/                # CSS and images
│   │   ├── image/
│   │   ├── adminlogin.css
│   │   ├── mainpage.css
│   │   ├── pending-style.css
│   │   ├── userlogin.css
│   │   ├── usersignup.css
│   │   └── view-style.css
│   ├── templates/             # HTML templates (if present)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── estimationofcarbonfootprint/  # Main project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/                 # Global templates (if used)
├── manage.py
└── README.md
```

---

## 🚀 Features

- ✅ User authentication (sign up, login)
- 🚗 Transport, energy, and lifestyle input forms
- 🧮 Automated carbon footprint calculation
- 📊 Output visualizations/stats (if implemented)
- 🌍 Suggestion system for eco-friendly changes

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/whitedevilprogrammer/estimation-of-carbon-footprint.git
cd estimation-of-carbon-footprint
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate     # On Linux/Mac
env\Scripts\activate      # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> _Note: If `requirements.txt` is missing, install manually based on your Django version:_

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Then visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👨‍💻 Usage

- **Sign up / Log in**
- Enter your daily habits (transport, energy usage, waste)
- Get your estimated **carbon footprint**
- See tips to reduce emissions

---

## 🧠 Technologies Used

- Django (Python Web Framework)
- HTML5, CSS3
- SQLite3 (default DB)
- Static files (custom CSS)

---

## 📈 Future Enhancements

- Add charts using Chart.js or D3.js
- Integrate APIs for live carbon data
- User profile & history tracking
- Admin dashboard for analysis

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

---

## 🙋‍♂️ Author

**Ellalan Haridoss**  
Full Stack Developer (Golang + Vue.js + Django)  
📧 [ellalanharidoss@gmail.com](mailto:ellalanharidoss@gmail.com)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/ellalan-haridoss)

---

> "Let’s build technology that helps the planet, not harms it." 🌍💚
