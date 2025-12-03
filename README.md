# LBIA Dashboard 🚀

**Local Business Intelligence Assistant** - An AI-powered Streamlit dashboard for retail analytics featuring intelligent insights, customer churn prediction, inventory optimization, and revenue forecasting.

🌐 **Live App:** https://lbiaproject.streamlit.app/

## ✨ Features

### 📊 Overview Dashboard
- Real-time KPIs: Total Revenue (£9.75M), Orders (25.9K), Products (4K+), Customers (4.3K)
- Monthly revenue trend visualization
- AI-powered smart alerts for anomaly detection
- Interactive chat widget for natural language queries

### 💰 Revenue Analysis
- Top products by revenue with interactive charts
- Geographic revenue distribution across 38 countries
- **Customer Retention Intelligence** (NEW):
  - AI-powered churn prediction (High/Medium/At-Risk)
  - Automated retention strategy recommendations
  - RFM (Recency, Frequency, Monetary) analysis
  - Top at-risk customers identification

### 📦 Inventory Intelligence
- Inventory velocity classification (Fast/Slow Movers)
- Restock priority recommendations
- High-return product monitoring
- Revenue generator analysis with tabbed views

### 🔮 Forecasting
- ML-powered revenue predictions (Linear Regression)
- Configurable forecast horizon (1-12 months)
- 95% confidence intervals
- Model performance metrics (R², MAPE, Trend Coefficient)
- Interactive forecast visualization

### 🤖 AI Features
- Natural language query interface
- Context-aware business insights
- Anomaly detection and alerts
- Automated retention strategies
- SQL query generation from natural language

## 🛠️ Tech Stack

- **Frontend**: Streamlit 1.x, Plotly Express/Graph Objects
- **Backend**: Python 3.11+, MySQL 8.0
- **AI/ML**: 
  - OpenAI GPT-3.5-turbo (insights & NL queries)
  - scikit-learn (forecasting)
- **Database**: MySQL on Clever Cloud
- **Deployment**: Streamlit Community Cloud
- **Data Processing**: pandas, NumPy

## 🗄️ Database Schema

Four interconnected tables in normalized MySQL database:
- `customers` - Customer master data
- `products` - Product catalog
- `transactions` - Order headers
- `transaction_items` - Order line items with return flags

See `database_schema_diagram.md` for full ER diagram.

## 🚀 Deployment

**Live Production App:** https://lbiaproject.streamlit.app/

### Local Development

1. **Clone the repository:**
```bash
git clone https://github.com/aarojasbustamante/LBIA.git
cd LBIA
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up secrets:**
Create `.streamlit/secrets.toml`:
```toml
[connections.mysql]
host = "your-mysql-host"
port = 3306
database = "your-database"
username = "your-username"
password = "your-password"

OPENAI_API_KEY = "your-openai-api-key"
```

4. **Run the app:**
```bash
streamlit run streamlit_app.py
```

5. **Access locally:**
Open http://localhost:8501 in your browser


## 📊 Project Structure

```
LBIA/
├── streamlit_app.py          # Main application file
├── requirements.txt          # Python dependencies
├── online_retail_II_option2.csv  # Source data
├── README.md                # This file
├── LBIA_Exhibits/           # Project exhibits for report
│   ├── exhibit1_architecture.png
│   ├── exhibit2_schema.png
│   ├── exhibit3_overview.png
│   ├── exhibit4_revenue.png
│   ├── exhibit5_inventory.png
│   └── exhibit6_forecast.png
└── .streamlit/
    └── secrets.toml         # Configuration (not in repo)
```

## 📈 Key Metrics

- **Total Revenue**: £9.75M
- **Total Orders**: 25,900 transactions
- **Product Catalog**: 4,070 active products
- **Customer Base**: 4,372 unique customers
- **Countries Served**: 38 global markets
- **Time Period**: Dec 2009 - Dec 2011

## 🎓 Academic Project

This dashboard was developed as part of an MBA Data Management and AI course project. The system demonstrates:
- Data pipeline architecture (CSV → MySQL → Analytics)
- AI integration for business insights
- Machine learning for predictive analytics
- Interactive dashboard design
- Database normalization and optimization

**Report Documentation:**
- `README_EXHIBITS.md` - Guide to creating project exhibits
- `QUICK_REFERENCE.md` - Quick start checklist
- `architecture_diagram.md` - System architecture
- `database_schema_diagram.md` - Database ER diagram

## 👥 Team

- **Simran Verma** - Co-Founder
- **Shiv Uppal** - Co-Founder  
- **Alvaro Rojas** - Co-Founder
- **Marcia Rivera** - Co-Founder

---

© 2025 LBIA — All Rights Reserved
