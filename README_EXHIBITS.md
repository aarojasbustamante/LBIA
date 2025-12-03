# 📊 LBIA Project Exhibits - Complete Guide

## 🎯 Overview
This folder contains everything you need to create the 6 exhibits for your final project report.

---

## 📁 Files in This Folder

1. **QUICK_REFERENCE.md** ⭐ START HERE
   - Complete step-by-step checklist
   - 18-minute quick start guide
   - Quality checklist
   - Copy-paste ready captions

2. **EXHIBITS_GUIDE.md**
   - Detailed instructions for each exhibit
   - Screenshot tips and tools
   - Assembly instructions

3. **architecture_diagram.md**
   - Mermaid code for Exhibit 1
   - System architecture diagram
   - Copy → paste → download

4. **database_schema_diagram.md**
   - Mermaid code for Exhibit 2
   - ER diagram for 4 tables
   - Multiple tool options

5. **screenshot_guide.py**
   - Printable instruction guide
   - Run: `python3 screenshot_guide.py`
   - Detailed screenshot steps

---

## ⚡ Quick Start (18 Minutes Total)

### Step 1: Create Diagrams (5 minutes)

**Exhibit 1: System Architecture**
```bash
1. Open https://mermaid.live/
2. Open architecture_diagram.md
3. Copy the Mermaid code block
4. Paste into mermaid.live
5. Click "Download PNG"
6. Save as: exhibit1_architecture.png
```

**Exhibit 2: Database Schema**
```bash
1. Open https://mermaid.live/ (new tab)
2. Open database_schema_diagram.md
3. Copy the Mermaid code block
4. Paste into mermaid.live
5. Click "Download PNG"
6. Save as: exhibit2_schema.png
```

### Step 2: Capture Screenshots (10 minutes)

**All screenshots from:** https://lbiaproject.streamlit.app/

**Exhibit 3: Overview Dashboard**
- Click Overview tab
- Cmd+Shift+4 → capture metrics + chart
- Save as: exhibit3_overview.png

**Exhibit 4: Revenue Analysis**
- Click Revenue tab
- Click "Generate Retention Strategies" button
- Use Chrome extension "Awesome Screenshot" → Capture entire page
- Save as: exhibit4_revenue.png

**Exhibit 5: Inventory Dashboard**
- Click Inventory tab
- Click "Restock Priority" sub-tab
- Cmd+Shift+4 → capture full view
- Save as: exhibit5_inventory.png

**Exhibit 6: Forecast Dashboard**
- Click Forecast tab
- Move slider to 3-6 months
- Wait for chart update
- Cmd+Shift+4 → capture dashboard
- Save as: exhibit6_forecast.png

### Step 3: Assemble PDF (3 minutes)

**Using PowerPoint:**
1. Create new presentation
2. Create 6 slides
3. For each slide:
   - Title: "Exhibit X: [Name]"
   - Insert image
   - Add caption from QUICK_REFERENCE.md
4. File → Export → Create PDF
5. Save as: LBIA_Project_Exhibits.pdf

---

## 📋 Exhibit Descriptions

| # | Title | Type | Tool | Time |
|---|-------|------|------|------|
| 1 | System Architecture | Diagram | Mermaid.live | 2 min |
| 2 | Database Schema | Diagram | Mermaid.live | 2 min |
| 3 | Overview Dashboard | Screenshot | Browser | 1 min |
| 4 | Revenue Analysis | Screenshot | Browser + Extension | 2 min |
| 5 | Inventory Dashboard | Screenshot | Browser | 1 min |
| 6 | Forecast Dashboard | Screenshot | Browser | 1 min |

**Total Time: ~18 minutes**

---

## ✅ Quality Checklist

Before submitting, verify:

### Images
- [ ] All 6 images are PNG format
- [ ] Resolution minimum 1920x1080
- [ ] Text is clearly readable
- [ ] No browser UI visible
- [ ] Dark theme preserved

### Content
- [ ] Exhibit 1: Shows complete 7-step pipeline
- [ ] Exhibit 2: Shows all 4 tables + relationships
- [ ] Exhibit 3: Shows 6 metrics + trend chart
- [ ] Exhibit 4: Shows products + churn prediction
- [ ] Exhibit 5: Shows velocity + tabs
- [ ] Exhibit 6: Shows forecast + confidence interval

