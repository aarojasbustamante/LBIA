# LBIA Project Exhibits Guide

## How to Create Your 6 Exhibits for the Report

---

## Exhibit 1: System Architecture Diagram

**Description:** A flowchart showing the data pipeline from CSV upload to AI insights.

**To Create:**
1. Use **draw.io** (diagrams.net) or **PowerPoint**
2. Create boxes with arrows connecting:

```
┌─────────────────┐
│   CSV Upload    │
│ (User Interface)│
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│ Validation & Cleaning   │
│ • Check columns         │
│ • Handle NaN values     │
│ • Type conversion       │
└────────┬────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Product Mapping +        │
│ Return Flagging          │
│ • Map stock codes        │
│ • Flag negative quantity │
└────────┬─────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ MySQL Database (4 Tables)      │
│ ┌──────────┐  ┌──────────┐    │
│ │customers │  │ products │    │
│ └──────────┘  └──────────┘    │
│ ┌──────────┐  ┌──────────┐    │
│ │transactions│ │  items   │    │
│ └──────────┘  └──────────┘    │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────┐
│ Streamlit Cached       │
│ SQL Queries            │
│ (@st.cache_data)       │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Plotly Visualizations  │
│ • Charts               │
│ • Metrics              │
│ • Tables               │
└────────┬───────────────┘
         │
         ▼
┌─────────────────────────────┐
│ AI Insight Engine           │
│ ┌─────────┐  ┌───────────┐ │
│ │ OpenAI  │  │  Parser   │ │
│ │  API    │  │ Fallback  │ │
│ └─────────┘  └───────────┘ │
└────────┬────────────────────┘
         │
         ▼
┌────────────────────────┐
│ Smart Alerts +         │
│ Forecasts              │
│ • Anomaly detection    │
│ • Trend predictions    │
└────────────────────────┘
```

**Tools:** Use Lucidchart, draw.io, or PowerPoint with shapes and arrows.

