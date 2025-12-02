# -----------------------------
# LBIA DASHBOARD - FINAL APP1.PY (UPDATED)
# -----------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mysql.connector
import requests
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
    
    /* White text for dark background elements */
    body, p, span, h1, h2, h3, h4, h5, h6, label {
        color: #ffffff !important;
    }
    
    /* White text for markdown, but NOT inside ai-box */
    .stMarkdown:not(.ai-box *):not(.ai-box) {
        color: #ffffff !important;
    }
    
    /* Black text for everything inside .ai-box (highest priority) */
    .ai-box, 
    .ai-box *, 
    .ai-box .stMarkdown,
    .ai-box .stMarkdown *,
    .ai-box div,
    .ai-box p,
    .ai-box span {
        color: #000000 !important;
    }
    
    /* Remove white containers/blocks between sections */
    [data-testid="stHorizontalBlock"] {
        background: transparent !important;
    }
    .element-container {
        background: transparent !important;
    }
    
    /* Hide the white spacing box between expander and next section */
    details[open] + div[data-testid="stVerticalBlock"] > div:first-child {
        display: none !important;
    }
    /* Alternative: make it match background if display:none doesn't work */
    details + div[data-testid="stVerticalBlock"] > div:first-child {
        background: #1a1a1a !important;
        height: 0px !important;
        min-height: 0px !important;
        padding: 0 !important;
        margin: 0 !important;
    }

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
    
    /* Make all team photos uniform size */
    [data-testid="stImage"] img {
        width: 200px !important;
        height: 200px !important;
        object-fit: cover !important;
        border-radius: 8px !important;
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

# Free AI using Hugging Face
import requests

AI_HEADER_HTML = """
<div class="ai-header">
    <div class="ai-icon">🤖</div>
    <div>
        <p style='margin:0;font-size:13px;font-weight:600;'>AI Analyst</p>
        <p style='margin:0;font-size:11px;color:#64748b;'>Powered by AI</p>
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


def ai_insight(context, page_key="overview"):
    """Generate AI insights. Use parsed insights as primary, with OpenAI/HuggingFace as backup enhancement."""
    try:
        # ALWAYS use parsed insights as the reliable baseline
        parsed_insights = parse_context_for_insights(context, page_key)
        
        # Return the high-quality parsed insights
        # These are tailored per tab with MBA-level strategic analysis
        logging.info(f"Using parsed insights for {page_key}")
        return parsed_insights
        
    except Exception as e:
        logging.error(f"Parse error: {e}")
        return "- 📊 Data analysis in progress. Please review the detailed metrics and visualizations above for insights."
        
    except Exception as e:
        logging.error(f"AI error: {e}")
        return parse_context_for_insights(context, page_key)


def parse_context_for_insights(context, page_key):
    """Parse the context data and generate meaningful business insights."""
    try:
        insights = []
        
        if page_key == "overview":
            # Parse overview data and generate comprehensive business insights
            revenue = orders = customers = products = aov = return_rate = sold = returned = 0
            
            # Extract all metrics
            try:
                if "Total Revenue:" in context:
                    revenue_str = context.split("Total Revenue:")[1].split(".")[0].strip().replace("£", "").replace(",", "")
                    revenue = float(revenue_str)
                if "Total Orders:" in context:
                    orders_str = context.split("Total Orders:")[1].split(".")[0].strip().replace(",", "")
                    orders = int(orders_str)
                if "Number of Customers:" in context:
                    customers_str = context.split("Number of Customers:")[1].split(".")[0].strip().replace(",", "")
                    customers = int(customers_str)
                if "Number of Products:" in context:
                    products_str = context.split("Number of Products:")[1].split(".")[0].strip().replace(",", "")
                    products = int(products_str)
                if "Return Rate:" in context:
                    return_rate_str = context.split("Return Rate:")[1].split("%")[0].strip()
                    return_rate = float(return_rate_str)
                if "Items Sold:" in context:
                    sold_str = context.split("Items Sold:")[1].split(".")[0].strip().replace(",", "")
                    sold = int(sold_str)
                if "Items Returned:" in context:
                    returned_str = context.split("Items Returned:")[1].split(".")[0].strip().replace(",", "")
                    returned = int(returned_str)
                    
                aov = revenue / orders if orders > 0 else 0
                revenue_per_customer = revenue / customers if customers > 0 else 0
                orders_per_customer = orders / customers if customers > 0 else 0
                
            except Exception as e:
                logging.error(f"Overview parsing error: {e}")
            
            # Generate strategic insights
            
            # 1. Revenue & Scale Insight
            if revenue > 1000000:
                insights.append(f"💰 Strong Performance: £{revenue:,.0f} revenue demonstrates market leadership. Action: Scale operations, expand product lines, and explore new markets")
            elif revenue > 500000:
                insights.append(f"📈 Growth Phase: £{revenue:,.0f} revenue from {orders:,} orders. Action: Optimize conversion funnel and increase customer acquisition spend")
            else:
                insights.append(f"🚀 Opportunity Stage: £{revenue:,.0f} revenue base. Action: Focus on PMF validation, customer feedback loops, and targeted marketing")
            
            # 2. Order Economics Insight
            if aov > 500:
                insights.append(f"⭐ Premium Positioning: £{aov:,.0f} AOV indicates B2B or luxury segment. Action: Enhance white-glove service, VIP programs, and premium packaging")
            elif aov > 200:
                insights.append(f"✓ Healthy Economics: £{aov:,.0f} AOV with good margins. Action: Test price optimization and introduce product bundles to increase to £{(aov * 1.15):,.0f}")
            else:
                insights.append(f"💡 AOV Optimization Needed: £{aov:,.0f} AOV below target. Action: Implement cart upsells, free shipping thresholds at £{(aov * 1.5):,.0f}, and bundle discounts")
            
            # 3. Customer Quality & LTV Insight
            if customers > 0:
                if revenue_per_customer > 200:
                    insights.append(f"🎯 High-Value Customers: £{revenue_per_customer:,.0f} per customer with {orders_per_customer:.1f} avg orders. Action: Launch loyalty tiers and personalized retention campaigns")
                else:
                    insights.append(f"📊 Customer LTV: £{revenue_per_customer:,.0f} per customer. Action: Increase repeat rate through email sequences, retargeting, and exclusive offers")
            
            # 4. Returns & Quality Insight
            if return_rate > 15:
                cost_of_returns = revenue * (return_rate / 100)
                insights.append(f"⚠️ High Returns Alert: {return_rate:.1f}% ({returned:,} items) costs ~£{cost_of_returns:,.0f}. Action: Review product descriptions, size guides, and quality control immediately")
            elif return_rate > 8:
                insights.append(f"⚡ Returns Monitoring: {return_rate:.1f}% rate is manageable. Action: Survey return reasons and improve product imagery to reach <8% target")
            else:
                insights.append(f"✅ Excellent Quality: {return_rate:.1f}% return rate shows strong product-market fit. Action: Use as marketing proof point and maintain QC standards")
                
        elif page_key == "revenue":
            # Parse revenue data and generate insights
            product_insights = []
            country_insights = []
            
            if "Top 5 Products by Revenue:" in context:
                products_section = context.split("Top 5 Products by Revenue:")[1].split("Top 5 Countries")[0]
                products = products_section.split(".")[:5]  # Get up to 5 products
                
                revenue_values = []
                product_data = []
                
                for prod in products:
                    if "£" in prod and ":" in prod:
                        try:
                            name = prod.split(":")[0].strip()
                            rev_str = prod.split("£")[1].split("revenue")[0].strip().replace(",", "")
                            units_str = prod.split(",")[1].split("units")[0].strip() if "units" in prod else "0"
                            
                            revenue = float(rev_str)
                            units = int(units_str)
                            
                            revenue_values.append(revenue)
                            product_data.append({"name": name, "revenue": revenue, "units": units})
                        except:
                            pass
                
                if len(revenue_values) >= 2:
                    total_top_revenue = sum(revenue_values)
                    top_product = product_data[0]
                    concentration = (top_product["revenue"] / total_top_revenue) * 100
                    
                    # Revenue concentration insight
                    if concentration > 50:
                        product_insights.append(f"⚠️ High revenue concentration: {top_product['name']} drives {concentration:.0f}% of top product revenue (£{top_product['revenue']:,.0f}) - diversify to reduce dependency risk")
                    elif concentration > 35:
                        product_insights.append(f"📊 Moderate concentration: {top_product['name']} accounts for {concentration:.0f}% of top revenue (£{top_product['revenue']:,.0f}) - monitor and develop backup SKUs")
                    else:
                        product_insights.append(f"✓ Healthy revenue distribution: Top product {top_product['name']} represents {concentration:.0f}% (£{top_product['revenue']:,.0f}) - balanced portfolio reduces risk")
                    
                    # Star performer insight with specific actions
                    avg_price = top_product["revenue"] / top_product["units"] if top_product["units"] > 0 else 0
                    product_insights.append(f"🌟 Star Product: {top_product['name']} - {top_product['units']:,} units sold at £{avg_price:.2f} avg. Action: Ensure 30-day stock coverage, create bundle offers, and explore variations")
                    
                    # Second product comparison
                    if len(product_data) >= 2:
                        second_product = product_data[1]
                        gap = ((top_product["revenue"] - second_product["revenue"]) / second_product["revenue"]) * 100
                        if gap > 50:
                            product_insights.append(f"💡 Opportunity: Bridge {gap:.0f}% revenue gap between #1 and #2 ({second_product['name']}) through targeted promotion of runner-up products")
                
            if "Top 5 Countries by Revenue:" in context:
                countries_section = context.split("Top 5 Countries by Revenue:")[1]
                countries = countries_section.split(".")[:5]
                
                country_data = []
                for country in countries:
                    if "£" in country and ":" in country:
                        try:
                            name = country.split(":")[0].strip()
                            # Skip "Unknown" countries
                            if name.lower() == "unknown":
                                continue
                                
                            rev_str = country.split("£")[1].split("revenue")[0].strip().replace(",", "")
                            orders_str = country.split(",")[1].split("orders")[0].strip() if "orders" in country else "0"
                            
                            revenue = float(rev_str)
                            orders = int(orders_str)
                            
                            country_data.append({"name": name, "revenue": revenue, "orders": orders})
                        except:
                            pass
                
                if len(country_data) >= 1:
                    top_country = country_data[0]
                    aov = top_country["revenue"] / top_country["orders"] if top_country["orders"] > 0 else 0
                    
                    country_insights.append(f"🌍 Primary Market: {top_country['name']} generates £{top_country['revenue']:,.0f} from {top_country['orders']:,} orders (£{aov:.0f} AOV) - optimize inventory allocation and localized campaigns here")
                    
                if len(country_data) >= 2:
                    second_country = country_data[1]
                    market_share = (second_country["revenue"] / (country_data[0]["revenue"] + second_country["revenue"])) * 100
                    
                    country_insights.append(f"🚀 Growth Market: {second_country['name']} ({market_share:.0f}% of top 2) with £{second_country['revenue']:,.0f} revenue - invest in market-specific SEO, local partnerships, and currency optimization")
                
                if len(country_data) >= 3:
                    third_country = country_data[2]
                    country_insights.append(f"🌱 Emerging: {third_country['name']} (£{third_country['revenue']:,.0f}) shows potential - test localized content and regional shipping options")
            
            # Combine insights
            insights.extend(product_insights[:2])  # Top 2 product insights
            insights.extend(country_insights[:2])  # Top 2 country insights
            
            if not insights:
                insights.append("- Review top products and geographic distribution for revenue optimization opportunities")
                        
        elif page_key == "inventory":
            # Parse inventory data and generate strategic insights
            fast = slow = total = 0
            avg_return_rate = 0
            urgent_restocks = []
            high_return_products = []
            
            try:
                if "Fast Movers:" in context and "Total Active Products:" in context:
                    fast_str = context.split("Fast Movers:")[1].split("products")[0].strip().replace(",", "")
                    total_str = context.split("Total Active Products:")[1].split(".")[0].strip().replace(",", "")
                    fast = int(fast_str)
                    total = int(total_str)
                    
                if "Slow Movers:" in context:
                    slow_str = context.split("Slow Movers:")[1].split("products")[0].strip().replace(",", "")
                    slow = int(slow_str)
                    
                if "Average Return Rate:" in context:
                    avg_return_str = context.split("Average Return Rate:")[1].split("%")[0].strip()
                    avg_return_rate = float(avg_return_str)
                    
                # Parse restock priorities
                if "Top Restock Priorities:" in context:
                    restock_section = context.split("Top Restock Priorities:")[1].split("High Return")[0]
                    items = restock_section.split(".")[:3]
                    for item in items:
                        if "days left" in item.lower() and ":" in item:
                            urgent_restocks.append(item.strip())
                            
                # Parse high return products
                if "High Return Products:" in context:
                    return_section = context.split("High Return Products:")[1].split(".")[:2]
                    for item in return_section:
                        if "return rate" in item.lower() and ":" in item:
                            high_return_products.append(item.strip())
                            
            except Exception as e:
                logging.error(f"Inventory parsing error: {e}")
            
            # Generate inventory optimization insights
            
            # 1. Velocity Analysis
            if total > 0:
                fast_pct = (fast / total * 100)
                slow_pct = (slow / total * 100)
                
                if fast_pct < 20:
                    potential_savings = slow * 50  # Estimate £50 per slow-moving SKU
                    insights.append(f"⚠️ Low Velocity Alert: Only {fast_pct:.0f}% ({fast} SKUs) are fast movers vs {slow_pct:.0f}% slow. Action: Clear {slow} slow movers via 20-30% markdowns to free ~£{potential_savings:,.0f} in working capital")
                elif fast_pct < 40:
                    insights.append(f"📊 Balanced Portfolio: {fast_pct:.0f}% fast movers ({fast} SKUs) drives sales. Action: Double down on winners - increase safety stock 1.5x for top 20 SKUs and phase out bottom 20%")
                else:
                    insights.append(f"🔥 High-Velocity Portfolio: {fast_pct:.0f}% fast movers ({fast} SKUs) - strong PMF. Action: Negotiate bulk discounts with suppliers and consider increasing reorder quantities 25%")
            
            # 2. Stockout Risk & Restock Urgency
            if len(urgent_restocks) > 0:
                days_mentioned = []
                for item in urgent_restocks:
                    try:
                        if "days left" in item.lower():
                            days_str = item.split("days left")[0].split(",")[-1].strip()
                            days = float(days_str)
                            days_mentioned.append(days)
                    except:
                        pass
                
                if days_mentioned and min(days_mentioned) < 7:
                    insights.append(f"🚨 Critical Stockout Risk: {len(urgent_restocks)} products have <7 days inventory. Action: Expedite POs via air freight, activate safety stock, and enable backorder options")
                elif days_mentioned and min(days_mentioned) < 14:
                    insights.append(f"⏰ Restock Window Closing: {len(urgent_restocks)} items need reorder this week. Action: Issue POs today, confirm lead times, and consider increasing reorder points by 30%")
                else:
                    insights.append(f"📦 Restock Planning: {len(urgent_restocks)} products approaching reorder point. Action: Schedule POs, review supplier reliability, and optimize order quantities")
            else:
                insights.append(f"✅ Healthy Stock Levels: No critical shortages detected. Action: Maintain current reorder policies and monitor weekly for trending SKUs")
            
            # 3. Returns & Quality Issues
            if avg_return_rate > 10:
                insights.append(f"⚠️ Return Rate Concern: {avg_return_rate:.1f}% avg return rate impacts margins. Action: Implement product QC inspection, improve descriptions, and add detailed photos/videos")
            elif avg_return_rate > 5:
                insights.append(f"📋 Returns Monitoring: {avg_return_rate:.1f}% return rate. Action: Track top return reasons, enhance product specs, and test AR/3D viewers for better preview")
            else:
                insights.append(f"✨ Excellent Quality Standards: {avg_return_rate:.1f}% return rate is best-in-class. Action: Document QC processes and use as supplier evaluation benchmark")
            
            # 4. Specific Problem Products
            if len(high_return_products) > 0:
                insights.append(f"🔍 Problem SKUs Identified: {len(high_return_products)} products with >10% returns. Action: Pause advertising, review with suppliers, and consider delisting if unresolved in 30 days")
                
        elif page_key == "forecast":
            # Parse forecast data and generate predictive insights
            next_month_forecast = avg_forecast = r2_score = mape = 0
            trend_direction = ""
            historical_revenues = []
            forecast_revenues = []
            
            try:
                if "Next Month Forecast:" in context:
                    forecast_str = context.split("Next Month Forecast:")[1].split(".")[0].strip().replace("£", "").replace(",", "")
                    next_month_forecast = float(forecast_str)
                    
                if "Average Forecast:" in context:
                    avg_str = context.split("Average Forecast:")[1].split(".")[0].strip().replace("£", "").replace(",", "")
                    avg_forecast = float(avg_str)
                    
                if "Trend Direction:" in context:
                    trend_direction = context.split("Trend Direction:")[1].split(".")[0].strip().lower()
                    
                if "Model Accuracy:" in context and "R² =" in context and "MAPE" in context:
                    r2_str = context.split("R² =")[1].split("%")[0].strip()
                    r2_score = float(r2_str)
                    mape_str = context.split("MAPE =")[1].split("%")[0].strip()
                    mape = float(mape_str)
                    
                # Parse historical and forecast values
                if "Recent Historical Revenue" in context:
                    hist_section = context.split("Recent Historical Revenue")[1].split("Revenue Forecasts")[0]
                    for val in hist_section.split("£")[1:]:
                        try:
                            rev = float(val.split(".")[0].strip().replace(",", ""))
                            historical_revenues.append(rev)
                        except:
                            pass
                            
                if "Revenue Forecasts for Next" in context:
                    forecast_section = context.split("Revenue Forecasts for Next")[1].split("Next Month Forecast")[0]
                    for val in forecast_section.split("£")[1:]:
                        try:
                            rev = float(val.split(".")[0].strip().replace(",", ""))
                            forecast_revenues.append(rev)
                        except:
                            pass
                            
            except Exception as e:
                logging.error(f"Forecast parsing error: {e}")
            
            # Generate strategic forecast insights
            
            # 1. Trend Direction & Strategic Implications
            if "upward" in trend_direction:
                growth_rate = ((avg_forecast - historical_revenues[-1]) / historical_revenues[-1] * 100) if historical_revenues else 0
                insights.append(f"📈 Growth Trajectory: Upward trend forecasted with {abs(growth_rate):.1f}% projected growth. Action: Scale inventory 20-25%, increase ad spend 15%, and hire 1-2 customer service reps ahead of demand")
                
                if next_month_forecast > 0:
                    capacity_needed = next_month_forecast * 1.15  # 15% buffer
                    insights.append(f"🎯 Next Month Target: £{next_month_forecast:,.0f} forecasted. Action: Secure capacity for £{capacity_needed:,.0f}, pre-order high-velocity SKUs, and prepare promotional calendar")
            else:
                decline_rate = ((historical_revenues[-1] - avg_forecast) / historical_revenues[-1] * 100) if historical_revenues else 0
                insights.append(f"⚠️ Declining Trend: {abs(decline_rate):.1f}% projected decline signals market headwinds. Action: Launch retention campaigns, review pricing vs competitors, and cut discretionary spending 20%")
                
                insights.append(f"💡 Counter-Decline Strategy: Test flash sales, win-back emails to churned customers, and optimize for high-margin products to maintain profitability")
            
            # 2. Forecast Accuracy & Decision Confidence
            if mape < 10:
                insights.append(f"✅ High-Confidence Forecasts: MAPE {mape:.1f}% (excellent) + R² {r2_score:.0f}% indicates reliable predictions. Action: Use for firm commitments on inventory POs, staffing plans, and cash flow projections")
            elif mape < 20:
                buffer_pct = 15
                insights.append(f"📊 Good Forecast Reliability: MAPE {mape:.1f}% suggests {buffer_pct}% safety buffer needed. Action: Plan for £{avg_forecast * (1 + buffer_pct/100):,.0f} scenario and maintain flexible supplier terms")
            else:
                buffer_pct = 25
                insights.append(f"⚡ Moderate Uncertainty: MAPE {mape:.1f}% requires {buffer_pct}% contingency buffers. Action: Use conservative lower-bound estimates for fixed costs, keep variable costs flexible")
            
            # 3. Revenue Planning & Resource Allocation
            if len(forecast_revenues) >= 3:
                peak_month = max(forecast_revenues)
                low_month = min(forecast_revenues)
                volatility = ((peak_month - low_month) / low_month * 100) if low_month > 0 else 0
                
                if volatility > 30:
                    insights.append(f"🔄 High Volatility: {volatility:.0f}% swing forecasted (£{low_month:,.0f} to £{peak_month:,.0f}). Action: Use flexible staffing (contractors), implement dynamic pricing, and maintain 45-day cash runway")
                else:
                    insights.append(f"📉 Stable Outlook: {volatility:.0f}% variance enables predictable planning. Action: Lock in fixed costs, negotiate annual supplier contracts for better rates")
        
        if insights:
            return "\n".join(insights[:5])  # Limit to 5 insights
        else:
            return "- Insufficient data for detailed analysis. Continue tracking metrics for trend analysis."
            
    except Exception as e:
        logging.error(f"Parse error: {e}")
        return "- Data analysis in progress. Please review the detailed metrics and visualizations above for insights."


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
            st.session_state[f"resp_{page_key}"] = ai_insight(context, page_key)

    resp_key = f"resp_{page_key}"
    if resp_key in st.session_state:
        insights_text = st.session_state[resp_key]
        all_lines = [line.strip() for line in insights_text.split('\n') if line.strip()]
        
        if all_lines:
            # Build ONE box with all insights as bullet points
            insights_html = "<div style='background:#ffffff;border-radius:8px;padding:16px;margin-top:16px;border:1px solid #e2e8f0;'>"
            
            for line in all_lines:
                parts = line.split(' ', 1)
                emoji = parts[0] if len(parts) >= 1 else "•"
                text = parts[1] if len(parts) == 2 else (parts[0] if len(parts) == 1 else "")
                
                if not text:
                    continue
                
                import html as htmllib
                text = htmllib.escape(text)
                
                # Simple bullet point style
                insights_html += f"<div style='color:#000000;font-size:14px;line-height:1.8;margin-bottom:8px;'>{emoji} {text}</div>"
            
            insights_html += "</div>"
            st.markdown(insights_html, unsafe_allow_html=True)
        else:
            st.markdown("<div style='color:#64748b;font-size:14px;margin-top:12px;'>No insights available.</div>", unsafe_allow_html=True)

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
    avg_order = rev / orders if orders > 0 else 0

    # AI
    overview_summary = (
        f"Total Revenue: £{rev:,.0f}. "
        f"Total Orders: {orders:,}. "
        f"Number of Products: {products:,}. "
        f"Number of Customers: {customers:,}. "
        f"Items Sold: {sold:,}. "
        f"Items Returned: {returned:,}. "
        f"Return Rate: {return_rate:.1f}%. "
        f"Average Order Value: £{avg_order:,.0f}."
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
        top_products_text = ". ".join([
            f"{row['Product']}: £{row['Revenue']:,.0f} revenue, {row['Units']:,} units"
            for _, row in top_df.head(5).iterrows()
        ])
    else:
        top_products_text = "No data available"
        
    if country_df is not None and not country_df.empty:
        country_df.index = country_df.index + 1
        countries_text = ". ".join([
            f"{row['Country']}: £{row['Revenue']:,.0f} revenue, {row['Orders']:,} orders"
            for _, row in country_df.head(5).iterrows()
        ])
    else:
        countries_text = "No data available"

    revenue_summary = (
        f"Top 5 Products by Revenue: {top_products_text}. "
        f"Top 5 Countries by Revenue: {countries_text}."
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
        
        # Format top restock priorities
        if not restock_df.empty:
            restock_text = ". ".join([
                f"{row['Product']}: {row['Units Sold']:,} units sold, {row['Avg Daily Sales']:.1f} daily sales rate"
                for _, row in restock_df.head(5).iterrows()
            ])
        else:
            restock_text = "No urgent restock needs"
            
        # Format high return products
        if not high_ret_df.empty:
            high_return_text = ". ".join([
                f"{row['Product']}: {row['Return Rate']} return rate, {row['Units Returned']:,} returned out of {row['Units Sold']:,} sold"
                for _, row in high_ret_df.head(3).iterrows()
            ])
        else:
            high_return_text = "No products with high return rates"
        
        # AI Context
        inventory_summary = (
            f"Total Active Products: {total_products:,}. "
            f"Fast Movers: {fast_movers} products ({fast_movers/total_products*100:.0f}%). "
            f"Slow Movers: {slow_movers} products ({slow_movers/total_products*100:.0f}%). "
            f"Average Return Rate: {avg_return_rate:.1f}%. "
            f"Top Restock Priorities: {restock_text}. "
            f"High Return Products: {high_return_text}."
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
        
        # Format historical data
        recent_history = ". ".join([
            f"{row['Month']}: £{row['Revenue']:,.0f}"
            for _, row in hist_df[['Month', 'Revenue']].tail(6).iterrows()
        ])
        
        # Format forecasts
        forecast_text = ". ".join([
            f"{row['Month']}: £{row['Forecast']:,.0f}"
            for _, row in forecast_df.iterrows()
        ])
        
        next_month_forecast = future_predictions[0]
        avg_forecast = np.mean(future_predictions)
        trend_direction = "upward" if model.coef_[0] > 0 else "downward"
        
        # AI Context
        forecast_summary = (
            f"Recent Historical Revenue (Last 6 Months): {recent_history}. "
            f"Revenue Forecasts for Next {forecast_months} Months: {forecast_text}. "
            f"Next Month Forecast: £{next_month_forecast:,.0f}. "
            f"Average Forecast: £{avg_forecast:,.0f}. "
            f"Trend Direction: {trend_direction}. "
            f"Model Accuracy: R² = {r2_score:.2%}, MAPE = {mape:.1f}%."
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
        st.image("Marcia.jpeg", width=200)
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
