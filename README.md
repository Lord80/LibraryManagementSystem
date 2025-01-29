📚 Library Management System
A web-based Library Management System built using Flask, MongoDB, HTML, CSS, and JavaScript.
This system allows users to view available books, borrow them, and manage the library efficiently.

📌 Features
✅ Add, View, and Manage Books
✅ Search Books Dynamically
✅ Borrow Books with a Click
✅ User Authentication (Login/Signup)
✅ Responsive UI with Modern Design

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript (Jinja2 templating)
Backend: Flask (Python)
Database: MongoDB
Authentication: Flask-Login, Flask-WTF
📂 Project Structure
bash
Copy
Edit
Library-Management-System/
│── app.py                  # Main Flask application
│── db.py                   # Database connection
│── routes.py               # Routes for handling requests
│── forms.py                # Forms for login & book actions
│── models.py               # MongoDB models
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│
├── templates/              # Jinja2 Templates (HTML)
│   ├── base.html           # Base template
│   ├── index.html          # Homepage
│   ├── books.html          # List of books
│   ├── borrow_book.html    # Borrow book page
│   ├── login.html          # User login page
│
├── static/                 # Static files (CSS, JS, Images)
│   ├── css/style.css       # Main CSS file
│   ├── js/script.js        # JavaScript functions
│
└── migrations/             # Database migrations
🚀 Installation Guide
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/Lord80/Library-Management-System.git
cd Library-Management-System
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Start MongoDB Server
Make sure MongoDB is running. If you use MongoDB Atlas, update the connection string in db.py:

python
Copy
Edit
client = pymongo.MongoClient("mongodb+srv://your_user:your_password@your_cluster.mongodb.net/")
5️⃣ Run the Application
sh
Copy
Edit
python app.py
The server will start at http://127.0.0.1:5000/. Open it in your browser.

🖼️ Screenshots
Home Page	Books List
🛠️ Future Improvements
✅ Admin Dashboard for Book Management
✅ Book Return System
✅ User Profiles & Borrowing History
📩 Contact & Contribution
💡 Found a bug or have suggestions? Feel free to open an issue or contribute!
🔗 GitHub: Lord80