**Colors to use:**
- Blue (#3b82f6) for data processing
- Purple (#667eea) for AI components
- Green (#10b981) for outputs

---

## Exhibit 2: Database Schema

**Description:** Entity-Relationship diagram showing the 4 tables and their relationships.

**To Create in draw.io or PowerPoint:**

```
┌─────────────────────┐
│     customers       │
├─────────────────────┤
│ PK customer_id      │
│    country          │
│    first_trans_date │
│    total_orders     │
└──────────┬──────────┘
           │ 1
           │
           │ *
┌──────────▼──────────┐
│    transactions     │
├─────────────────────┤
│ PK transaction_id   │
│    invoice_no       │
│ FK customer_id      │◄─────┐
│    invoice_date     │      │
│    total_amount     │      │ 1
└──────────┬──────────┘      │
           │ 1               │
           │                 │
           │ *               │
┌──────────▼──────────┐      │
│  transaction_items  │      │
├─────────────────────┤      │
│ PK item_id          │      │
│ FK transaction_id   │──────┘
│ FK product_id       │──────┐
│    quantity         │      │
│    unit_price       │      │
│    is_return        │      │
│    line_total       │      │
└─────────────────────┘      │
                             │ *
                             │
                             │ 1
                    ┌────────▼────────┐
                    │    products     │
                    ├─────────────────┤
                    │ PK product_id   │
                    │    stock_code   │
                    │    description  │
                    │    category     │
                    └─────────────────┘
```

**Key:**
- PK = Primary Key
- FK = Foreign Key
- 1 = One
- * = Many

---

## Exhibit 3: Overview Dashboard Screenshot

**To Capture:**
1. Go to: https://lbiaproject.streamlit.app/
2. Click on **Overview** tab
3. Scroll to show:
   - Revenue metrics (Total Revenue, Total Orders, Products, Customers)
   - Avg Order Value and Return Rate
   - Monthly Revenue Trend chart
   - Smart Alerts section (if visible)
4. Take a screenshot using:
   - Mac: `Cmd + Shift + 4` (drag to select area)
   - Windows: `Win + Shift + S`
5. Save as `exhibit3_overview.png`

**Key elements to highlight in your report:**
- Clean, professional dark theme
- Real-time KPI metrics
- Interactive trend chart
- AI-generated anomaly alerts

---

## Exhibit 4: Revenue Analysis Screenshot

**To Capture:**
1. Go to: https://lbiaproject.streamlit.app/
2. Click on **Revenue** tab
3. Scroll to show:
   - Top Products by Revenue (bar chart)
   - Top Products table
   - Revenue by Country table
   - Customer Retention Intelligence section
   - High Risk/Medium Risk/At-Risk Revenue metrics
   - Top At-Risk Customers table
   - Generate Retention Strategies button
4. Take screenshot
5. Save as `exhibit4_revenue.png`

**Key elements:**
- Product performance visualization
- Geographic revenue breakdown
- AI-powered churn prediction
- Retention strategy recommendations

---

## Exhibit 5: Inventory Dashboard Screenshot

**To Capture:**
1. Go to: https://lbiaproject.streamlit.app/
2. Click on **Inventory** tab
3. Scroll to show:
   - Inventory velocity metrics (Active Products, Fast Movers, Slow Movers, Avg Return Rate)
   - Inventory Velocity Distribution (pie chart)
   - Top Revenue Generators chart
   - Tabbed section showing:
     - Restock Priority
     - Slow Movers
     - High Returns
     - All Products
4. Take screenshot showing the tabs
5. Save as `exhibit5_inventory.png`

**Key elements:**
- Inventory classification system
- Fast/slow mover analysis
- Return rate monitoring
- Actionable restock priorities

---

## Exhibit 6: Forecast Dashboard Screenshot

**To Capture:**
1. Go to: https://lbiaproject.streamlit.app/
2. Click on **Forecast** tab
3. Adjust the forecast slider to show 3-6 months
4. Scroll to show:
   - Forecast Settings slider
   - Key metrics (Next Month Forecast, 3-Month Avg, Trend Direction, Forecast Confidence)
   - Historical Performance & Forecast chart showing:
     - Blue line (Actual Revenue)
     - Dotted line (Model Fit)
     - Red dashed line (Forecast)
     - Pink shaded area (Confidence Range)
   - Forecast Details table
   - Model Performance metrics (R² Score, MAPE, Trend Coefficient)
5. Take screenshot
6. Save as `exhibit6_forecast.png`

**Key elements:**
- Interactive forecast horizon selection
- ML model accuracy metrics (MAPE, R²)
- Visual trend projection with confidence intervals
- Actionable planning insights

---

## Tips for Professional Screenshots

1. **Clear the browser cache** before taking screenshots for best performance
2. **Use full screen** (F11) to hide browser UI
3. **Zoom to 100%** for crisp images
4. **Capture in daylight mode** if colors look washed out
5. **Annotate if needed** using PowerPoint or Snagit to add arrows/callouts

---

## Creating a Combined Exhibit Document

**Option 1: PowerPoint**
1. Create new presentation
2. One slide per exhibit
3. Title each slide: "Exhibit 1: System Architecture", etc.
4. Add screenshot or diagram
5. Add caption describing what's shown
6. Export as PDF: File → Export → PDF

**Option 2: Word Document**
1. Create new document
2. Insert page breaks between exhibits
3. Title: "Exhibit 1: System Architecture Diagram"
4. Insert image
5. Add caption: "Figure shows data flow from CSV upload through MySQL database to AI-powered insights"
6. Save as PDF

---

## Screenshot Checklist

- [ ] Exhibit 1: Architecture diagram created (draw.io/PowerPoint)
- [ ] Exhibit 2: Database schema diagram created
- [ ] Exhibit 3: Overview dashboard screenshot captured
- [ ] Exhibit 4: Revenue analysis screenshot captured
- [ ] Exhibit 5: Inventory dashboard screenshot captured
- [ ] Exhibit 6: Forecast dashboard screenshot captured
- [ ] All images saved as PNG (high resolution)
- [ ] All exhibits compiled into single PDF document
- [ ] File size under 10MB for submission

---

## Final Assembly

1. Create a folder: `LBIA_Exhibits/`
2. Place all 6 exhibit images inside
3. Create the exhibits document with all 6 exhibits
4. Export as: `LBIA_Project_Exhibits.pdf`
5. Include in your final ZIP file submission

Good luck with your submission! 🎉
