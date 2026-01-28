# 📦 Texno Scraper

A simple Python web scraper that collects product data (image, title, credit price, and current price) from an online tech store using **Requests**, **BeautifulSoup**, and **dotenv**.
---
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/Scraping-BeautifulSoup-green?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-Library-orange?style=for-the-badge)
---

## 🚀 Features

- Scrapes product:
  - 🖼 Image URLs  
  - 🏷 Titles  
  - 💳 Installment prices  
  - 💰 Current prices  
- Saves all data into a structured **JSON file**
- Uses environment variables for cleaner configuration

---

## 🛠 Requirements

Install the dependencies:

pip install requests beautifulsoup4 python-dotenv


⚙️ Setup

Create a .env file in the project root:

URL=https://example.com/
HOST=https://example.com


Replace the URL with the actual site you want to scrape.


🧠 How It Works

Sends an HTTP request to the target page

Parses HTML using BeautifulSoup

Extracts product cards using class selectors

Stores results in a list and exports to JSON

⚠️ Disclaimer

This project is for educational purposes only. Always check a website’s robots.txt and terms of service before scraping.
