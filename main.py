import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="People Analytics Dashboard",
    page_icon="👩‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.header("")
page = st.sidebar.radio(
    "Pages",
    ["Data Understanding",
    "Data Exploration"]
)

# Fungsi load dataset
@st.cache_data
def load_data():
    return pd.read_csv("D:\People Analytics\data\employee_survey.csv")

# Data Understanding
if page == "Data Understanding":
    # Judul
    st.title("Data Understanding")
    st.markdown("""
        Dataset Employee Survey dari Kaggle merupakan kumpulan data hasil survei terhadap karyawan yang
        digunakan untuk menganalisis tingkat kepuasan kerja, keterlibatan karyawan (employee engagement),
        serta faktor-faktor yang dapat memengaruhi produktivitas dan retensi tenaga kerja.     

        Data ini akan dianalisis secara deskriptif dan eksploratif untuk mengidentifikasi pola yang menunjukkan 
        bagaimana berbagai faktor memengaruhi tingkat kepuasan kerja dan keterlibatan karyawan. Melalui penerapan 
        metode statistik dan visualisasi data, hasil survei yang semula bersifat mentah dapat diubah menjadi wawasan
        yang mendalam dan informatif.
                
    """)

    # Load dataset
    st.subheader("Data Employee Survey")
    df = load_data()
    st.dataframe(df)

    # Deskripsi dataset
    st.subheader("Deskripsi Kolom Data")
    # Data deskripsi kolom
    data_dict = {
        "Kolom Data": [
            "emp_id", "gender", "age", "marital_status", "job_level", "experience", "dept", "emp_type",
            "wlb", "work_env", "physical_activity_hours", "workload", "stress", "sleep_hours",
            "commute_mode", "commute_distance", "num_companies", "team_size", "num_reports",
            "edu_level", "have_ot", "training_hours_per_year", "job_satisfaction"
        ],
        "Deskripsi": [
            "Nomor unik setiap karyawan",
            "Jenis kelamin",
            "Umur",
            "Status pernikahan",
            "Tingkatan jabatan",
            "Pengalaman kerja",
            "Departemen tempat karyawan bekerja",
            "Jenis status karyawan dalam perusahaan",
            "Skala ordinal Work-Life Balance",
            "Tingkat kepuasan karyawan terhadap lingkungan kerja",
            "Jumlah jam seseorang melakukan aktivitas fisik dalam periode tertentu",
            "Jumlah pekerjaan atau tugas yang harus diselesaikan dalam jangka waktu tertentu",
            "Tingkat stres karyawan",
            "Rata-rata jam tidur per hari",
            "Moda transportasi ke kantor",
            "Jarak perjalanan ke kantor (dalam km)",
            "Jumlah perusahaan tempat karyawan pernah bekerja sebelumnya",
            "Ukuran tim tempat karyawan bekerja saat ini",
            "Jumlah bawahan langsung (direct reports) karyawan",
            "Tingkat pendidikan terakhir",
            "Apakah karyawan sering lembur (overtime) → True/False",
            "Jumlah rata-rata jam pelatihan yang diikuti karyawan dalam setahun",
            "Tingkat kepuasan kerja karyawan"
        ]
    }
    # Membuat data dict jadi dataframe
    desk_df = pd.DataFrame(data_dict)
    st.dataframe(desk_df)

    # Informasi data
    st.subheader("Informasi Data")
    st.markdown(f"""
        - Jumlah Kolom : {df.shape[1]}
        - Jumlah Baris : {df.shape[0]}              
    """)
    info = pd.DataFrame({
        "Nama Kolom" : df.columns,
        "Tipe Data"  : df.dtypes.values,
        "Jumlah Nilai Unik" : df.nunique().values
    })
    st.dataframe(info)


