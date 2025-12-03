# LBIA Project Exhibits - Quick Reference

## 🎯 Complete Exhibit Checklist

### Exhibit 1: System Architecture Diagram ✨
**What:** Data flow from CSV to AI insights  
**Tool:** https://mermaid.live/  
**File:** Copy code from `architecture_diagram.md`  
**Output:** `exhibit1_architecture.png`  
**Time:** 2 minutes

**Steps:**
1. Open https://mermaid.live/
2. Copy Mermaid code from `architecture_diagram.md`
3. Paste into left editor
4. Click "Download PNG"
5. Save as `exhibit1_architecture.png`

---

### Exhibit 2: Database Schema Diagram 📊
**What:** 4-table ER diagram with relationships  
**Tool:** https://mermaid.live/ or https://dbdiagram.io/  
**File:** Copy code from `database_schema_diagram.md`  
**Output:** `exhibit2_schema.png`  
**Time:** 2 minutes

**Steps:**
1. Open https://mermaid.live/
2. Copy Mermaid ER code from `database_schema_diagram.md`
3. Paste into editor
4. Click "Download PNG"
5. Save as `exhibit2_schema.png`

---

### Exhibit 3: Overview Dashboard 🏠
**What:** Main dashboard with metrics and trends  
**URL:** https://lbiaproject.streamlit.app/ → Overview tab  
**Output:** `exhibit3_overview.png`  
**Time:** 1 minute

**Must Show:**
- [ ] Total Revenue, Orders, Products, Customers (top row)
- [ ] Average Order Value, Return Rate (second row)
- [ ] Monthly Revenue Trend chart
- [ ] Smart Alerts section

**Screenshot:**
- Mac: `Cmd + Shift + 4` → drag selection
- Windows: `Win + Shift + S`

---

### Exhibit 4: Revenue Analysis 💰
**What:** Product performance + churn prediction  
**URL:** https://lbiaproject.streamlit.app/ → Revenue tab  
**Output:** `exhibit4_revenue.png`  
**Time:** 2 minutes (scrolling screenshot)

**Must Show:**
- [ ] Top Products by Revenue (bar chart)
- [ ] Revenue by Country table
- [ ] Customer Retention Intelligence section
- [ ] High Risk / Medium Risk / At-Risk metrics
- [ ] Top At-Risk Customers table
- [ ] Retention strategies (click Generate button first)

**Tool:** Use "Awesome Screenshot" Chrome extension for full-page capture

---

### Exhibit 5: Inventory Dashboard 📦
**What:** Velocity classification and restock priorities  
**URL:** https://lbiaproject.streamlit.app/ → Inventory tab  
**Output:** `exhibit5_inventory.png`  
**Time:** 1 minute

**Must Show:**
- [ ] Active Products, Fast Movers, Slow Movers metrics
- [ ] Inventory Velocity Distribution (pie chart)
- [ ] Top 10 Revenue Generators chart
- [ ] Tabbed section (Restock Priority, Slow Movers, High Returns, All Products)

**Tip:** Click on "Restock Priority" tab before screenshot

---

### Exhibit 6: Forecast Dashboard 📈
**What:** ML-powered revenue predictions  
**URL:** https://lbiaproject.streamlit.app/ → Forecast tab  
**Output:** `exhibit6_forecast.png`  
**Time:** 1 minute

**Must Show:**
- [ ] Forecast Settings slider (set to 3-6 months)
- [ ] Next Month Forecast, 3-Month Avg, Trend, Confidence metrics
- [ ] Historical Performance & Forecast chart with:
  - Blue line (Actual)
  - Dotted line (Model Fit)
  - Red dashed (Forecast)
  - Pink shaded (Confidence)
- [ ] Forecast Details table
- [ ] Model Performance (R², MAPE, Trend Coefficient)

---

## 🚀 Quick Start (10-Minute Version)

### Step 1: Create Diagrams (5 minutes)
```bash
# Open these two links in browser tabs:
1. https://mermaid.live/
2. https://mermaid.live/ (second tab)

# Tab 1: Architecture
- Open architecture_diagram.md
- Copy Mermaid code
- Paste into mermaid.live
- Download PNG → exhibit1_architecture.png

# Tab 2: Database Schema
- Open database_schema_diagram.md
- Copy Mermaid code
- Paste into mermaid.live
- Download PNG → exhibit2_schema.png
```

### Step 2: Capture Screenshots (5 minutes)
```bash
# Open: https://lbiaproject.streamlit.app/

# Exhibit 3 (Overview)
1. Ensure Overview tab is active
2. Cmd+Shift+4 → drag to select dashboard
3. Save as exhibit3_overview.png

# Exhibit 4 (Revenue)
1. Click Revenue tab
2. Scroll to bottom → Click "Generate Retention Strategies"
3. Install Chrome extension "Awesome Screenshot"
4. Click extension → Capture entire page
5. Save as exhibit4_revenue.png

# Exhibit 5 (Inventory)
1. Click Inventory tab
2. Click "Restock Priority" sub-tab
3. Cmd+Shift+4 → capture full view
4. Save as exhibit5_inventory.png

# Exhibit 6 (Forecast)
1. Click Forecast tab
2. Move slider to 3-6 months
3. Wait for chart to update
4. Cmd+Shift+4 → capture dashboard
5. Save as exhibit6_forecast.png
```

