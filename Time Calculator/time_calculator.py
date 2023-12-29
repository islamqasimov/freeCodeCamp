def add_time(start, duration, start_day=''):
# Declaring variables for usage
    daysLeft = 0

    days =["Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    
    sTime = start.split(":")
    sHour = int(sTime[0])
    sMin = int(sTime[1][:2])
    sPer = sTime[1][3:]
    sDay = days.index(start_day.capitalize())+1 if start_day != '' else 0

    dTime = duration.split(":")
    dHour = int(dTime[0])
    dMin = int(dTime[1])

    eHour = 0
    eMin = ''
    ePer = sPer
    eDay = sDay
    end_day = ''

# Counting Minutes:
    eMin = sMin + dMin

    if eMin >= 60:
        eMin -= 60
        eHour += 1
    ###
        
# Counting Hours:
    eHour += sHour + dHour

    if eHour >= 24:
        while eHour >= 24:
            eHour -= 24
            daysLeft += 1
    if eHour > 12:
        eHour -= 12
        ePer = 'AM' if sPer == 'PM' else 'PM'
        daysLeft += 1 if ePer == 'AM' else 0
    elif eHour == 12:
        ePer = 'AM' if sPer == 'PM' else 'PM'
        daysLeft += 1 if ePer == 'AM' else 0

# Counting Days:
    if daysLeft == 1:
        eDay += 1
    elif daysLeft >= 7:
        eDay = (eDay+daysLeft)%7
    else:
        eDay += daysLeft
    
            
# Rendering
    eMin = '0'+str(eMin) if len(str(eMin)) == 1 else str(eMin)
    eHour = '00' if eHour == 0 else str(eHour)
    daysLeftRend = f"({daysLeft} days later)" if daysLeft != 1 else f"(next day)" if daysLeft != 0 else ''
    end_day = days[eDay-1] if start_day != '' else ''

    if start_day != '' and daysLeft != 0:
        return f"{eHour}:{eMin} {ePer}, {end_day} {daysLeftRend}"  
    elif start_day != '' and daysLeft == 0:
        return f"{eHour}:{eMin} {ePer}, {end_day}"
    elif start_day == '' and daysLeft != 0:
        return f"{eHour}:{eMin} {ePer} {daysLeftRend}"
    elif start_day == '' and daysLeft == 0:
        return f"{eHour}:{eMin} {ePer}"  
    