# Data Exploration
elif page == "Data Exploration":
    df = load_data()
    st.title("Data Exploration")
    st.write("Halaman ini menampilkan analisis dan visualisasi interaktif People Analytics")

    st.sidebar.header("Filter Data")
    pilih_dept = st.sidebar.multiselect("Departemen :",
                                        sorted(df['dept'].unique().tolist()))
    pilih_joblevel = st.sidebar.multiselect("Job Level :",
                                            sorted(df['job_level'].unique().tolist()))
    pilih_satisfaction = st.sidebar.multiselect("Job Satisfaction :",
                                          sorted(df['job_satisfaction'].unique().tolist()))
    filtered = df.copy()
    if pilih_dept:
        filtered = filtered[filtered["dept"].isin(pilih_dept)]
    if pilih_joblevel:
        filtered = filtered[filtered["job_level"].isin(pilih_joblevel)]
    if pilih_satisfaction:
        filtered = filtered[filtered["job_satisfaction"].isin(pilih_satisfaction)]
    
    # KPI employee overview
    st.subheader("Employee Overview")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Total Employees", len(filtered))
    col2.metric("Avg Age", round(filtered["age"].mean(),1))
    col3.metric("Avg Experience", round(filtered["experience"].mean(), 1))
    col4.metric("Avg Stress Level", round(filtered["stress"].mean(), 2))
    col5.metric("Avg WLB Score", round(filtered["wlb"].mean(), 2))
    col6.metric("Avg Job Satisfaction", round(filtered["job_satisfaction"].mean(), 2))

    # Palette
    palette = ["#A8E6CF", "#ABD8FF", "#FFC5EF", "#F9FF9E", "#D8C3FE", "#F0A287", "#C9AF7B", "#B5B9B6"]
    
    # Tab explore data
    tab1, tab2, tab3 = st.tabs(["Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis"])

    # Visualisasi univariate analysis
    with tab1:
        # Job satisfaction column
        st.subheader("Job Satisfaction")
        col1 = st.columns(1)[0]
        with col1:
            hist_target = px.histogram(
                filtered,
                x="job_satisfaction",
                nbins=10,
                color_discrete_sequence=["#A8E6CF"]
            )
            st.plotly_chart(hist_target, use_container_width=True)
        
        # Employees demographics visualization
        st.subheader("Employee Demographics")
        col2, col3 = st.columns(2)
        # Gender
        with col2:
            pie_gender = px.pie(filtered, names="gender",
                                title="Gender Distribution",
                                color_discrete_sequence=["#ABD8FF", "#FFC5EF"] )
            st.plotly_chart(pie_gender, use_container_width=True)

        # Education level
        with col3:
            bar_edulevel = px.bar(filtered["edu_level"].value_counts().reset_index(name="count").rename(columns={"index":"edu_level"}),
                                x="count", y="edu_level", color="edu_level",
                                orientation="h",
                                title="Education Level Distribution",
                                labels={"count":"Employees", "edu_level":"Education Level"},
                                color_discrete_sequence=palette)
            st.plotly_chart(bar_edulevel, use_container_width=True)
        
        # Age column
        col4 = st.columns(1)[0]
        with col4:
            bar_age = px.bar(filtered["age"].value_counts().reset_index(name="count").rename(columns={"index":"age"}),
                                x="age", y="count", color="age",
                                title="Age Distribution",
                                labels={"count":"Employees", "age":"Age"},
                                color_discrete_sequence=palette)
            st.plotly_chart(bar_age, use_container_width=True)

        # Workforce structure visualization
        st.subheader("Workforce Structure")
        col5, col6 = st.columns(2)
        # Department
        with col5:
            bar_dept = px.bar(filtered["dept"].value_counts().reset_index(name="count").rename(columns={"index":"dept"}),
                                x="count", y="dept", color="dept",
                                orientation="h",
                                title="Department Distribution",
                                labels={"count":"Employees", "dept":"Department"},
                                color_discrete_sequence=palette)
            st.plotly_chart(bar_dept, use_container_width=True)
        
        # Job level
        with col6:
            bar_joblevel = px.bar(filtered["job_level"].value_counts().reset_index(name="count").rename(columns={"index":"job_level"}),
                                x="count", y="job_level", color="job_level",
                                orientation="h",
                                title="Job Level Distribution",
                                labels={"count":"Employees", "job_level":"Job Level"},
                                color_discrete_sequence=palette)
            st.plotly_chart(bar_joblevel, use_container_width=True)

        col7, col8 = st.columns(2)
        # Experience
        with col7:
            bar_experience = px.bar(filtered["experience"].value_counts().reset_index(name="count").rename(columns={"index":"experience"}),
                                x="experience", y="count", color="experience",
                                title="Experience Distribution",
                                labels={"count":"Employees", "experience":"Experience"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_experience, use_container_width=True)
        
        # Employee types
        with col8:
            bar_emptype = px.bar(filtered["emp_type"].value_counts().reset_index(name="count").rename(columns={"index":"emp_type"}),
                                x="emp_type", y="count", color="emp_type",
                                title="Employee Types Distribution",
                                labels={"count":"Employees", "emp_type":"Employee Types"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_emptype, use_container_width=True)
        
        # Work-Life & Wellbeing
        st.subheader("Work-Life & Wellbeing")
        col9, col10 = st.columns(2)
        # Work life balance score
        with col9:
            bar_wlb = px.bar(filtered["wlb"].value_counts().reset_index(name="count").rename(columns={"index":"wlb"}),
                                x="wlb", y="count", color="wlb",
                                title="Work Life Balance Distribution",
                                labels={"count":"Employees", "wlb":"WLB Score"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_wlb, use_container_width=True)

        # Stress
        with col10:
            bar_stress = px.bar(filtered["stress"].value_counts().reset_index(name="count").rename(columns={"index":"stress"}),
                                x="stress", y="count", color="stress",
                                title="Stress Distribution",
                                labels={"count":"Employees", "stress":"Stress Level"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_stress, use_container_width=True)

        col11, col12 = st.columns(2)
        # Sleep
        with col11:
            bar_sleep = px.bar(filtered["sleep_hours"].value_counts().reset_index(name="count").rename(columns={"index":"sleep_hours"}),
                                x="sleep_hours", y="count", color="sleep_hours",
                                title="Sleep Hours Distribution",
                                labels={"count":"Employees", "sleep_hours":"Sleep Hours"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_sleep, use_container_width=True)

        # Workload
        with col12:
            bar_workload = px.bar(filtered["workload"].value_counts().reset_index(name="count").rename(columns={"index":"workload"}),
                                x="workload", y="count", color="workload",
                                title="Workload Distribution",
                                labels={"count":"Employees", "workload":"Workload"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_workload, use_container_width=True)

        # Training & Development
        st.subheader("Training & Development")
        col13 = st.columns(1)[0]
        # Training hours
        with col13:
            bar_training = px.bar(filtered["training_hours_per_year"].value_counts().reset_index(name="count").rename(columns={"index":"training_hours_per_year"}),
                                x="training_hours_per_year", y="count", color="training_hours_per_year",
                                title="Training Hours Distribution",
                                labels={"count":"Employees", "training_hours_per_year":"Training Hours"},
                                color_discrete_sequence = palette)
            st.plotly_chart(bar_training, use_container_width=True)
