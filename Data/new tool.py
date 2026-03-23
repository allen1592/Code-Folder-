import pandas as pd

# 🔹 Bước 1: Đọc file CSV
file_path = r"/Code/data/hannel_oct.csv"
df = pd.read_csv(file_path)

# 🔹 Bước 2: Tách ngày (phần đầu trong "Date Time")
df['Date'] = df['Date Time'].str.extract(r'(\d+/\d+/\d+)')

# 🔹 Bước 3: Chuyển 'Date' sang kiểu datetime để sắp xếp chính xác
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce')

# 🔹 Bước 4: Làm sạch dữ liệu 'Traffic Total (speed)'
df['Traffic Total (speed)'] = (
    df['Traffic Total (speed)']
    .astype(str)
    .str.replace(' Mbit/s', '', regex=False)
    .str.replace(',', '', regex=False)
)
df['Traffic Total (speed)'] = pd.to_numeric(df['Traffic Total (speed)'], errors='coerce')
# 🔹 Bước 5: Tính TỔNG traffic mỗi ngày (đơn vị Mbit/s)
daily_total = (
    df.groupby('Date', as_index=False)['Traffic Total (speed)'].sum()
    .rename(columns={'Traffic Total (speed)': 'Total Traffic (Mbit/s)'})
)

# 🔹 Bước 6: Đổi sang Gbps
daily_total['Total Traffic (Gbps)'] = daily_total['Total Traffic (Mbit/s)'] / 1000

# 🔹 Bước 7: Sắp xếp theo thứ tự thời gian
daily_total = daily_total.sort_values('Date')

# 🔹 Bước 8: Xuất ra file Excel
output_path = r"/Code/Data/Daily_Avg_Traffic_Sorted.xlsx"
daily_total.to_excel(output_path, index=False)

print("✅ File Excel đã được tạo thành công:", output_path)
