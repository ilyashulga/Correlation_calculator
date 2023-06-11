import pandas as pd
import plotly.graph_objs as go

# Read the structured data from Excel (xlsx) file, skipping 4 rows
df = pd.read_excel('1.xlsx', skiprows=4, engine='openpyxl')

# Assuming 'measurement1' and 'measurement2' are the column names for the two measurements
measurement1 = df['Safety voltage']
measurement2 = df['ABS (Delta CTMIn - CTMOut)']
measurement3 = df['OPT temperature']
measurement4 = df['ABS (Delta PT- CTMIn)']
measurement5 = df['ABS (Delta PT- CTMOut)']
measurement6 = df['OPT CTMIn']

# Calculate the correlation coefficient (Pearson correlation)
correlation_coefficient_1 = measurement1.corr(measurement2)
correlation_coefficient_2 = measurement3.corr(measurement2)
correlation_coefficient_3 = measurement3.corr(measurement4)
correlation_coefficient_4 = measurement3.corr(measurement5)
correlation_coefficient_5 = measurement2.corr(measurement6)

print(df.head())

# Print the correlation coefficient
print("Safety Voltage vs ABS (Delta CTMIn - CTMOut) Correlation Coefficient:", correlation_coefficient_1)
print("OPT Temperature vs ABS (Delta CTMIn - CTMOut) Correlation Coefficient:", correlation_coefficient_2)
print("OPT Temperature vs ABS (Delta PT- CTMIn) Correlation Coefficient:", correlation_coefficient_3)
print("OPT CTMIn vs ABS (Delta CTMIn - CTMOut) Correlation Coefficient:", correlation_coefficient_4)


# ------------------------------- Histogram Plotting ------------------------------

# Create a histogram trace for each set of data
trace1 = go.Histogram(x=measurement1, name='Safety voltage', autobinx=True, opacity=0.7)


# Create a layout for the plot
layout = go.Layout(barmode='overlay', xaxis=dict(tickmode = 'linear',
        #tick0 = 10,
        #dtick = 1,
        #tickformat="%b\n%Y",
        ticklabelmode="period",
        dtick="s1",
        title='Safety Voltage'),
        yaxis=dict(title='Count'))

# Create a figure containing the histogram traces
fig = go.Figure(data=[trace1], layout=layout)

# Show the plot
fig.show()