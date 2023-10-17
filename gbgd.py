from datetime import datetime, timedelta
data = datetime.now()
data2 = new_final_time = data + timedelta(days=2, seconds=0, microseconds=0, milliseconds=0, minutes=20, hours=4, weeks=5)
def tempo(tpost):
    data = datetime.now()
    diferenca = data - tpost
    t = f"Há {diferenca.seconds}s"
    #if diferenca.

'''days
seconds
'''
diferenca = data2 - data
print(diferenca.seconds)

data_formatada = data.strftime("%d/%m/%Y, %H:%M") # ("%m/%d/%Y, %H:%M:%S")