from datetime import datetime

def convert_time(time_arg):
    # parse time string into datetime object
    t =  datetime.strptime(time_arg,"%I:%M:%S%p")
    print("Time : " ,t)

    # format datetime into 24 hrs 
    return datetime.strftime(t,"%H:%M:%S")
    
my_time = '07:05:45PM'
result = convert_time(my_time)
print(result)
