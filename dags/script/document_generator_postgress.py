def script():
    import pandas as pd
    import psycopg2 as ps
    import sys, subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'docxtpl'])
    from docxtpl import DocxTemplate
    from pathlib import Path

# Konfigurasi koneksi ke database
    conn = ps.connect(
            host= "host.docker.internal",
            port= '5432',
            database= 'postgres',
            user= 'airflow',
            password= 'airflow'
        )
    base_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    output_dir = base_dir / "/usr/local/airflow/include/OUTPUT_POSTGRES"

    # Create output folder for the word documents
    output_dir.mkdir(exist_ok=True)

    # Membuat objek kursor
    cur = conn.cursor()

# Mengambil data dari tabel di database
    sql = '''SELECT * FROM "user" where id in (4,7)'''
   
    
# Membuat deklarasi data untuk t

    df = pd.read_sql(sql,conn)
# Membuka template dokumen Word
    for record in df.to_dict(orient='records'):
        file_path = '/usr/local/airflow/include/my_wd.docx'
        template = DocxTemplate(file_path)
    
# Menggabungkan konteks data dengan template
        template.render(record)
        
# Menentukan Tempat Penyimpanan
        output_path = output_dir / f"{record['nama']}-{record['kelas']}-generated_doc.docx"
# Menyimpan dokumen Word yang dihasilkan
        template.save(output_path)

# Menutup koneksi ke database
        cur.close()
        conn.close()


