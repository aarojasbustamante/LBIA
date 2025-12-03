"""
Screenshot Guide for LBIA Dashboard
This file provides detailed instructions for capturing the 6 exhibits needed for your report.
"""

# ====================================================================
# EXHIBIT 3: Overview Dashboard Screenshot
# ====================================================================

exhibit_3_instructions = """
EXHIBIT 3: OVERVIEW DASHBOARD

URL: https://lbiaproject.streamlit.app/

Steps:
1. Open the URL in Chrome/Safari
2. Click on "Overview" in the sidebar (should be default)
3. Wait for all metrics to load
4. Scroll to show:
   ✓ Top metrics row: Total Revenue, Total Orders, Total Products, Unique Customers
   ✓ Second metrics row: Average Order Value, Return Rate
   ✓ Monthly Revenue Trend chart (blue line chart)
   ✓ Smart Alerts section (if any anomalies detected)
   
5. Press F11 for full-screen (or Cmd+Shift+F on Mac)
6. Take screenshot:
   - Mac: Cmd + Shift + 4 (drag to select)
   - Windows: Win + Shift + S
   
7. Save as: exhibit3_overview.png

Key Elements to Show:
- Clean dark theme interface
- All 6 KPI metrics clearly visible
- Interactive revenue trend chart
- AI-generated smart alerts (if present)

Annotation Ideas:
- Arrow pointing to metrics: "Real-time KPIs"
- Arrow to chart: "Interactive trend visualization"
- Arrow to alerts: "AI-powered anomaly detection"
"""

# ====================================================================
# EXHIBIT 4: Revenue Analysis Screenshot
# ====================================================================

exhibit_4_instructions = """
EXHIBIT 4: REVENUE ANALYSIS DASHBOARD

URL: https://lbiaproject.streamlit.app/

Steps:
1. Click on "Revenue" tab in sidebar
2. Scroll to capture TWO screenshots (or one long scrolling screenshot):

   Screenshot 4a - Top Section:
   ✓ Top Products by Revenue (horizontal bar chart)
   ✓ Top 10 Products table
   ✓ Revenue by Country table
   
   Screenshot 4b - Bottom Section:
   ✓ Customer Retention Intelligence header
   ✓ Three metrics: High Risk, Medium Risk, At-Risk Revenue
   ✓ Top 10 At-Risk Customers table
   ✓ "Generate Retention Strategies" button
   ✓ Retention strategies output (if generated)

3. For scrolling screenshot on Mac:
   - Install "Awesome Screenshot" Chrome extension
   - Click extension → Capture entire page
   
4. Save as: exhibit4_revenue.png

Key Elements to Show:
- Product performance rankings
- Geographic revenue distribution
- Churn risk classification (High/Medium/At-Risk)
- Actionable customer retention insights

Annotation Ideas:
- Box around churn metrics: "AI-Powered Churn Prediction"
- Highlight top product: "Best seller identification"
- Arrow to strategies: "Automated retention planning"
"""

# ====================================================================
# EXHIBIT 5: Inventory Dashboard Screenshot
# ====================================================================

exhibit_5_instructions = """
EXHIBIT 5: INVENTORY DASHBOARD

URL: https://lbiaproject.streamlit.app/

Steps:
1. Click on "Inventory" tab in sidebar
2. Scroll to show:
   ✓ Top metrics: Active Products, Fast Movers, Slow Movers, Avg Return Rate
   ✓ Inventory Velocity Distribution (pie chart)
   ✓ Top 10 Revenue Generators (bar chart)
   ✓ Tabbed section showing all 4 tabs:
     - Restock Priority (⚠️ icon)
     - Slow Movers (🐌 icon)
     - High Returns (↩️ icon)
     - All Products (📦 icon)
   
3. Click on "Restock Priority" tab to show that view
4. Take screenshot showing the tab interface

5. Save as: exhibit5_inventory.png

Key Elements to Show:
- Inventory velocity classification (Fast/Slow)
- Visual distribution pie chart
- Tabbed organization for different views
- Actionable restock priorities

Annotation Ideas:
- Circle the velocity pie chart: "Automated classification"
- Box around tabs: "Multiple action-oriented views"
- Highlight return rate: "Quality monitoring"
"""

# ====================================================================
# EXHIBIT 6: Forecast Dashboard Screenshot
# ====================================================================

exhibit_6_instructions = """
EXHIBIT 6: FORECAST DASHBOARD

URL: https://lbiaproject.streamlit.app/

Steps:
1. Click on "Forecast" tab in sidebar
2. Adjust the slider to 3-6 months forecast
3. Wait for the chart to update
4. Scroll to show:
   ✓ Forecast Settings slider
   ✓ Four metrics: Next Month Forecast, 3-Month Avg, Trend Direction, Forecast Confidence
   ✓ Historical Performance & Forecast chart with:
     - Blue line (Actual Revenue)
     - Dotted blue line (Model Fit)
     - Red dashed line (Forecast)
     - Pink shaded area (Confidence Range)
   ✓ Forecast Details table
   ✓ Model Performance section (R² Score, MAPE, Trend)
   
5. Take screenshot showing the complete forecast view

6. Save as: exhibit6_forecast.png

Key Elements to Show:
- Interactive forecast horizon control
- Multi-line forecast chart with confidence interval
- Model accuracy metrics (R², MAPE)
- Future revenue predictions table

Annotation Ideas:
- Arrow to confidence band: "95% confidence interval"
- Box around R² score: "Model accuracy: 0.XX"
- Highlight trend: "Revenue trajectory indicator"
"""

