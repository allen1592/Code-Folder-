import pandas as pd

# 🔹 Bước 1: Đọc file CSV
file_path = r"/Code/data/historicdata (1).csv"
df = pd.read_csv(file_path)

# 🔹 Bước 2: Tách phần ngày (loại bỏ giờ)
df['Date'] = df['Date Time'].str.extract(r'(\d+/\d+/\d+)')

# 🔹 Bước 3: Làm sạch dữ liệu 'Traffic Total (speed)' (bỏ " Mbit/s")
df['Traffic Total (speed)'] = (
    df['Traffic Total (speed)']
    .astype(str)
    .str.replace(' Mbit/s', '', regex=False)
    .str.replace(',', '', regex=False)
)
df['Traffic Total (speed)'] = pd.to_numeric(df['Traffic Total (speed)'], errors='coerce')

# 🔹 Bước 4: Tính **trung bình** traffic (Mbit/s) theo ngày
daily_avg_traffic = df.groupby('Date', as_index=False)['Traffic Total (speed)'].mean()

# 🔹 Bước 5: Xuất ra file Excel
output_path = "Daily_Avg_Traffic_Mbit.xlsx"
daily_avg_traffic.to_excel(output_path, index=False)

print("✅ File Excel đã được tạo thành công:", output_path)