### PDF
- [ ] Exactly 6 pages
- [ ] Each exhibit properly labeled
- [ ] Captions explain content
- [ ] File size under 10MB
- [ ] Filename: LBIA_Project_Exhibits.pdf

---

## 🛠️ Recommended Tools

**For Diagrams:**
- Mermaid.live (FREE, instant) ⭐ RECOMMENDED
- dbdiagram.io (FREE, database schemas)
- draw.io (FREE, manual drawing)

**For Screenshots:**
- Mac: Cmd+Shift+4 (built-in)
- Chrome Extension: "Awesome Screenshot" (for scrolling pages)
- Windows: Win+Shift+S (built-in)

**For PDF Assembly:**
- PowerPoint → Export PDF ⭐ EASIEST
- Word → Save as PDF
- macOS Preview → Combine PDFs

---

## 📝 Pre-Written Captions

Copy these directly into your PowerPoint/Word:

**Exhibit 1:**
> System architecture diagram illustrating the LBIA data pipeline from CSV upload through MySQL storage to AI-powered business insights. The system uses Streamlit for caching, Plotly for visualization, and OpenAI GPT-3.5-turbo for generating actionable recommendations.

**Exhibit 2:**
> Entity-Relationship diagram showing the normalized database schema with four interconnected tables: customers, products, transactions, and transaction_items. Foreign key relationships enable comprehensive analytics across customer behavior, product performance, and transaction history.

**Exhibit 3:**
> Overview dashboard displaying real-time KPIs including total revenue (£9.75M), order volume (25,900), and product catalog (4,070 items). The monthly revenue trend chart visualizes sales patterns, while AI-generated smart alerts identify anomalies requiring attention.

**Exhibit 4:**
> Revenue analysis dashboard featuring top-performing products by revenue and geographic distribution across 38 countries. The Customer Retention Intelligence section leverages AI to identify at-risk customers based on recency, frequency, and monetary patterns, with automated retention strategy recommendations.

**Exhibit 5:**
> Inventory dashboard categorizing 4,070 active products into Fast Movers (39.9%) and Slow Movers (60.1%) based on sales velocity. The tabbed interface provides actionable views for restock prioritization, slow-moving items, high-return products, and comprehensive product listings.

**Exhibit 6:**
> Sales forecasting dashboard powered by Linear Regression showing 6-month revenue predictions with 95% confidence intervals. Model performance metrics include R² score, MAPE, and trend coefficient, enabling data-driven planning for inventory, staffing, and cash flow management.

---

## 🆘 Troubleshooting

**Q: Mermaid diagram doesn't render**  
A: Make sure you copied the ENTIRE code block including the triple backticks (```)

**Q: Screenshot is blurry**  
A: Set browser zoom to 100% (Cmd+0), use PNG not JPEG

**Q: Can't capture full Revenue page**  
A: Install Chrome extension "Awesome Screenshot" for scrolling capture

**Q: PDF too large**  
A: Compress images at https://tinypng.com/ before adding to document

**Q: Dashboard won't load**  
A: Wait 30 seconds for Streamlit to wake up, then refresh

---

## 📧 Final Submission Structure

```
Project_Submission.zip
├── LBIA_Project_Report.pdf (4 pages max)
├── LBIA_Project_Exhibits.pdf (6 pages - one per exhibit)
└── [Any additional files]
```

---

## 🎯 Next Steps

1. ✅ Read QUICK_REFERENCE.md
2. ✅ Create Exhibits 1-2 using Mermaid.live (5 min)
3. ✅ Capture Exhibits 3-6 from dashboard (10 min)
4. ✅ Assemble PDF with captions (3 min)
5. ✅ Quality check using checklist
6. ✅ Submit!

---

## 📌 Important Links

- **Dashboard:** https://lbiaproject.streamlit.app/
- **Diagram Tool:** https://mermaid.live/
- **Alt Diagram Tool:** https://dbdiagram.io/
- **Screenshot Extension:** [Awesome Screenshot](https://chrome.google.com/webstore/detail/awesome-screenshot-screen/nlipoenfbbikpbjkfpfillcgkibla)

---

**Good luck with your submission! 🎉**

If you need help, review the detailed guides in the other .md files.
