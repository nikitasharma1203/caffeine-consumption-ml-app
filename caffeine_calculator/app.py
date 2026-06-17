import streamlit as st
import pandas as pd

# Page Configuration with clean browser tab metadata
st.set_page_config(page_title="Caffeine Intake Calculator", layout="wide", page_icon="☕")

# Production UI Custom Theming Injection
st.markdown("""
    <style>
    /* Main App Background Override */
    .stApp {
        background-color: #f5f1e6;
    </style>
""", unsafe_allow_html=True)

# Application Header & Editorial Subtitle
st.markdown("""
# ☕ Brew. Sip. Track.
### *"Because every cup tells a story: make sure yours stays balanced."*
---
""")

# Verified Brand Concentration Profiles (mg of caffeine per 100ml)
caffeine_data = {
    "Tea": {
        "Waghbakri": 20.00, "Lipton": 23.25, "Girnar": 25.00, "Others(Green tea)": 30.00,
        "Tetley": 33.00, "Others(Regular tea)": 35.36, "Tata": 37.00, "Dwarkesh": 37.86, 
        "Red Label": 48.00, "Taj": 58.80, "Tulsi": 0.00
    },
    "Coffee": {
        "MSU Nescafe": 24.08, "Ajay": 38.00, "Others(Regular)": 55.00, "Davidoff": 57.00, 
        "Nescafe": 60.00, "Continental": 62.00, "Amul": 70.00, "Starbucks": 73.00, 
        "Others(Black)": 75.00, "Bru": 80.00, "Sunrise": 90.00
    },
    "Energy Drink": {
        "Sting": 29.00, "Red Bull": 30.00, "Others": 31.00, "Monster": 36.00, 
        "Coca cola": 38.00, "Mountain Dew": 54.00
    }
}

# Session State Initialization
if "drinks" not in st.session_state:
    st.session_state["drinks"] = pd.DataFrame(columns=["Session ID", "Type", "Brand", "Size (ml)", "Servings", "Caffeine (mg)"])

# ----------------- SIDEBAR INTERACTION SECTION -----------------
st.sidebar.header("👤 Profile & Context")
weight = st.sidebar.number_input("Your Weight (kg):", min_value=30, max_value=200, value=70, step=1)

# Biometric parameters driving the ML Advisory Framework
st.sidebar.markdown("---")
st.sidebar.header("🩺 Health Context")
sleep_hours = st.sidebar.slider("Sleep Hours Last Night:", min_value=0, max_value=12, value=7)
focus_state = st.sidebar.selectbox("Current Academic Focus State:", ["Normal Operations", "Exam Preparation Period", "Sustained High-Stress Deadline"])

st.sidebar.markdown("---")
st.sidebar.header("☕ Add Drink Configuration")
drink_type = st.sidebar.selectbox("Drink Type:", list(caffeine_data.keys()))
brand = st.sidebar.selectbox("Brand Variety:", list(caffeine_data[drink_type].keys()))
size = st.sidebar.number_input("Cup Volume Size (ml):", min_value=50, max_value=1000, step=50, value=250)
servings = st.sidebar.number_input("Number of Servings:", min_value=1, max_value=10, value=1)

# Real-time conversion formula based on chemical back-titration research
caffeine_per_100ml = caffeine_data[drink_type][brand]
caffeine_per_cup = (caffeine_per_100ml / 100) * size
total_item_caffeine = caffeine_per_cup * servings

st.sidebar.info(f"💡 Calculated dosage for this entry: **{total_item_caffeine:.2f} mg**")

# Session state action layouts
col_add, col_del = st.sidebar.columns(2)

with col_add:
    if st.button("➕ Add Drink", use_container_width=True):
        new_row = {
            "Session ID": len(st.session_state["drinks"]) + 1,
            "Type": drink_type,
            "Brand": brand,
            "Size (ml)": size,
            "Servings": servings,
            "Caffeine (mg)": round(total_item_caffeine, 2)
        }
        st.session_state["drinks"] = pd.concat(
            [st.session_state["drinks"], pd.DataFrame([new_row])],
            ignore_index=True
        )