---

## 📄 Assembly Into PDF (5 minutes)

### Option A: PowerPoint (Recommended)
1. Open PowerPoint
2. Create 6 blank slides
3. For each slide:
   - Title: "Exhibit X: [Name]"
   - Insert → Picture → select exhibit image
   - Resize to fit slide
   - Add caption/description below
4. File → Export → Create PDF/XPS
5. Save as: `LBIA_Project_Exhibits.pdf`

### Option B: Word
1. Open Word
2. For each exhibit:
   - Heading 1: "Exhibit X: [Name]"
   - Insert → Pictures → select image
   - Add caption
   - Insert → Page Break
3. File → Save As → PDF
4. Save as: `LBIA_Project_Exhibits.pdf`

---

## ✅ Quality Checklist Before Submission

### Image Quality
- [ ] All images are PNG format (not JPEG)
- [ ] Resolution minimum 1920x1080
- [ ] Text is clearly readable
- [ ] No browser UI visible (bookmarks, tabs)
- [ ] Dark theme preserved in screenshots

### Content Completeness
- [ ] Exhibit 1 shows complete data pipeline (7+ steps)
- [ ] Exhibit 2 shows all 4 tables with relationships
- [ ] Exhibit 3 shows all 6 metrics + trend chart
- [ ] Exhibit 4 shows both product analysis AND churn prediction
- [ ] Exhibit 5 shows velocity classification AND tabs
- [ ] Exhibit 6 shows forecast chart with confidence interval

### Document Assembly
- [ ] PDF contains exactly 6 pages
- [ ] Each exhibit is properly labeled
- [ ] Captions explain what's shown
- [ ] File size under 10MB
- [ ] Filename: `LBIA_Project_Exhibits.pdf`

### References in Report
- [ ] Text references "See Exhibit X" for each visual
- [ ] Exhibits support written analysis
- [ ] Exhibit numbers match PDF page order

---

## 📋 Exhibit Captions (Copy-Paste Ready)

**Exhibit 1 Caption:**
> "System architecture diagram illustrating the LBIA data pipeline from CSV upload through MySQL storage to AI-powered business insights. The system uses Streamlit for caching, Plotly for visualization, and OpenAI GPT-3.5-turbo for generating actionable recommendations."

**Exhibit 2 Caption:**
> "Entity-Relationship diagram showing the normalized database schema with four interconnected tables: customers, products, transactions, and transaction_items. Foreign key relationships enable comprehensive analytics across customer behavior, product performance, and transaction history."

**Exhibit 3 Caption:**
> "Overview dashboard displaying real-time KPIs including total revenue (£9.75M), order volume (25,900), and product catalog (4,070 items). The monthly revenue trend chart visualizes sales patterns, while AI-generated smart alerts identify anomalies requiring attention."

**Exhibit 4 Caption:**
> "Revenue analysis dashboard featuring top-performing products by revenue and geographic distribution across 38 countries. The Customer Retention Intelligence section leverages AI to identify at-risk customers based on recency, frequency, and monetary patterns, with automated retention strategy recommendations."

**Exhibit 5 Caption:**
> "Inventory dashboard categorizing 4,070 active products into Fast Movers (39.9%) and Slow Movers (60.1%) based on sales velocity. The tabbed interface provides actionable views for restock prioritization, slow-moving items, high-return products, and comprehensive product listings."

**Exhibit 6 Caption:**
> "Sales forecasting dashboard powered by Linear Regression showing 6-month revenue predictions with 95% confidence intervals. Model performance metrics include R² score, MAPE, and trend coefficient, enabling data-driven planning for inventory, staffing, and cash flow management."

---

## 🎯 Final File Structure

```
LBIA_Exhibits/
├── exhibit1_architecture.png
├── exhibit2_schema.png
├── exhibit3_overview.png
├── exhibit4_revenue.png
├── exhibit5_inventory.png
├── exhibit6_forecast.png
└── LBIA_Project_Exhibits.pdf ← Submit this
```

---

## ⏱️ Time Estimate

| Task | Time |
|------|------|
| Create diagrams (Exhibits 1-2) | 5 min |
| Capture screenshots (Exhibits 3-6) | 5 min |
| Assemble PDF with captions | 5 min |
| Quality check | 3 min |
| **TOTAL** | **18 min** |

---

## 🆘 Troubleshooting

**Problem:** Screenshot is blurry  
**Solution:** Use 100% zoom (Cmd+0), ensure high DPI display

**Problem:** Mermaid diagram looks weird  
**Solution:** Copy the ENTIRE code block including backticks

**Problem:** Can't capture full Revenue page  
**Solution:** Install "Awesome Screenshot" Chrome extension

**Problem:** PDF file too large (>10MB)  
**Solution:** Compress images at https://tinypng.com/ before inserting

**Problem:** Dashboard not loading  
**Solution:** Wait 30 seconds for Streamlit to wake up, refresh if needed

---

## 📧 Ready to Submit

Once you have `LBIA_Project_Exhibits.pdf`:
1. Include in your final project ZIP file
2. Reference exhibits in your 4-page report
3. Ensure report + exhibits = max 10 pages total
4. Submit before deadline

**Good luck! 🎉**