# ====================================================================
# TOOLS FOR SCREENSHOTS
# ====================================================================

screenshot_tools = """
RECOMMENDED SCREENSHOT TOOLS:

1. Built-in (Free):
   Mac: Cmd + Shift + 4 (select area) or Cmd + Shift + 5 (screenshot app)
   Windows: Win + Shift + S (Snipping Tool)

2. Browser Extensions (For full-page scrolling):
   - Awesome Screenshot (Chrome/Edge/Firefox)
   - FireShot (Chrome)
   - GoFullPage (Chrome)
   
3. Professional Tools:
   - Snagit ($50, free trial) - Best for annotations
   - CleanShot X (Mac, $29) - Clean, scrolling screenshots
   - ShareX (Windows, Free) - Advanced screenshot tool

4. Quick Tips:
   ✓ Use 100% zoom (Cmd+0 or Ctrl+0)
   ✓ Hide bookmarks bar (Cmd+Shift+B)
   ✓ Use Incognito mode for clean interface
   ✓ Take screenshots in PNG format (not JPEG)
   ✓ Minimum 1920x1080 resolution
"""

# ====================================================================
# CREATING DIAGRAMS (Exhibits 1 & 2)
# ====================================================================

diagram_tools = """
DIAGRAM CREATION TOOLS:

Exhibit 1: System Architecture
- Option A: Mermaid.live (https://mermaid.live/) - EASIEST!
  → Copy code from architecture_diagram.md
  → Paste into editor
  → Download PNG
  
- Option B: draw.io (https://app.diagrams.net/)
  → Manual creation with shapes
  → More customizable
  
- Option C: PowerPoint
  → Use SmartArt → Process
  → Add text and connectors

Exhibit 2: Database Schema
- Option A: Mermaid.live - RECOMMENDED!
  → Copy code from database_schema_diagram.md
  → Instant ER diagram
  
- Option B: dbdiagram.io (https://dbdiagram.io/)
  → Paste schema code
  → Export PNG
  
- Option C: MySQL Workbench
  → Database → Reverse Engineer
  → Export diagram
"""

# ====================================================================
# FINAL ASSEMBLY CHECKLIST
# ====================================================================

final_checklist = """
FINAL ASSEMBLY CHECKLIST:

□ Exhibit 1: System Architecture Diagram (from Mermaid/draw.io)
□ Exhibit 2: Database Schema Diagram (from Mermaid/dbdiagram.io)
□ Exhibit 3: Overview Dashboard Screenshot (1920x1080 min)
□ Exhibit 4: Revenue Analysis Screenshot (full page scroll)
□ Exhibit 5: Inventory Dashboard Screenshot (showing tabs)
□ Exhibit 6: Forecast Dashboard Screenshot (with chart)

Assembly Steps:
1. Create folder: LBIA_Exhibits/
2. Save all 6 exhibits as PNG files
3. Open PowerPoint or Word
4. Create 6 pages, one per exhibit
5. Title each page: "Exhibit X: [Name]"
6. Insert image (Insert → Picture)
7. Add caption below image explaining what's shown
8. Export as PDF: File → Export → Create PDF
9. Name file: LBIA_Project_Exhibits.pdf

Quality Checks:
✓ All images are clear and readable
✓ Text in screenshots is legible
✓ Diagrams show all components
✓ File size under 10MB
✓ PDF has 6 pages (one per exhibit)
✓ Each exhibit is properly labeled

Submission:
- Include exhibits PDF in your final ZIP file
- Reference exhibits in your 4-page report text
- Example: "See Exhibit 3 for the Overview dashboard interface"
"""

# ====================================================================
# PRINT ALL INSTRUCTIONS
# ====================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("LBIA PROJECT - EXHIBIT CREATION GUIDE")
    print("=" * 70)
    print()
    print(exhibit_3_instructions)
    print("\n" + "=" * 70 + "\n")
    print(exhibit_4_instructions)
    print("\n" + "=" * 70 + "\n")
    print(exhibit_5_instructions)
    print("\n" + "=" * 70 + "\n")
    print(exhibit_6_instructions)
    print("\n" + "=" * 70 + "\n")
    print(screenshot_tools)
    print("\n" + "=" * 70 + "\n")
    print(diagram_tools)
    print("\n" + "=" * 70 + "\n")
    print(final_checklist)
    print("\n" + "=" * 70)
    print("Good luck with your submission! 🎉")
    print("=" * 70)
