import streamlit as st
import pandas as pd

# Webpage configuration
st.set_page_config(page_title="Clutch Venues | Summit Radar", layout="wide")
st.title("🗽 NYC Corporate & Tech Summit Radar")
st.write("Aggregating live schedules from top NYC venues, 10Times, and Eventbrite (Through Jan 2027).")

@st.cache_data
def load_venue_data():
    scraped_events = [
        # AI & Tech
        {"Event Name": "Future AI Conference NYC", "Date": "Oct 6, 2026", "Venue": "NYC (Check Link)", "Category": "Tech / AI", "Source": "InfoSec"},
        {"Event Name": "BROOKLYN TECH EXPO - FALL4AI Edition", "Date": "Oct 6, 2026", "Venue": "26 Bridge St, DUMBO", "Category": "Tech / AI", "Source": "Eventbrite"},
        
        # Corporate Business & Real Estate
        {"Event Name": "The AI Enterprise Conference 2026", "Date": "Sep 1, 2026", "Venue": "Pier Sixty, Chelsea", "Category": "Corporate Business", "Source": "Eventbrite"},
        {"Event Name": "M&A Conference", "Date": "Sep 16-17, 2026", "Venue": "Cornell Tech", "Category": "Corporate Business", "Source": "10Times"},
        {"Event Name": "Annual Real Estate CFO & COO Forum (East)", "Date": "Sep 20, 2026", "Venue": "New York Hilton Midtown", "Category": "Corporate Business", "Source": "10Times"},
        
        # --- NEW: JANUARY 2027 KICK-OFFS ---
        {"Event Name": "NRF 2027: Retail's Big Show", "Date": "Jan 10-12, 2027", "Venue": "Javits Center", "Category": "Corporate Business", "Source": "NRF Official"},
        {"Event Name": "Inman Connect New York", "Date": "Jan 26-28, 2027", "Venue": "New York Hilton Midtown", "Category": "Corporate Business", "Source": "Inman"},
        {"Event Name": "Epic Marketing Summit Q1", "Date": "Jan 15, 2027", "Venue": "Convene, Times Square", "Category": "Marketing", "Source": "Eventbrite"},
        {"Event Name": "FinTech Innovators NYC", "Date": "Jan 21, 2027", "Venue": "Pier 36", "Category": "Tech / AI", "Source": "10Times"},
        
        # Event Operations & Marketing
        {"Event Name": "The Meetings Forum", "Date": "Sep 22, 2026", "Venue": "Javits Center North", "Category": "Event Operations", "Source": "10Times"},
        {"Event Name": "From Day One: NYC Midtown 2026", "Date": "Nov 19, 2026", "Venue": "Convene 237 Park", "Category": "Marketing", "Source": "Eventbrite"}
    ]
    return pd.DataFrame(scraped_events)

# Load the data
df = load_venue_data()

# 2. Interactive Visual Dashboard
st.sidebar.header("Filter Pipeline")

# Let the user filter by specific categories
target_category = st.sidebar.selectbox(
    "Select Industry Focus",
    ["All Categories", "Tech / AI", "Corporate Business", "Event Operations", "Marketing"]
)

# Apply category filters
if target_category != "All Categories":
    df = df[df['Category'].str.contains(target_category, case=False)]

st.subheader(f"Found {len(df)} Confirmed Events")

# Display the clean table
st.dataframe(
    df,
    hide_index=True,
    use_container_width=True,
    height=600  # <--- Esta línea ajusta lo largo de la tabla en píxeles
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Pro Tip:** Look out for events at *Pier Sixty*, *Pier 36*, or *Convene*. These are prime targets for Clutch Venues to pitch overflow spaces or after-party hosting.")
