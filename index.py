python
import pandas as pd

# Load datasets
transport_data = pd.read_csv('Abu_Dhabi_Public_Transport_Usage_2018_2024.csv')
hotel_data = pd.read_excel('Abu_Dhabi_Hotels_Open_Datasets1_0.xlsx')

# Example integration: Identify peak hotel occupancy seasons and correlate with transport usage
hotel_data['OccupancyDate'] = pd.to_datetime(hotel_data['Date'])
transport_data['TransportDate'] = pd.to_datetime(transport_data['Date'])

# Group by date to find peak seasons
hotel_peak_seasons = hotel_data.groupby(hotel_data['OccupancyDate'].dt.quarter)['OccupancyRate'].mean()
transport_peak_usage = transport_data.groupby(transport_data['TransportDate'].dt.quarter)['PassengerCount'].mean()

# Merge datasets on quarters
combined_data = pd.merge(hotel_peak_seasons, transport_peak_usage, left_index=True, right_index=True)

print("Combined Data Insights")
print(combined_data)
