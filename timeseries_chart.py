import pandas as pd
import panel as pn
import hvplot.pandas

# Ekstensi Panel (misalnya, untuk widget tabel interaktif)
pn.extension('tabulator')

# Baca file CSV
file_path = "D:\\datacuaca.csv"
df = pd.read_csv(file_path)

# Pastikan kolom 'timestamp' berupa datetime, jika belum
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Jika diperlukan, pastikan kolom tanggal terpisah sudah bertipe data yang sesuai
# (misalnya, 'year', 'month', 'day' sebagai angka)
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['month'] = pd.to_numeric(df['month'], errors='coerce')
df['day'] = pd.to_numeric(df['day'], errors='coerce')

# Widget untuk filter berdasarkan tahun dan bulan
year_widget = pn.widgets.IntSlider(
    name="Year", 
    start=int(df['year'].min()), 
    end=int(df['year'].max()), 
    value=int(df['year'].min())
)

month_widget = pn.widgets.IntSlider(
    name="Month", 
    start=1, 
    end=12, 
    value=1
)

# Fungsi untuk menampilkan tabel data yang terfilter
@pn.depends(year=year_widget, month=month_widget)
def filtered_table(year, month):
    filtered = df[(df['year'] == year) & (df['month'] == month)]
    return pn.widgets.DataFrame(filtered, width=800, height=400)

# Fungsi untuk menampilkan grafik temperature terhadap waktu
@pn.depends(year=year_widget, month=month_widget)
def temperature_chart(year, month):
    filtered = df[(df['year'] == year) & (df['month'] == month)]
    if filtered.empty:
        return "No data for selected year and month."
    return filtered.hvplot.line(x='timestamp', y='temperature', title="Temperature over Time", width=1400, height=600)

# Fungsi untuk menampilkan grafik humidity terhadap waktu
@pn.depends(year=year_widget, month=month_widget)
def humidity_chart(year, month):
    filtered = df[(df['year'] == year) & (df['month'] == month)]
    if filtered.empty:
        return "No data for selected year and month."
    return filtered.hvplot.line(x='timestamp', y='humidity', title="Humidity over Time", width=1400, height=600)

# Fungsi untuk menampilkan grafik pressure terhadap waktu
@pn.depends(year=year_widget, month=month_widget)
def pressure_chart(year, month):
        filtered = df[(df['year'] == year) & (df['month'] == month)]
        if filtered.empty:
            return "No data for selected year and month."
        return filtered.hvplot.line(x='timestamp', y='pressure', title="Pressure over Time", width=1400, height=600)

# Layout dashboard menggunakan Panel dengan beberapa tab
dashboard = pn.Column(
    "# Time Series Dashboard",
    pn.Row(year_widget, month_widget),
    pn.Tabs(
        ("Data Table", filtered_table),
        ("Temperature Chart", temperature_chart),
        ("Humidity Chart", humidity_chart),
        ("Pressure Chart", pressure_chart)
    )
)

# Menjadikan dashboard dapat diakses dengan Panel Serve
dashboard.servable()
