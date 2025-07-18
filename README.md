# 🛒 Shopify Store Insights Fetcher API

A backend API project built using **FastAPI** that fetches **brand-related information** like About, Privacy Policy, and Return Policy from any **public Shopify website**.

> 🎯 Developed as part of a backend task for a **GenAI Developer Internship**.

---

## 📌 Features

- 🔍 Scrapes Shopify store URLs in real-time
- ⚡ FastAPI-powered REST API
- 🎯 Clean architecture using models and routing
- ✅ Easily extendable to persist data in MySQL
- 🧩 Follows best practices like modularity, OOP, SOLID, and REST

---

## ⚙️ Tech Stack

- **Python 3.11+**
- **FastAPI** for backend API
- **BeautifulSoup4** for web scraping
- **Uvicorn** for local server
- *(Optional)*: MySQL for persistence (bonus part)

---

## 🚀 How to Run Locally

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/shopify-insights-api.git
cd shopify-insights-api

## 2. Install dependencies
pip install -r requirements.txt

## 3. Run the FastAPI app
uvicorn main:app --reload

## 4. Test it in your browser
Go to 👉 http://127.0.0.1:8000/docs

Use the /fetch-brand endpoint by pasting any Shopify store URL, like:

https://bluecrate.com


## 🏗 Folder Structure
shopify-insights-api/
├── main.py          # FastAPI app + routes
├── models.py        # Pydantic models
├── database.py      # DB config (optional - for bonus)
├── scraper.py       # Web scraping logic
├── requirements.txt
└── README.md

## 🤝 A Note from the Developer
I’m a passionate beginner eager to grow as a backend + AI developer. This project was a hands-on task and I enjoyed building it from scratch with clean code and RESTful principles.

Thank you for reviewing my work 🙏
I’m excited for the opportunity to contribute, learn, and grow with your team.




