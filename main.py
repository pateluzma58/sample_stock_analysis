
"""
Synthetic stock data used in this assignment
Day   Open   Close
1     100    98
2     98  98
3     98  101
4     101 101
5     101 102
6     102 105
...
20    107 106
"""

import csv

data = [
    {"Day": 1, "Open": 100, "Close": 98},
    {"Day": 2, "Open": 98, "Close": 98},
    {"Day": 3, "Open": 98, "Close": 101},
    {"Day": 4, "Open": 101, "Close": 101},
    {"Day": 5, "Open": 101, "Close": 102},
    {"Day": 6, "Open": 102, "Close": 105},
    {"Day": 7, "Open": 105, "Close": 106},
    {"Day": 8, "Open": 106, "Close": 104},
    {"Day": 9, "Open": 104, "Close": 102},
    {"Day": 10, "Open": 102, "Close": 101},
    {"Day": 11, "Open": 101, "Close": 104},
    {"Day": 12, "Open": 104, "Close": 105},
    {"Day": 13, "Open": 105, "Close": 106},
    {"Day": 14, "Open": 106, "Close": 106},
    {"Day": 15, "Open": 106, "Close": 105},
    {"Day": 16, "Open": 105, "Close": 109},
    {"Day": 17, "Open": 109, "Close": 110},
    {"Day": 18, "Open": 110, "Close": 105},
    {"Day": 19, "Open": 105, "Close": 107},
    {"Day": 20, "Open": 107, "Close": 106}
]

for i, row in enumerate(data):
    open_price = row["Open"]
    close_price = row["Close"]
    pct_change = (close_price - open_price) / open_price * 100
    row["PctChange"] = pct_change

    yesterday = data[i - 1]["PctChange"] if i > 0 else None

    positive_today = pct_change > 0
    positive_yesterday = (yesterday is not None) and (yesterday > 0)
    negative_today = pct_change < 0
    negative_yesterday = (yesterday is not None) and (yesterday < 0)

    signal = "HOLD"

    if (yesterday is not None) and pct_change > 2 and positive_today and positive_yesterday:
        signal = "BUY"
    elif pct_change < -2 or (negative_today and negative_yesterday):
        signal = "SELL"
    else:
        signal = "HOLD"

    row["Signal"] = signal

print("Day  Open   Close  PctChange   Signal")
for row in data:
    print(
        f"{row['Day']:2d}  {row['Open']:6.2f}  {row['Close']:6.2f}  "
        f"{row['PctChange']:8.3f}   {row['Signal']}"
    )

with open("stock_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Day", "Open", "Close", "PctChange", "Signal"])
    writer.writeheader()
    writer.writerows(data)

