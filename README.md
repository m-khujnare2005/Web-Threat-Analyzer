
# 🛡️ Web Threat Analyzer

Web Threat Analyzer is a cybersecurity-focused web application that analyzes website security and generates a threat assessment report. The application performs multiple security checks such as SSL verification, security header analysis, WHOIS lookup, and threat score calculation. All scan results are stored in MongoDB for future reference.

---

## 🚀 Features

- ✅ URL Validation
- 🔒 SSL Certificate Analysis
- 🛡️ Security Headers Inspection
- 🌐 WHOIS Domain Information Lookup
- 📊 Threat Score Calculation
- ⚠️ Risk Level Assessment
- 💾 MongoDB Database Storage
- 🎨 Interactive Web Interface

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MongoDB Atlas

### Python Libraries
- requests
- validators
- python-whois
- pymongo
- flask
- flask-cors

---

## 📂 Project Structure

```text
web-threat-analyzer/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   └── modules/
│       ├── url_validators.py
│       ├── ssl_checker.py
│       ├── header_checker.py
│       ├── whois_checker.py
│       ├── risk_calculator.py
│       └── database.py
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/web-threat-analyzer.git
```

```bash
cd web-threat-analyzer
```

---

## 📦 Install Dependencies

Open terminal inside the backend folder:

```bash
cd backend
```

Install required packages:

```bash
python -m pip install flask
python -m pip install flask-cors
python -m pip install requests
python -m pip install validators
python -m pip install python-whois
python -m pip install pymongo
```

Or install everything together:

```bash
python -m pip install flask flask-cors requests validators python-whois pymongo
```

---

## 🗄️ MongoDB Setup

1. Create a MongoDB Atlas account.
2. Create a Cluster.
3. Create a Database User.
4. Copy your MongoDB Connection String.
5. Open:

```text
backend/modules/database.py
```

6. Replace:

```python
MongoClient("YOUR_MONGODB_CONNECTION_STRING")
```

with your connection string.

---

## ▶️ Running the Project

### Step 1: Start Backend Server

Open terminal:

```bash
cd backend
```

Run:

```bash
python app.py
```

Expected Output:

```text
* Running on http://127.0.0.1:5000
```

---

### Step 2: Start Frontend

Open the frontend folder in VS Code.

Run:

```text
Right Click → Open with Live Server
```

or simply open:

```text
frontend/index.html
```

in your browser.

---

## 🧪 How to Use

1. Enter a website URL.

Example:

```text
https://google.com
```

2. Click:

```text
Scan Website
```

3. View:

- SSL Status
- Certificate Issuer
- Security Headers
- WHOIS Information
- Threat Score
- Risk Level

4. Scan results are automatically saved to MongoDB.

---

## 📊 Sample Output

```text
Website: https://google.com

SSL Status: Valid

Certificate Issuer:
Google Trust Services

Threat Score:
45/100

Risk Level:
HIGH RISK
```

---

## 🔮 Future Enhancements

- AI-Based Threat Detection
- Phishing Website Detection
- Malware URL Analysis
- Dashboard Analytics
- PDF Report Generation
- User Authentication
- Scan History Dashboard

---

## 👨‍💻 Author

Manthan Khujnare

Cyber Security Student | Frontend Developer | Exploring Data Analytics & AI

---

## 📜 License

This project is developed for educational and learning purposes.
