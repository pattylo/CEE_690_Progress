# Visualize data in table format (Excel-like) - selected columns only
import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))
ax.axis('tight')
ax.axis('off')

# Select specific columns to display
selected_cols = ['Date', 'Natural_Gas', 'Crude_oil', 'Copper', '...', 'S&P_500', 'Apple', '...']

# Get data for selected columns (skip '...' placeholders)
table_data = [selected_cols]  # Header row

# Get first 5 data rows
for idx in range(5):
    row = []
    row.append(all_data.iloc[idx]['Date'])
    row.append(all_data.iloc[idx]['Natural_Gas'])
    row.append(all_data.iloc[idx]['Crude_oil'])
    row.append(all_data.iloc[idx]['Copper'])
    row.append('...')
    row.append(all_data.iloc[idx]['S&P_500'])
    row.append(all_data.iloc[idx]['Apple'])
    row.append('...')
    table_data.append(row)

# Add final row with dots
table_data.append(['...'] * len(selected_cols))

# Create table
table = ax.table(cellText=table_data, 
                 cellLoc='center',
                 loc='center',
                 bbox=[0, 0, 1, 1])

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.5)

# Make header row bold and with different color
for i in range(len(selected_cols)):
    cell = table[(0, i)]
    cell.set_facecolor('#4472C4')
    cell.set_text_props(weight='bold', color='white')

# Alternate row colors for data rows
for i in range(1, len(table_data)):
    for j in range(len(selected_cols)):
        cell = table[(i, j)]
        if i % 2 == 0:
            cell.set_facecolor('#E7E6E6')
        else:
            cell.set_facecolor('#FFFFFF')

plt.title(f'Data Preview - Total {len(all_data)} rows', 
          fontsize=14, fontweight='bold', pad=20)
plt.show()