# 📊 People Analytics Dashboard — Employee Job Satisfaction EDA

Dashboard ini dibuat menggunakan **Streamlit** untuk melakukan *Exploratory Data Analysis (EDA)* terhadap data karyawan.  
Tujuannya adalah memahami **faktor-faktor yang memengaruhi tingkat kepuasan kerja (Job Satisfaction)** di perusahaan.

---

## 🎯 Tujuan Analisis
- Menganalisis faktor-faktor seperti stres, beban kerja, work-life balance, dan lingkungan kerja terhadap kepuasan kerja.  
- Mengetahui distribusi demografis karyawan berdasarkan usia, gender, dan jabatan.  
- Menyediakan visualisasi interaktif untuk membantu HR dalam pengambilan keputusan berbasis data.

---

## 🚀 Fitur Dashboard
- **Employee Overview:** Gambaran umum karyawan (usia, gender, pengalaman, dan departemen).  
- **Job Satisfaction Analysis:** Distribusi kepuasan kerja dan perbandingan antar kelompok.  
- **Workforce Structure:** Analisis struktur tenaga kerja berdasarkan level jabatan dan tim.
- **Employee Demographics:** Analisis demografi seperti umur, gender, dan education level.

---

## 🧱 Struktur Folder
📁 people-analytics-dashboard/
│
├── app.py # File utama Streamlit
├── requirements.txt # Daftar library Python
├── README.md # Dokumentasi proyek
│
├── 📂 data/
└── employee_data.csv # Dataset utama


---

## 📊 Deskripsi Dataset

Dataset berisi data karyawan yang digunakan untuk analisis kepuasan kerja.  
Berikut penjelasan setiap kolom:

| Kolom | Deskripsi |
|-------|------------|
| `emp_id` | Nomor unik setiap karyawan |
| `gender` | Jenis kelamin karyawan |
| `age` | Umur karyawan |
| `marital_status` | Status pernikahan (Menikah, Belum Menikah, Duda/Janda) |
| `job_level` | Tingkatan jabatan (misalnya: Junior, Senior, Manager) |
| `experience` | Jumlah tahun pengalaman kerja |
| `dept` | Departemen tempat karyawan bekerja |
| `emp_type` | Jenis status karyawan (Tetap, Kontrak, Paruh Waktu) |
| `wlb` | Skala Work-Life Balance (misalnya 1–5) |
| `work_env` | Tingkat kepuasan terhadap lingkungan kerja |
| `physical_activity_hours` | Rata-rata jam aktivitas fisik per periode tertentu |
| `workload` | Jumlah pekerjaan/tugas yang diselesaikan dalam periode tertentu |
| `stress` | Tingkat stres kerja (skala 1–5) |
| `sleep_hours` | Rata-rata jam tidur per hari |
| `commute_mode` | Moda transportasi ke kantor (misalnya mobil, motor, transportasi umum) |
| `commute_distance` | Jarak perjalanan ke kantor (dalam kilometer) |
| `num_companies` | Jumlah perusahaan sebelumnya tempat karyawan pernah bekerja |
| `team_size` | Jumlah anggota tim tempat karyawan bekerja |
| `num_reports` | Jumlah bawahan langsung (direct reports) |
| `edu_level` | Tingkat pendidikan terakhir |
| `have_ot` | Apakah karyawan sering lembur (`True` / `False`) |
| `training_hours_per_year` | Rata-rata jam pelatihan per tahun |
| `job_satisfaction` | Skor tingkat kepuasan kerja (variabel utama) |

---

👩‍💻 Author
Afifah Fitri Ritonga
📧 [afifahfitriritonga@gmail.com]
