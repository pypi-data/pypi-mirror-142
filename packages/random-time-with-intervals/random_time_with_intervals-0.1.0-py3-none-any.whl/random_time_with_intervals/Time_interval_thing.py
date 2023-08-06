import random as rand
import xlsxwriter
import time

def time_gen_hour(hour,minute,second):
# Hours    
    if minute== 59 and second==59:
        hour = hour + 1
        minute = 0
        second = 0

    hour = f'{hour:02}'
# Minutes
    if minute == 0:
        minute = 0
    else:
       minute = minute + rand.randint(0,20)

    minute = f'{minute:02}'
# Seconds
    if second==0:
        second = 0
    else:
        second = rand.randint(1,59)
        if second == 59:
            second = 0
            minute = minute + 1
    second = f'{second:02}'
# Print function
    print(hour + ':' + minute + ':' + second)
    
book = xlsxwriter.Workbook('Timesheet.xlsx')
worksheet = book.add_worksheet()
row = 0
col = 0


def time_between(x, y ,between):
#    x = int(input("Starting hour? (Example: '12')"))
#    y = int(input("Finishing hour? (Example: '13')"))
#    between = int(input("How many random times do you want?"))
    
    start = time.time()
    row = 0
    # Turning into seconds    
    x = x * 60 * 60 
    y = y * 60 * 60
    z = y - x
    # Difference
    d = z/between
    d = int(d)
    # For loop
    times = []
    for i in range(between):
        x2 = x + d
        i = rand.randint(x,x2)
        x = x2
        times.append(i)
    # Turning back into HH:MM:SS
    times_decimals= []
    for t in times:
        t = t/60
        t = t/60
        times_decimals.append(t)
    for t in times_decimals:
        hours = int(t)
        minutes = (t*60) % 60
        seconds = (t*3600) % 60
        x = "%d:%02d:%02d" % (hours, minutes, seconds)
    # Returning into an excel spreadsheet
        worksheet.write(row, col, x)
        row += 1
    end = time.time()
    thingy = end - start
    return f"Done in {thingy:.2f} seconds"

for i in range(40):
    some_number = rand.randint(30,45)
    time_between(5,6,some_number)
    col += 1

book.close()

