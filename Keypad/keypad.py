from machine import Pin

# Define the rows and columns of the keypad
rows = [Pin(15), Pin(14), Pin(13), Pin(12)]
columns = [Pin(11), Pin(10), Pin(9)]
message = 'You pressed'
# Define the keys on the keypad
keys = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']]

# Initialize the rows as inputs
for row in rows:
    row.init(Pin.IN, Pin.PULL_UP)

# Initialize the columns as outputs
for column in columns:
    column.init(Pin.OUT)

# Continuously read keypad input
while True:
    for j in range(len(columns)):
        # Set the current column as low
        columns[j].low()
        for i in range(len(rows)):
            if rows[i].value() == 0:
                print(message,keys[i][j])
        # Set the current column as high
        columns[j].high()
    