with col_del:
    if st.button("🗑️ Undo Last", use_container_width=True):
        if not st.session_state["drinks"].empty:
            st.session_state["drinks"] = st.session_state["drinks"].iloc[:-1]

if st.sidebar.button("🔄 Reset Tracking Matrix", use_container_width=True):
    st.session_state["drinks"] = pd.DataFrame(columns=["Session ID", "Type", "Brand", "Size (ml)", "Servings", "Caffeine (mg)"])


# ----------------- MAIN CORE DASHBOARD DISPLAY -----------------
# 1. Real-time Calculation Pipeline
total_caffeine_logged = st.session_state["drinks"]["Caffeine (mg)"].sum()
safe_daily_threshold = round(2.5 * weight, 2)

# 2. Key Performance Indicators Layout
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric(label="Total Consumed Caffeine", value=f"{total_caffeine_logged:.2f} mg")
with kpi2:
    st.metric(label="Calculated Personal Limit", value=f"{safe_daily_threshold:.2f} mg")
with kpi3:
    remaining_balance = max(0.0, safe_daily_threshold - total_caffeine_logged)
    st.metric(label="Remaining Safe Allowance", value=f"{remaining_balance:.2f} mg", 
              delta=f"-{total_caffeine_logged:.2f} mg" if total_caffeine_logged > 0 else None, delta_color="inverse")

# 3. Dynamic Progress System
progress_factor = min(total_caffeine_logged / safe_daily_threshold if safe_daily_threshold > 0 else 0.0, 1.0)
st.progress(progress_factor)

# 4. Contextual Diagnostics Feedback
if total_caffeine_logged == 0:
    st.info("🎯 Your metric log is empty. Use the sidebar controller to build your tracking matrix.")
elif total_caffeine_logged < safe_daily_threshold:
    st.success(f"✅ Safe Zone: Your current intake is within optimal levels. You have consumed **{progress_factor*100:.1f}%** of your target maximum threshold.")
elif total_caffeine_logged == safe_daily_threshold:
    st.warning("⚖️ Boundary Warning: You have reached your exact safe limit. Additional consumption may cause adverse physiological symptoms.")
else:
    st.error(f"🚨 Overdose Alert: Toxicological threshold breached by **{total_caffeine_logged - safe_daily_threshold:.2f} mg**! Halt intake and increase water consumption.")

# 5. Pipeline Expert Advisory Module
if total_caffeine_logged > 0:
    st.markdown("---")
    st.subheader("🩺 Dynamic Clinical Diagnostic Advisory")
    
    # Conditional logic adapted from your ML clustering and outlier findings
    advise_flags = []
    
    if sleep_hours < 6:
        advise_flags.append("⚠️ **Sleep Deprivation Flag:** High caffeine intake combined with restricted sleep patterns creates severe rebound fatigue cycle risks.")
    if focus_state in ["Exam Preparation Period", "Sustained High-Stress Deadline"] and total_caffeine_logged >= 200:
        advise_flags.append("🚨 **Exam-Spiker Pattern Verified:** You are exhibiting high-stress dependency spikes. Watch out for secondary symptoms like baseline anxiety, jitters, or heart rate fluctuations.")
    if drink_type == "Energy Drink" and total_caffeine_logged > safe_daily_threshold:
        advise_flags.append("❌ **High Sugar/Taurine Interaction Warning:** Energy drinks cause rapid glycemic crashes. Switch to low-dose regular green tea or water.")
        
    if advise_flags:
        for alert in advise_flags:
            st.markdown(alert)
    else:
        st.markdown("🍏 **Systemic Check:** Your current intake matrix shows no immediate metabolic conflict flags.")

# 6. Current Interactive Session Logging Table
st.markdown("---")
st.subheader("📋 Session Log Matrix")
if st.session_state["drinks"].empty:
    st.caption("No beverages logged for the current active tracking matrix window.")
else:
    st.dataframe(st.session_state["drinks"], use_container_width=True, hide_index=True)