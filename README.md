# ⚡ Rogaland Electricity Price Monitor (NO2)

An end-to-end data pipeline built with Python and SQL. It fetches daily electricity prices for the Rogaland region (NO2 zone) via a public REST API, stores the structured data in an SQLite database, and queries the cheapest electricity hours of the day.

## 🛠️ Tech Stack
- **Python 3**: Requests, Pandas, SQLAlchemy
- **Database**: SQL / SQLite
- **API**: Hva Koster Strømmen API (Public REST API)

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install requests pandas sqlalchemy