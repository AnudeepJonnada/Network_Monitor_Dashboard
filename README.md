# 🌐 Network Monitoring Dashboard

A full-stack web application that lets you monitor devices on your local or remote network. Displays **online/offline status**, **latency (ms)**, and **last seen timestamps** using a clean and responsive Bootstrap dashboard.

---
<img width="500" alt="Untitled" src="https://github.com/user-attachments/assets/d5218efa-4dea-4c4f-be4b-6e5da67d1aab" />

## 🚀 Features

- ✅ Live device status (Online/Offline)
- 📶 Ping latency (in milliseconds)
- 🕒 "Last Seen" timestamp for offline devices
- ➕ Add devices via frontend form
- 🌍 Responsive and mobile-friendly UI (Bootstrap 5)
- 📁 JSON file-based device storage
- 🔁 Real-time updates via API

---

## 🛠 Tech Stack

| Layer     | Tech Used            |
|-----------|----------------------|
| Frontend  | HTML, CSS, JavaScript, Bootstrap 5 |
| Backend   | Python, Flask, Flask-CORS |
| Data      | JSON (devices.json)  |

---



---

## 💻 Local Setup

### 1️⃣ Clone the repo:

```bash
git clone https://github.com/AnudeepJonnada/Network_Monitor_Dashboard.git
cd Network_Monitor_Dashboard
```

### 2️⃣ Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the Flask server:

```bash
python3 -m backend.app
```

### 5️⃣ Open the Dashboard

Use **Live Server** extension in VS Code to open `frontend/index.html`  
> Make sure Flask is running first!


## 🙋‍♂️ Author

**Anudeep Jonnada** 

---



