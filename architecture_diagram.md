# System Architecture Diagram - Text for draw.io

## Instructions:
1. Go to https://app.diagrams.net/
2. Create New Diagram → Blank Diagram
3. Use the shapes below and connect them with arrows

## Shapes to Create:

### Layer 1: Data Input
**Rectangle (Blue #3b82f6)**
Text: "CSV Upload\nUser Interface"

↓ Arrow

### Layer 2: Data Validation
**Rectangle (Blue #3b82f6)**
Text: "Data Validation & Cleaning
• Column verification
• NaN handling
• Type conversion
• Date parsing"

↓ Arrow

### Layer 3: Processing
**Rectangle (Blue #3b82f6)**
Text: "Data Processing
• Product mapping
• Return identification
• Customer aggregation
• Transaction linking"

↓ Arrow

### Layer 4: Storage
**Cylinder Database Shape (Gray #64748b)**
Text: "MySQL Database
━━━━━━━━━━━━
customers
products
transactions
transaction_items"

↓ Arrow (splits into 2)

### Layer 5: Application (Two parallel boxes)
**Rectangle (Purple #667eea)**
Text: "Streamlit Caching
@st.cache_data
SQL Query Execution"

**Rectangle (Purple #667eea)**
Text: "Plotly Visualizations
Charts & Graphs
Interactive Metrics"

↓ Arrows (merge into one)

### Layer 6: AI Processing
**Rectangle (Orange #f59e0b)**
Text: "AI Insight Engine
OpenAI GPT-3.5-turbo
Context: Revenue, Inventory
Output: Business insights"

↓ Arrow

### Layer 7: Outputs
**Rectangle (Green #10b981)**
Text: "Dashboard Outputs
• Anomaly alerts
• Churn predictions
• Restock priorities
• Revenue forecasts"

## Alternative: Mermaid Code
Copy this code to https://mermaid.live/ for instant diagram:

```mermaid
graph TD
    A[CSV Upload<br/>User Interface] --> B[Data Validation & Cleaning<br/>• Column verification<br/>• NaN handling<br/>• Type conversion]
    B --> C[Data Processing<br/>• Product mapping<br/>• Return identification<br/>• Customer aggregation]
    C --> D[(MySQL Database<br/>customers | products<br/>transactions | transaction_items)]
    D --> E[Streamlit Caching<br/>@st.cache_data]
    D --> F[Plotly Visualizations<br/>Charts & Graphs]
    E --> G[AI Insight Engine<br/>OpenAI GPT-3.5-turbo]
    F --> G
    G --> H[Dashboard Outputs<br/>• Anomaly alerts<br/>• Churn predictions<br/>• Restock priorities<br/>• Revenue forecasts]
    
    style A fill:#3b82f6,color:#fff
    style B fill:#3b82f6,color:#fff
    style C fill:#3b82f6,color:#fff
    style D fill:#64748b,color:#fff
    style E fill:#667eea,color:#fff
    style F fill:#667eea,color:#fff
    style G fill:#f59e0b,color:#fff
    style H fill:#10b981,color:#fff
```

## Quick Steps for Mermaid:
1. Copy the code above
2. Go to https://mermaid.live/
3. Paste the code
4. Click "Download PNG" or "Download SVG"
5. Use as Exhibit 1
