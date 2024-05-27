import pandas as pd


def filling_missing_data(df):
    df.fillna(
        {
        "Adults (ages 15+) and children (ages 0-14) newly infected with HIV":df['Adults (ages 15+) and children (ages 0-14) newly infected with HIV'].median(),
        "Adults (ages 15-49) newly infected with HIV":df['Adults (ages 15-49) newly infected with HIV'].median(),
        "Arms exports (SIPRI trend indicator values)":df['Arms exports (SIPRI trend indicator values)'].median(),
        "Automated teller machines (ATMs) (per 100,000 adults)":df['Automated teller machines (ATMs) (per 100,000 adults)'].mean(),
        "Arms imports (SIPRI trend indicator values)":df['Arms imports (SIPRI trend indicator values)'].median(),
        "Average transaction cost of sending remittances from a specific country (%)":df['Average transaction cost of sending remittances from a specific country (%)'].mean(),
        "Average transaction cost of sending remittances to a specific country (%)":df['Average transaction cost of sending remittances to a specific country (%)'].median(),
        "Bank capital to assets ratio (%)":df['Bank capital to assets ratio (%)'].median(),
        "Bank liquid reserves to bank assets ratio (%)":df['Bank liquid reserves to bank assets ratio (%)'].median(),
        "Bank nonperforming loans to total gross loans (%)":df['Bank nonperforming loans to total gross loans (%)'].median(),
        "Charges for the use of intellectual property, payments (BoP, current US$)":df['Charges for the use of intellectual property, payments (BoP, current US$)'].median(),
        "Charges for the use of intellectual property, receipts (BoP, current US$)":df['Charges for the use of intellectual property, receipts (BoP, current US$)'].median(), 
        "Commercial bank branches (per 100,000 adults)":df["Commercial bank branches (per 100,000 adults)"].median(),
        "Computer, communications and other services (% of commercial service exports)":df["Computer, communications and other services (% of commercial service exports)"].mean(),
        "Computer, communications and other services (% of commercial service imports)":df["Computer, communications and other services (% of commercial service imports)"].mean(),
        "Consumer price index (2010 = 100)":df['Consumer price index (2010 = 100)'].median(),
        "Domestic credit provided by financial sector (% of GDP)":df['Domestic credit provided by financial sector (% of GDP)'].median(),
        "Domestic credit to private sector (% of GDP)":df['Domestic credit to private sector (% of GDP)'].median(),
        "Domestic credit to private sector by banks (% of GDP)":df['Domestic credit to private sector by banks (% of GDP)'].median(),
        "Employment to population ratio, 15+, female (%) (national estimate)":df['Employment to population ratio, 15+, female (%) (national estimate)'].mean(),
        "Employment to population ratio, 15+, male (%) (national estimate)":df["Employment to population ratio, 15+, male (%) (national estimate)"].median(),
        "Employment to population ratio, 15+, total (%) (national estimate)":df["Employment to population ratio, 15+, total (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, female (%) (national estimate)":df["Employment to population ratio, ages 15-24, female (%) (national estimate)"].median(),
        "Employment to population ratio, ages 15-24, male (%) (national estimate)":df["Employment to population ratio, ages 15-24, male (%) (national estimate)"].mean(),
        "Employment to population ratio, ages 15-24, total (%) (national estimate)":df["Employment to population ratio, ages 15-24, total (%) (national estimate)"].mean(),
         "Final consumption expenditure (% of GDP)":df['Final consumption expenditure (% of GDP)'].median(),
        "Final consumption expenditure (annual % growth)":df['Final consumption expenditure (annual % growth)'].median(),
        "Final consumption expenditure (constant 2010 US$)":df['Final consumption expenditure (constant 2010 US$)'].median(),
        'Final consumption expenditure (constant LCU)':df['Final consumption expenditure (constant LCU)'].median(),
        'Final consumption expenditure (current LCU)':df['Final consumption expenditure (current LCU)'].mean(),
        'Final consumption expenditure (current US$)':df['Final consumption expenditure (current US$)'].median(),
        'Fixed broadband subscriptions':df['Fixed broadband subscriptions'].median(),
        'Fixed broadband subscriptions (per 100 people)':df['Fixed broadband subscriptions (per 100 people)'].median(),
        'Fixed telephone subscriptions':df['Fixed telephone subscriptions'].median(),
        'Fixed telephone subscriptions (per 100 people)':df['Fixed telephone subscriptions (per 100 people)'].median(),
        "GDP (constant 2010 US$)":df['GDP (constant 2010 US$)'].median(),
        "GDP growth (annual %)":df['GDP growth (annual %)'].median(),
        "GDP per capita (constant 2010 US$)":df['GDP per capita (constant 2010 US$)'].median(),
        "GNI (constant 2010 US$)":df['GNI (constant 2010 US$)'].median(),
        'GNI growth (annual %)':df['GNI growth (annual %)'].mean(),
        "GNI per capita (constant 2010 US$)":df['GNI per capita (constant 2010 US$)'].median(),
        "High-technology exports (current US$)":df['High-technology exports (current US$)'].median(),
         "Individuals using the Internet (% of population)":df['Individuals using the Internet (% of population)'].mean(),
          "Military expenditure (% of GDP)":df['Military expenditure (% of GDP)'].median(),
        "Ratio of female to male labor force participation rate (%) (national estimate)":df["Ratio of female to male labor force participation rate (%) (national estimate)"].mean(),
        "Total reserves (includes gold, current US$)":df["Total reserves (includes gold, current US$)"].median()
        },inplace=True
    )
    return df
 
def main():
    df=pd.read_csv("final_demographics_data.csv")
    
    return filling_missing_data(df)
    
processed_df = main()

# ----------------------------------------------------------
# Latitude and Longitude of the countries
latitudes = [36.7372, -34.6037, -35.2809, 48.2082, 23.8103,
    53.9045, 50.8503, -15.7942, 45.4215, -33.4489,
    39.9042, 4.7109, 55.6761, 0.1807, 30.0444,
    9.0208, 48.8566, 52.5200, 5.6037, 37.9838,
    28.6139, -6.2088, 33.3152, 53.3498, 31.7683,
    41.9028, 35.6895, 51.1694, 1.2921, 3.1390,
    19.4326, 34.0209, 27.7172, 52.3676, 9.0765,
    59.9139, 33.6844, -12.0464, 14.5995, 52.2297,
    38.7223, 44.4268, 24.7136, 1.3521, -25.7469,
    40.4168, 6.9271, 59.3293, 46.8182, 13.7563,
    36.8065, 39.9334, 0.3476, 50.4501, 24.4539,
    38.9072, 21.0278]

longitudes = [3.0863, -58.3816, 149.1300, 16.3738, 90.4125,
    27.5615, 4.3517, -47.8825, -75.6910, -70.6693,
    116.4074, -74.0721, 12.5683, -78.4678, 31.2357,
    38.7469, 2.3522, 13.4050, -0.1870, 23.7275,
    77.2090, 106.8456, 44.3661, -6.2603, 35.2137,
    12.4964, 139.6917, 71.4491, 36.8219, 101.6869,
    -99.1332, -6.8416, 85.3240, 4.9041, 7.3986,
    10.7522, 73.0479, -77.0428, 120.9842, 21.0122,
    -9.1393, 26.1025, 46.6753, 103.8198, 28.1879,
    -3.7038, 79.8612, 18.0686, 8.2275, 100.5018,
    10.1815, 32.8597, 32.5825, 30.5234, 54.3773,
    -77.0369, 105.8342]