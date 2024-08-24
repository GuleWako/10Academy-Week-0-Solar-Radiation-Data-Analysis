def readData(data):
    if data=='Benin':
        return '../data/benin-malanville.csv'
    elif data=='Sierra Leone':
        return '../data/sierraleone-bumbuna.csv'
    elif data =='Togo':
        return '../data/togo-dapaong_qc.csv'
    else:
        print("No data with this name")

def CheckOutLiers(data, column_name):
    q1 = data[column_name].quantile(0.25)
    q3 = data[column_name].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data[column_name] < lower_bound) | (data[column_name] > upper_bound)]
    print(f"Potential outliers in {column_name}: {outliers.shape[0]}")
