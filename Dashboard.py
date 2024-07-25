import streamlit as st
from streamlit_gsheets import GSheetsConnection

#ydata profiling
import pandas as pd
from ydata_profiling import ProfileReport

# report untuk streamlit
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title = "Data Profiler Dashboard",
    page_icon = "📝",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

# ----- Judul Dashboard
#st.title("Data Profiler")
st.markdown("<h1 style='text-align: center;'> Data Profiler App </h1>",
            unsafe_allow_html=True)
st.markdown("---")

# ----- Sidebar
with st.sidebar:
    st.subheader("Promotion Data")
    st.markdown("----")

# ------ Buat Button
if st.sidebar.button("Start Profiling Data"):
    st.write("Report")
    ## read data
    conn = st.connection("gsheet", type = GSheetsConnection)

    df = conn.read(
        spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
        worksheet = st.secrets.gsheet_promotion["worksheet"]
    )
    
    ## Generated Report
    pr = ProfileReport(df)

    st_profile_report(pr)
else:
    st.info("Click bar sebelah kiri")
    