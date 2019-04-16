import re

def linkyparsing(string):
    
    #Regex for parsing the serial port data
    regex = re.compile('([A-Za-z0-9]+)\s([A-Za-z0-9.]+)')
    #for safety purposes
    state = 'N.A.'
    ID = 'N.A.'
    subsc = 'N.A.'
    iSubsc = 'N.A.'
    cons  = 'N.A.'
    curRate = 'N.A.'
    instInt = 'N.A.'
    maxInt = 'N.A.'
    appPow = 'N.A.'
    tGroup = 'N.A.'
    addData = False # additionnal info from the linky
    iterresult=iter(regex.findall(stringtest))
    for item in (iterresult):
        treatment = item
        # distributing data
        if treatment[0] == 'MOTDETAT':
            state=treatment[1]
        elif treatment[0] == 'ADCO':
            ID=treatment[1]
        elif treatment[0] == 'OPTARIF':
            subsc=treatment[1]
        elif treatment[0] == 'ISOUSC':
            iSubsc=treatment[1]
        elif treatment[0] == 'BASE':
            cons=treatment[1]
        elif treatment[0] == 'PTEC':
            curRate=treatment[1]        
        elif treatment[0] == 'IINST':
            instInt=treatment[1]
        elif treatment[0] == 'IMAX':
            maxInt=treatment[1]
        elif treatment[0] == 'PAPP':
            appPow=treatment[1]
        elif treatment[O] == 'HHPHC':
            tGroup=treatment[1]
        else:
            addData= True 
        # prepairing everything for line insertion into database
    return [state,ID,subsc,iSubsc,cons,curRate,instInt,maxInt,appPow,tGroup,addData]
                    

