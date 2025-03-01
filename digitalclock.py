f=open('digitalclockinput1.txt','r')
w=f.readline()
def create_time(time):
    global Time
    if len(time)==6:
        time='0'+time
    PM_or_AM=time[-2]
    hour=int(time[:2])
    time_list=['1','2','3','4','5','6','7','8','9','10','11']
    if str(hour) in time_list and PM_or_AM=='p':
        s_hour=str(int(time[:2])+12)
        Time=s_hour+time[2:5]
        return Time
    elif hour==12 and PM_or_AM=='a':
        s_hour='01'
        Time=s_hour+time[2:5]
        return Time
    else:
        Time=time[:5]
        return Time
    return Time
create_time(w)
d=list(Time)

five=[' _ ','|_ ',' _|']
zero=[' _ ','| |','|_|']
four=['   ','|_|','  |']
dots=[' ','.','.']
two=[' _ ',' _|','|_ ']
seven=[' _ ','  |','  |']
one=['   ','  |','  |']
three=[' _ ',' _|',' _|']
nine=[' _ ','|_|',' _|']
eight=[' _ ','|_|','|_|']
six=[' _','|_ ','|_|']
number_list=[zero,one,two,three,four,five,six,seven,eight,nine,dots]
list_coo=[]
for item in d:
    if item=='.':
        list_coo.append(number_list[-1])
    else:
        for t in range(10):
            if int(item)==t:
                list_coo.append(number_list[t])
for r in range(3):
    w=list_coo[0][r]+list_coo[1][r]+list_coo[2][r]+list_coo[3][r]+list_coo[4][r]
    print(w)
    
