# -----------------------------
# LBIA DASHBOARD - FINAL APP1.PY (UPDATED)
# -----------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mysql.connector
from openai import OpenAI
import logging

# Logging
logging.basicConfig(level=logging.INFO)

# Page config
st.set_page_config(
    page_title="LBIA Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove default top padding
st.markdown("<style>.block-container {padding-top: 0 !important;}</style>", unsafe_allow_html=True)

# Global CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    * {font-family: 'Inter', sans-serif;}

    [data-testid="stSidebar"] {display:none;}
    #MainMenu, footer, header {visibility:hidden;}
    .stApp {background:#1a1a1a;}
    * {color: #ffffff !important;}

    /* Hero */
    .hero {
        background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%);
        border-radius: 16px;
        padding: 36px 40px;
        margin-bottom: 4px;
        min-height: 140px;
    }
    .hero-chip {
        display:inline-block;
        background:rgba(255,255,255,0.15);
        color:white;
        padding:6px 14px;
        border-radius:20px;
        font-size:12px;
        font-weight:500;
    }
    .hero-title {color:white;font-size:28px;font-weight:700;margin:8px 0 4px 0;}
    .hero-desc {color:rgba(255,255,255,0.85);font-size:15px;max-width:600px;}

    /* All buttons rectangular (nav + Run Analysis) */
    .stButton > button {
        background: linear-gradient(135deg,#3b82f6,#2563eb);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 6px 18px;
        font-weight: 500;
        font-size: 13px;
    }
    .stButton > button:hover {
        box-shadow: 0 4px 12px rgba(59,130,246,0.35);
    }

    /* AI Box */
    .ai-box {
        background:white;
        border-radius:12px;
        border:1px solid #e2e8f0;
        padding:20px 24px;
        margin-top:16px;
        margin-bottom:48px;
    }
    .ai-box * {color: #0f172a !important;}
    .ai-header {display:flex;gap:12px;align-items:center;margin-bottom:0;}
    .ai-icon {
        width:36px;height:36px;
        background:linear-gradient(135deg,#3b82f6,#6366f1);
        border-radius:8px;color:white !important;
        display:flex;align-items:center;justify-content:center;
    }
    .ai-response {
        background:#f8fafc;border-left:3px solid #3b82f6;
        padding:16px;border-radius:8px;margin-top:12px;
        font-size:14px;white-space:pre-wrap;line-height:1.6;
        color: #0f172a !important;
    }
    .ai-response * {color: #0f172a !important;}
    .ai-response p {color: #0f172a !important;}
    .ai-response div {color: #0f172a !important;}

    /* Run Analysis – same style but scoped inside AI box if you want to tweak further later */
    .ai-box .stButton > button {
        border-radius: 8px;
        padding: 6px 18px;
        font-size: 13px;
        min-width: 120px;
    }

    /* Dataframe/Table Styling */
    [data-testid="stDataFrame"] {
        background: white !important;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #e2e8f0;
    }
    /* Force all dataframe elements to black */
    [data-testid="stDataFrame"],
    [data-testid="stDataFrame"] *,
    [data-testid="stDataFrame"] div,
    [data-testid="stDataFrame"] span,
    [data-testid="stDataFrame"] button,
    [data-testid="stDataFrame"] input,
    [data-testid="stDataFrame"] label,
    [data-testid="stDataFrame"] p {
        color: #0f172a !important;
    }
    div[data-testid="stDataFrame"] table {
        font-size: 13px;
        background: white !important;
    }
    div[data-testid="stDataFrame"] th {
        background: #f8fafc !important;
        font-weight: 600 !important;
        padding: 12px 8px !important;
        border-bottom: 2px solid #e2e8f0 !important;
        color: #0f172a !important;
    }
    div[data-testid="stDataFrame"] td {
        padding: 10px 8px !important;
        border-bottom: 1px solid #f1f5f9 !important;
        color: #0f172a !important;
    }
    div[data-testid="stDataFrame"] tr:hover {
        background: #f8fafc !important;
    }
    /* Column header controls and icons */
    [data-testid="stDataFrame"] button,
    [data-testid="stDataFrame"] button * {
        color: #0f172a !important;
    }
    [data-testid="stDataFrame"] svg,
    [data-testid="stDataFrame"] svg * {
        color: #0f172a !important;
        fill: #0f172a !important;
        stroke: #0f172a !important;
    }
    /* Dropdown menus */
    div[role="menu"],
    div[role="menu"] *,
    div[role="menuitem"],
    div[role="menuitem"] * {
        background: white !important;
        color: #0f172a !important;
    }
    /* Popover/tooltip backgrounds */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] * {
        background: white !important;
        color: #0f172a !important;
    }

    /* Remove any card effect around images (About page) */
    [data-testid="stImage"] {
        background: transparent !important;
        padding: 0 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }

    /* We are not using text inputs so hide the big input pill if any */
    div[data-baseweb="input"] {
        display: none;
    }
    
    /* Professional section divider */
    .section-divider {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(to right, transparent, #64748b, transparent) !important;
        margin: 32px 0 !important;
        opacity: 0.4 !important;
    }
    
    /* Hide default Streamlit hr styling */
    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(to right, transparent, #64748b, transparent) !important;
        margin: 32px 0 !important;
        opacity: 0.4 !important;
    }
</style>
""", unsafe_allow_html=True)

# DB CONFIG (unchanged)
DB_CONFIG = {
    'host': st.secrets["database"]["host"],
    'port': st.secrets["database"]["port"],
    'database': st.secrets["database"]["database"],
    'user': st.secrets["database"]["user"],
    'password': st.secrets["database"]["password"]
}

# OpenAI
OPENAI_API_KEY = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=OPENAI_API_KEY)

AI_HEADER_HTML = """
<div class="ai-header">
    <div class="ai-icon">🤖</div>
    <div>
        <p style='margin:0;font-size:13px;font-weight:600;'>AI Analyst</p>
        <p style='margin:0;font-size:11px;color:#64748b;'>Powered by GPT</p>
    </div>
</div>
"""

# Utility functions
def safe_value(df, default=0):
    try:
        if df is not None and not df.empty:
            return df.iloc[0, 0]
    except Exception:
        pass
    return default


@st.cache_data(ttl=300)
def get_data(q):
    conn = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return pd.read_sql(q, conn)
    except mysql.connector.Error as db_err:
        st.error(f"Database connection error: Unable to retrieve data. Please check your connection.")
        logging.error(f"DB Error: {db_err}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error retrieving data: {str(e)}")
        logging.error(f"Data retrieval error: {e}")
        return pd.DataFrame()
    finally:
        if conn and conn.is_connected():
            conn.close()


def ai_insight(context):
    try:
        out = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Provide plain text insights only. No markdown, no **, no #. "
                        "Use at most 5 bullet points starting with '- '. "
                        "Do not nest sub-bullets."
                    )
                },
                {"role": "user", "content": f"Analyze this dashboard area:\n{context}"}
            ],
            max_tokens=350
        )
        return out.choices[0].message.content
    except Exception as e:
        logging.error(f"AI error: {e}")
        return f"AI temporarily unavailable. Error: {str(e)}"


def render_ai(page_key, description, context):
    st.markdown("<div class='ai-box'>", unsafe_allow_html=True)

    header_col, button_col, _ = st.columns([3, 1, 6])

    with header_col:
        st.markdown(AI_HEADER_HTML, unsafe_allow_html=True)
        st.markdown(
            f"<p style='font-size:12px;color:#64748b;margin-top:4px;'>{description}</p>",
            unsafe_allow_html=True
        )

    with button_col:
        if st.button("Run Analysis", key=f"btn_{page_key}", use_container_width=True):
            st.session_state[f"resp_{page_key}"] = ai_insight(context)

    resp_key = f"resp_{page_key}"
    if resp_key in st.session_state:
        st.markdown(f"<div class='ai-response'>{st.session_state[resp_key]}</div>",
                    unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# Navigation state
if "page" not in st.session_state:
    st.session_state.page = "Overview"

# Navigation bar
nav_cols = st.columns([2.5, 1, 1, 1, 1, 1, 1.5, 1])

with nav_cols[0]:
    # logo + brand
    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;">
        <div style="
            width:36px;height:36px;
            border-radius:12px;
            background:linear-gradient(135deg,#3b82f6,#6366f1);
            display:flex;align-items:center;justify-content:center;
            color:white;font-weight:700;font-size:18px;">
            L
        </div>
        <div>
            <div style="font-size:18px;font-weight:700;">LBIA</div>
            <div style="font-size:11px;color:#64748b;margin-top:-2px;">Business Intelligence</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with nav_cols[1]:
    if st.button("Overview"):
        st.session_state.page = "Overview"
with nav_cols[2]:
    if st.button("Revenue"):
        st.session_state.page = "Revenue"
with nav_cols[3]:
    if st.button("Inventory"):
        st.session_state.page = "Inventory"
with nav_cols[4]:
    if st.button("Forecast"):
        st.session_state.page = "Forecast"
with nav_cols[5]:
    if st.button("About"):
        st.session_state.page = "About"

st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

page = st.session_state.page

# -----------------------------
# OVERVIEW
# -----------------------------
if page == "Overview":

    st.markdown("""
    <div class='hero'>
        <span class='hero-chip'>AI-Powered Business Intelligence</span>
        <h1 class='hero-title'>Overview</h1>
        <p class='hero-desc'>Real-time retail metrics and AI insights.</p>
    </div>
    """, unsafe_allow_html=True)

 # CSV UPLOAD SECTION
    with st.expander("📤 Upload New Data", expanded=False):
        st.markdown("Upload a CSV file with the same format as Online Retail II dataset.")
        
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Columns needed: Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country"
        )
        
        if uploaded_file is not None:
            if st.button("Process & Load Data", key="upload_btn"):
                with st.spinner("Processing your data..."):
                    try:
                        # Read CSV
                        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
                        
                        # Validate columns
                        required_cols = ['Invoice', 'StockCode', 'Description', 'Quantity', 
                                    'InvoiceDate', 'Price', 'Customer ID', 'Country']
                        missing = [col for col in required_cols if col not in df.columns]
                        
                        if missing:
                            st.error(f"Missing columns: {', '.join(missing)}")
                        else:
                            # Clean data - HANDLE NaN VALUES
                            df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
                            df['Customer ID'] = df['Customer ID'].fillna(0).astype(int)
                            df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
                            df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
                            df['Description'] = df['Description'].fillna('Unknown Product')
                            df['Country'] = df['Country'].fillna('Unknown')
                            df['StockCode'] = df['StockCode'].fillna('UNKNOWN').astype(str).str.strip().str.upper()
                            
                            # Remove cancelled invoices and nulls
                            df = df[~df['Invoice'].astype(str).str.startswith('C', na=False)]
                            df = df.dropna(subset=['Price', 'Invoice', 'InvoiceDate', 'Quantity'])
                            
                            # Flag returns
                            df['is_return'] = df['Quantity'] < 0
                            
                            st.info(f"Cleaned data: {len(df)} rows ready to load")
                            
                            # Insert into database
                            conn = mysql.connector.connect(**DB_CONFIG)
                            cursor = conn.cursor()
                            
                            # Insert customers
                            customers = df[df['Customer ID'] > 0].groupby('Customer ID').agg({
                                'Country': 'first',
                                'InvoiceDate': 'min',
                                'Invoice': 'count'
                            }).reset_index()
                            customers.columns = ['customer_id', 'country', 'first_transaction_date', 'total_orders']
                            
                            for _, row in customers.iterrows():
                                cursor.execute("""
                                    INSERT INTO customers (customer_id, country, first_transaction_date, total_orders)
                                    VALUES (%s, %s, %s, %s)
                                    ON DUPLICATE KEY UPDATE total_orders = total_orders + VALUES(total_orders)
                                """, tuple(row))
                            
                            # Insert products
                            products = df.drop_duplicates(subset='StockCode')[['StockCode', 'Description']].copy()
                            products['category'] = products['Description'].astype(str).str.split().str[0]
                            
                            for _, row in products.iterrows():
                                cursor.execute("""
                                    INSERT IGNORE INTO products (stock_code, description, category)
                                    VALUES (%s, %s, %s)
                                """, (str(row['StockCode']), str(row['Description']), str(row['category'])))
                            
                            # Get product_id mapping
                            cursor.execute("SELECT product_id, stock_code FROM products")
                            product_map = {stock_code: product_id for product_id, stock_code in cursor.fetchall()}
                            
                            # Insert transactions and items
                            success_count = 0
                            for invoice_no, group in df.groupby('Invoice'):
                                customer_id = int(group['Customer ID'].iloc[0])
                                invoice_date = group['InvoiceDate'].iloc[0]
                                total_amount = float((group['Quantity'] * group['Price']).sum())
                                
                                cursor.execute("""
                                    INSERT INTO transactions (invoice_no, customer_id, invoice_date, total_amount)
                                    VALUES (%s, %s, %s, %s)
                                """, (str(invoice_no), customer_id, invoice_date, total_amount))
                                
                                transaction_id = cursor.lastrowid
                                
                                for _, row in group.iterrows():
                                    product_id = product_map.get(row['StockCode'])
                                    if product_id:
                                        cursor.execute("""
                                            INSERT INTO transaction_items 
                                            (transaction_id, product_id, quantity, unit_price, is_return, line_total)
                                            VALUES (%s, %s, %s, %s, %s, %s)
                                        """, (
                                            transaction_id, product_id, int(row['Quantity']),
                                            float(row['Price']), bool(row['is_return']),
                                            float(row['Quantity'] * row['Price'])
                                        ))
                                        success_count += 1
                            
                            conn.commit()
                            cursor.close()
                            conn.close()
                            
                            st.success(f"✅ Successfully loaded {success_count} transaction items!")
                            st.cache_data.clear()
                            st.rerun()
                            
                    except Exception as e:
                        st.error(f"Error processing file: {str(e)}")
                        logging.error(f"Upload error: {e}")

    st.markdown("<div style='height:1px;background:linear-gradient(to right,transparent,rgba(100,116,139,0.3),transparent);margin:40px 0;'></div>", unsafe_allow_html=True)

    # Metrics
    rev = safe_value(get_data("SELECT SUM(line_total) FROM transaction_items WHERE is_return=0"))
    orders = int(safe_value(get_data("SELECT COUNT(*) FROM transactions")))
    products = int(safe_value(get_data("SELECT COUNT(*) FROM products")))
    customers = int(safe_value(get_data("SELECT COUNT(*) FROM customers WHERE customer_id!=0")))

    qty_df = get_data("""
        SELECT 
        SUM(CASE WHEN is_return=0 THEN quantity ELSE 0 END) AS sold,
        SUM(CASE WHEN is_return=1 THEN ABS(quantity) ELSE 0 END) AS returned
        FROM transaction_items
    """)
    sold = safe_value(qty_df[["sold"]])
    returned = safe_value(qty_df[["returned"]])
    return_rate = returned / (sold + returned) * 100 if sold + returned > 0 else 0

    # AI
    overview_summary = (
        f"Revenue £{rev}, Orders {orders}, Products {products}, Customers {customers}, "
        f"Sold {sold}, Returned {returned}."
    )
    render_ai("overview", "AI insights for your overall business performance.", overview_summary)

    a, b, c, d = st.columns(4)
    a.metric("Total Revenue", f"£{rev:,.0f}")
    b.metric("Total Orders", f"{orders:,}")
    c.metric("Products", f"{products:,}")
    d.metric("Customers", f"{customers:,}")

    e, f, _, _ = st.columns(4)
    e.metric("Avg Order Value", f"£{(rev / orders if orders > 0 else 0):,.0f}")
    f.metric("Return Rate", f"{return_rate:.1f}%")

    st.markdown("""
The overview gives you a quick read on overall health - revenue, orders, product breadth, and customer base.
You can check this daily to catch sudden drops in orders, unusual return spikes, or changes in average order
value that might signal pricing or promotion issues.
    """)

    # Overview chart - monthly revenue
    trend_df = get_data("""
        SELECT DATE_FORMAT(t.invoice_date,'%Y-%m') AS Month,
               SUM(ti.line_total) AS Revenue
        FROM transactions t
        JOIN transaction_items ti ON t.transaction_id=ti.transaction_id
        WHERE ti.is_return=0
        GROUP BY Month
        ORDER BY Month
    """)
    if trend_df is not None and not trend_df.empty:
        st.subheader("Monthly Revenue Trend")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=trend_df["Month"],
            y=trend_df["Revenue"],
            mode="lines+markers",
            line=dict(color="#3b82f6", width=2.5)
        ))
        fig.update_layout(height=320, plot_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# REVENUE PAGE
# -----------------------------
elif page == "Revenue":

    st.markdown("""
    <div class='hero'>
        <span class='hero-chip'>Revenue Analytics</span>
        <h1 class='hero-title'>Revenue Performance</h1>
        <p class='hero-desc'>Analyze product revenue, customer geography, and purchasing behavior.</p>
    </div>
    """, unsafe_allow_html=True)

    top_df = get_data("""
        SELECT p.description AS Product,
               SUM(ti.quantity) AS Units,
               SUM(ti.line_total) AS Revenue
        FROM transaction_items ti
        JOIN products p ON ti.product_id=p.product_id
        WHERE ti.is_return=0
        GROUP BY p.product_id
        ORDER BY Units DESC
        LIMIT 10
    """)

    country_df = get_data("""
        SELECT c.country AS Country,
               COUNT(DISTINCT t.transaction_id) AS Orders,
               SUM(ti.line_total) AS Revenue
        FROM customers c
        JOIN transactions t ON c.customer_id=t.customer_id
        JOIN transaction_items ti ON t.transaction_id=ti.transaction_id
        WHERE ti.is_return=0
        GROUP BY c.country
        ORDER BY Revenue DESC
        LIMIT 10
    """)

    if top_df is not None and not top_df.empty:
        top_df.index = top_df.index + 1
    if country_df is not None and not country_df.empty:
        country_df.index = country_df.index + 1

    revenue_summary = (
        f"Top products:\n{top_df.to_string() if top_df is not None and not top_df.empty else 'No data'}\n\n"
        f"Revenue by country:\n{country_df.to_string() if country_df is not None and not country_df.empty else 'No data'}"
    )
    render_ai("revenue", "AI commentary on your revenue distribution.", revenue_summary)

    st.markdown("""
This page shows where money is actually coming from - which products drive the most revenue and
which countries contribute most to your top line. You can use it to decide which SKUs to feature,
bundle together, or avoid discounting too heavily.
    """)

    # bar chart for top products
    if top_df is not None and not top_df.empty:
        st.subheader("Top Products by Revenue")
        fig_bar = px.bar(top_df, x="Product", y="Revenue")
        fig_bar.update_layout(
            xaxis_tickangle=-45, 
            height=320,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#0f172a'),
            xaxis=dict(
                showgrid=True,
                gridcolor='#f1f5f9',
                title_font=dict(color='#0f172a'),
                tickfont=dict(color='#0f172a')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#f1f5f9',
                title_font=dict(color='#0f172a'),
                tickfont=dict(color='#0f172a')
            ),
            hoverlabel=dict(
                bgcolor="white",
                font_color="#0f172a"
            )
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top Products by Revenue")
        if top_df is not None and not top_df.empty:
            # Format the dataframe
            display_df = top_df.copy()
            display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"£{x:,.2f}")
            display_df['Units'] = display_df['Units'].apply(lambda x: f"{int(x):,}")
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=False,
                column_config={
                    "Product": st.column_config.TextColumn("Product", width="medium"),
                    "Units": st.column_config.TextColumn("Units", width="small"),
                    "Revenue": st.column_config.TextColumn("Revenue", width="small")
                }
            )
        else:
            st.info("No data available")
    with col2:
        st.subheader("Revenue by Country")
        if country_df is not None and not country_df.empty:
            # Format the dataframe
            display_df2 = country_df.copy()
            display_df2['Revenue'] = display_df2['Revenue'].apply(lambda x: f"£{x:,.2f}")
            display_df2['Orders'] = display_df2['Orders'].apply(lambda x: f"{int(x):,}")
            st.dataframe(
                display_df2,
                use_container_width=True,
                hide_index=False,
                column_config={
                    "Country": st.column_config.TextColumn("Country", width="medium"),
                    "Orders": st.column_config.TextColumn("Orders", width="small"),
                    "Revenue": st.column_config.TextColumn("Revenue", width="small")
                }
            )
        else:
            st.info("No data available")

# -----------------------------
# INVENTORY PAGE
# -----------------------------
elif page == "Inventory":

    st.markdown("""
    <div class='hero'>
        <span class='hero-chip'>Inventory Optimization</span>
        <h1 class='hero-title'>Inventory Intelligence</h1>
        <p class='hero-desc'>Data-driven restocking, turnover analysis, and inventory health monitoring.</p>
    </div>
    """, unsafe_allow_html=True)

    # Calculate inventory metrics
    inventory_metrics = get_data("""
        SELECT 
            p.product_id,
            COALESCE(p.description, CONCAT('Product #', p.stock_code)) AS Product,
            p.stock_code,
            SUM(CASE WHEN ti.is_return=0 THEN ti.quantity ELSE 0 END) AS Total_Sold,
            SUM(CASE WHEN ti.is_return=1 THEN ABS(ti.quantity) ELSE 0 END) AS Total_Returned,
            COUNT(DISTINCT t.transaction_id) AS Order_Frequency,
            DATEDIFF(MAX(t.invoice_date), MIN(t.invoice_date)) AS Days_Active,
            AVG(ti.unit_price) AS Avg_Price
        FROM products p
        JOIN transaction_items ti ON p.product_id = ti.product_id
        JOIN transactions t ON ti.transaction_id = t.transaction_id
        GROUP BY p.product_id, p.description, p.stock_code
        HAVING Total_Sold > 0
    """)

    if inventory_metrics is not None and not inventory_metrics.empty:
        # Calculate advanced metrics
        inventory_metrics['Daily_Sales_Rate'] = inventory_metrics['Total_Sold'] / inventory_metrics['Days_Active'].replace(0, 1)
        inventory_metrics['Return_Rate'] = (inventory_metrics['Total_Returned'] / inventory_metrics['Total_Sold'] * 100).round(1)
        inventory_metrics['Revenue'] = inventory_metrics['Total_Sold'] * inventory_metrics['Avg_Price']
        
        # Inventory classification
        high_velocity_threshold = inventory_metrics['Daily_Sales_Rate'].quantile(0.75)
        low_velocity_threshold = inventory_metrics['Daily_Sales_Rate'].quantile(0.25)
        
        inventory_metrics['Velocity_Class'] = inventory_metrics['Daily_Sales_Rate'].apply(
            lambda x: 'Fast Mover' if x >= high_velocity_threshold 
            else 'Slow Mover' if x <= low_velocity_threshold 
            else 'Medium Mover'
        )
        
        # Reorder recommendations (fast movers)
        restock_df = inventory_metrics[
            inventory_metrics['Velocity_Class'] == 'Fast Mover'
        ].sort_values('Daily_Sales_Rate', ascending=False)[['Product', 'Total_Sold', 'Daily_Sales_Rate', 'Revenue']].head(15)
        
        restock_df['Daily_Sales_Rate'] = restock_df['Daily_Sales_Rate'].round(1)
        restock_df['Revenue'] = restock_df['Revenue'].apply(lambda x: f"£{x:,.0f}")
        restock_df.columns = ['Product', 'Units Sold', 'Avg Daily Sales', 'Revenue']
        
        # Slow movers
        slow_df = inventory_metrics[
            inventory_metrics['Velocity_Class'] == 'Slow Mover'
        ].sort_values('Daily_Sales_Rate')[['Product', 'Total_Sold', 'Daily_Sales_Rate', 'Order_Frequency']].head(15)
        
        slow_df['Daily_Sales_Rate'] = slow_df['Daily_Sales_Rate'].round(2)
        slow_df.columns = ['Product', 'Units Sold', 'Avg Daily Sales', 'Order Frequency']
        
        # High return products
        high_ret_df = inventory_metrics[
            inventory_metrics['Return_Rate'] > 10
        ].sort_values('Return_Rate', ascending=False)[['Product', 'Total_Sold', 'Total_Returned', 'Return_Rate']].head(15)
        
        high_ret_df['Return_Rate'] = high_ret_df['Return_Rate'].apply(lambda x: f"{x}%")
        high_ret_df.columns = ['Product', 'Units Sold', 'Units Returned', 'Return Rate']
        
        # Overall inventory health metrics
        total_products = len(inventory_metrics)
        fast_movers = len(inventory_metrics[inventory_metrics['Velocity_Class'] == 'Fast Mover'])
        slow_movers = len(inventory_metrics[inventory_metrics['Velocity_Class'] == 'Slow Mover'])
        avg_return_rate = inventory_metrics['Return_Rate'].mean()
        
        # AI Context
        inventory_summary = (
            f"Inventory Overview:\n"
            f"- Total Active Products: {total_products}\n"
            f"- Fast Movers: {fast_movers} ({fast_movers/total_products*100:.0f}%)\n"
            f"- Slow Movers: {slow_movers} ({slow_movers/total_products*100:.0f}%)\n"
            f"- Average Return Rate: {avg_return_rate:.1f}%\n\n"
            f"Top restock priorities:\n{restock_df.head(5).to_string(index=False)}\n\n"
            f"High return products (>10% return rate):\n{high_ret_df.head(5).to_string(index=False) if not high_ret_df.empty else 'None'}"
        )
        
        render_ai("inventory", "AI recommendations for inventory optimization and risk management.", inventory_summary)
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Active Products", f"{total_products:,}")
        col2.metric("Fast Movers", f"{fast_movers} ({fast_movers/total_products*100:.0f}%)")
        col3.metric("Slow Movers", f"{slow_movers} ({slow_movers/total_products*100:.0f}%)")
        col4.metric("Avg Return Rate", f"{avg_return_rate:.1f}%")
        
        st.markdown("""
        **Inventory Intelligence:** Products are classified by sales velocity (daily sales rate). Fast movers need 
        frequent restocking, slow movers may need discounting or delisting. High return rates indicate quality issues 
        or customer mismatches that require investigation.
        """)
        
        # Velocity distribution chart
        st.subheader("Inventory Velocity Distribution")
        
        velocity_counts = inventory_metrics['Velocity_Class'].value_counts()
        fig_velocity = px.pie(
            values=velocity_counts.values,
            names=velocity_counts.index,
            color=velocity_counts.index,
            color_discrete_map={'Fast Mover': '#22c55e', 'Medium Mover': '#eab308', 'Slow Mover': '#ef4444'}
        )
        fig_velocity.update_traces(textposition='inside', textinfo='percent+label')
        fig_velocity.update_layout(
            height=300, 
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#0f172a'),
            xaxis=dict(
                showgrid=True,
                gridcolor='#f1f5f9',
                title_font=dict(color='#0f172a'),
                tickfont=dict(color='#0f172a')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#f1f5f9',
                title_font=dict(color='#0f172a'),
                tickfont=dict(color='#0f172a')
            ),
            hoverlabel=dict(
                bgcolor="white",
                font_color="#0f172a"
            )
        )
        st.plotly_chart(fig_velocity, use_container_width=True)
        
        # Top movers by revenue
        st.subheader("Top Revenue Generators (Fast Movers)")
        # Filter out generic products like "Manual" and get top 10
        top_revenue = inventory_metrics[
            ~inventory_metrics['Product'].str.upper().isin(['MANUAL', 'ADJUST', 'ADJUSTMENT', 'POSTAGE', 'DOTCOM'])
        ].nlargest(10, 'Revenue')[['Product', 'Total_Sold', 'Revenue', 'Daily_Sales_Rate']].copy()
        
        # Debug: show the data values
        st.write(f"Revenue range: £{top_revenue['Revenue'].min():,.2f} to £{top_revenue['Revenue'].max():,.2f}")
        
        # Sort by revenue for better display
        top_revenue = top_revenue.sort_values('Revenue', ascending=True)
        
        fig_revenue = px.bar(
            top_revenue,
            x='Revenue',
            y='Product',
            orientation='h',
            color='Revenue',
            color_continuous_scale='Blues',
            labels={'Revenue': 'Total Revenue (£)'},
            text='Revenue'
        )
        fig_revenue.update_traces(texttemplate='£%{text:,.0f}', textposition='outside')
        fig_revenue.update_layout(
            height=400, 
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color='#0f172a'),
            xaxis=dict(
                showgrid=True,
                gridcolor='#f1f5f9',
                title='Total Revenue (£)',
                title_font=dict(color='#0f172a'),
                tickfont=dict(color='#0f172a')
            ),
            yaxis=dict(
                showgrid=False,
                title='',
                title_font=dict(color='#0f172a'),
                tickfont=dict(color='#0f172a')
            ),
            hoverlabel=dict(
                bgcolor="white",
                font_color="#0f172a"
            )
        )
        fig_revenue.update_coloraxes(showscale=False)
        st.plotly_chart(fig_revenue, use_container_width=True)
        
        # Detailed tables
        tabs = st.tabs(["🔄 Restock Priority", "🐌 Slow Movers", "⚠️ High Returns", "📊 All Products"])
        
        with tabs[0]:
            st.markdown("**Fast-moving products requiring frequent replenishment**")
            if not restock_df.empty:
                restock_df.index = range(1, len(restock_df) + 1)
                st.dataframe(restock_df, use_container_width=True)
            else:
                st.info("No high-velocity products identified.")
        
        with tabs[1]:
            st.markdown("**Low-velocity products - consider discounting or delisting**")
            if not slow_df.empty:
                slow_df.index = range(1, len(slow_df) + 1)
                st.dataframe(slow_df, use_container_width=True)
            else:
                st.info("No slow-moving products identified.")
        
        with tabs[2]:
            st.markdown("**Products with return rates >10% - investigate quality or fit issues**")
            if not high_ret_df.empty:
                high_ret_df.index = range(1, len(high_ret_df) + 1)
                st.dataframe(high_ret_df, use_container_width=True)
            else:
                st.success("No products with concerning return rates.")
        
        with tabs[3]:
            st.markdown("**Complete inventory analysis**")
            all_products = inventory_metrics[['Product', 'Total_Sold', 'Daily_Sales_Rate', 'Return_Rate', 'Velocity_Class', 'Revenue']].copy()
            all_products['Daily_Sales_Rate'] = all_products['Daily_Sales_Rate'].round(2)
            all_products['Revenue'] = all_products['Revenue'].apply(lambda x: f"£{x:,.0f}")
            all_products.columns = ['Product', 'Units Sold', 'Daily Sales', 'Return Rate %', 'Category', 'Revenue']
            all_products.index = range(1, len(all_products) + 1)
            st.dataframe(all_products, use_container_width=True, height=400)
    
    else:
        st.warning("No inventory data available.")

# -----------------------------
# FORECAST PAGE
# -----------------------------
elif page == "Forecast":
    from sklearn.linear_model import LinearRegression
    import numpy as np

    st.markdown("""
    <div class='hero'>
        <span class='hero-chip'>Predictive Analytics</span>
        <h1 class='hero-title'>Sales Forecasting</h1>
        <p class='hero-desc'>ML-powered revenue predictions with accuracy metrics.</p>
    </div>
    """, unsafe_allow_html=True)

    # Get historical monthly data
    hist_df = get_data("""
        SELECT DATE_FORMAT(t.invoice_date,'%Y-%m') AS Month,
               SUM(ti.line_total) AS Revenue
        FROM transactions t
        JOIN transaction_items ti ON t.transaction_id=ti.transaction_id
        WHERE ti.is_return=0
        GROUP BY Month
        ORDER BY Month
    """)

    if hist_df is not None and not hist_df.empty and len(hist_df) >= 3:
        # Prepare data for model
        hist_df['month_num'] = range(len(hist_df))
        X = hist_df[['month_num']].values
        y = hist_df['Revenue'].values
        
        # Train Linear Regression model
        model = LinearRegression()
        model.fit(X, y)
        
        # Calculate model accuracy (R² score)
        r2_score = model.score(X, y)
        
        # Predict historical values for visualization
        hist_df['Predicted'] = model.predict(X)
        
        # Calculate MAPE (Mean Absolute Percentage Error)
        mape = np.mean(np.abs((y - hist_df['Predicted']) / y)) * 100
        
        # Interactive forecast horizon selector
        st.subheader("Forecast Settings")
        forecast_months = st.slider(
            "Select forecast horizon (months ahead):",
            min_value=1,
            max_value=6,
            value=3,
            help="Choose how many months to predict into the future"
        )
        
        # Generate future predictions
        last_month_num = hist_df['month_num'].max()
        future_months = range(last_month_num + 1, last_month_num + 1 + forecast_months)
        future_X = np.array(future_months).reshape(-1, 1)
        future_predictions = model.predict(future_X)
        
        # Create forecast dataframe
        last_month_str = hist_df['Month'].max()
        try:
            last_period = pd.Period(last_month_str, freq="M")
            future_labels = [(last_period + i).strftime("%Y-%m") for i in range(1, forecast_months + 1)]
        except:
            future_labels = [f"Month +{i}" for i in range(1, forecast_months + 1)]
        
        forecast_df = pd.DataFrame({
            'Month': future_labels,
            'Forecast': future_predictions
        })
        
        # AI Context
        forecast_summary = (
            f"Historical data (last 6 months):\n{hist_df[['Month', 'Revenue']].tail(6).to_string(index=False)}\n\n"
            f"Forecasts for next {forecast_months} months:\n{forecast_df.to_string(index=False)}\n\n"
            f"Model Accuracy: R² = {r2_score:.2%}, MAPE = {mape:.1f}%"
        )
        render_ai("forecast", "AI interpretation of revenue trends and forecast reliability.", forecast_summary)
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        next_month_forecast = future_predictions[0]
        avg_forecast = np.mean(future_predictions)
        trend = "Upward ↗" if model.coef_[0] > 0 else "Downward ↘"
        confidence = "High" if mape < 10 else "Medium" if mape < 20 else "Low"
        
        col1.metric("Next Month Forecast", f"£{next_month_forecast:,.0f}")
        col2.metric(f"{forecast_months}-Month Avg", f"£{avg_forecast:,.0f}")
        col3.metric("Trend Direction", trend)
        col4.metric("Forecast Confidence", f"{confidence} ({100-mape:.0f}%)")
        
        st.markdown("""
        **How it works:** The model uses Linear Regression to learn from your historical monthly revenue 
        and projects future performance. R² measures how well the model fits your data (closer to 100% = better). 
        MAPE shows average prediction error (lower = more accurate).
        """)
        
        # Visualization
        st.subheader("Historical Performance & Forecast")
        
        fig = go.Figure()
        
        # Historical actual revenue
        fig.add_trace(go.Scatter(
            x=hist_df['Month'], 
            y=hist_df['Revenue'],
            mode='lines+markers',
            name='Actual Revenue',
            line=dict(color='#3b82f6', width=2.5),
            marker=dict(size=6)
        ))
        
        # Historical predicted (model fit)
        fig.add_trace(go.Scatter(
            x=hist_df['Month'],
            y=hist_df['Predicted'],
            mode='lines',
            name='Model Fit',
            line=dict(color='#93c5fd', width=1.5, dash='dot'),
            opacity=0.7
        ))
        
        # Future forecast
        fig.add_trace(go.Scatter(
            x=forecast_df['Month'],
            y=forecast_df['Forecast'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#ef4444', width=2.5, dash='dash'),
            marker=dict(size=8, symbol='diamond')
        ))
        
        # Add confidence band (±10%)
        upper_bound = future_predictions * 1.1
        lower_bound = future_predictions * 0.9
        
        fig.add_trace(go.Scatter(
            x=forecast_df['Month'] + forecast_df['Month'][::-1].tolist(),
            y=upper_bound.tolist() + lower_bound[::-1].tolist(),
            fill='toself',
            fillcolor='rgba(239, 68, 68, 0.1)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Confidence Range (±10%)',
            showlegend=True
        ))
        
        fig.update_layout(
            height=400,
            plot_bgcolor='white',
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast table
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.subheader("Forecast Details")
            forecast_display = forecast_df.copy()
            forecast_display['Forecast'] = forecast_display['Forecast'].apply(lambda x: f"£{x:,.0f}")
            forecast_display.index = range(1, len(forecast_display) + 1)
            st.dataframe(forecast_display, use_container_width=True)
        
        with col_b:
            st.subheader("Model Performance")
            metrics_df = pd.DataFrame({
                'Metric': ['R² Score', 'MAPE', 'Trend Coefficient', 'Data Points Used'],
                'Value': [
                    f"{r2_score:.2%}",
                    f"{mape:.1f}%",
                    f"£{model.coef_[0]:,.0f}/month",
                    f"{len(hist_df)} months"
                ]
            })
            st.dataframe(metrics_df, use_container_width=True, hide_index=True)
    
    else:
        st.warning("Insufficient data for forecasting. Need at least 3 months of historical data.")

# -----------------------------
# ABOUT PAGE
# -----------------------------
elif page == "About":

    st.markdown("""
    <div class='hero'>
        <span class='hero-chip'>About LBIA</span>
        <h1 class='hero-title'>Our Mission</h1>
        <p class='hero-desc'>AI-powered intelligence for small and medium retail businesses.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("What We Do")
    st.write("""
LBIA (Local Business Intelligence Assistant) helps small and medium retailers turn raw transaction data
into decisions using real-time dashboards, forecasting, and AI-generated recommendations.
    """)

    st.markdown("<div style='height:1px;background:linear-gradient(to right,transparent,rgba(100,116,139,0.3),transparent);margin:40px 0;'></div>", unsafe_allow_html=True)
    st.subheader("Founding Team")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("<div style='text-align:center;display:flex;flex-direction:column;align-items:center;'>", unsafe_allow_html=True)
        st.image("Simran.png", width=200)
        st.markdown("<p style='margin-top:10px;margin-bottom:0;'><strong>Simran Verma</strong><br/>Co-Founder</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div style='text-align:center;display:flex;flex-direction:column;align-items:center;'>", unsafe_allow_html=True)
        st.image("Shiv.jpeg", width=200)
        st.markdown("<p style='margin-top:10px;margin-bottom:0;'><strong>Shiv Uppal</strong><br/>Co-Founder</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div style='text-align:center;display:flex;flex-direction:column;align-items:center;'>", unsafe_allow_html=True)
        st.image("Alvaro.jpg", width=200)
        st.markdown("<p style='margin-top:10px;margin-bottom:0;'><strong>Alvaro Rojas</strong><br/>Co-Founder</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown("<div style='text-align:center;display:flex;flex-direction:column;align-items:center;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:140px;line-height:200px;height:200px;'>👩</div>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:10px;margin-bottom:0;'><strong>Marcia Rivera</strong><br/>Co-Founder</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:#64748b;font-size:12px;'>© 2025 LBIA — All Rights Reserved</p>",
    unsafe_allow_html=True
)
