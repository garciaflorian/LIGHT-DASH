import re

def linkyparsing(string):
    
    #Regex for parsing the serial port data
    regex = re.compile('([A-Za-z0-9]+)\s([A-Za-z0-9.]+)')

    # prepairing everything for line insertion into database
    line = {} #dictionnary because django dislikes normal SQL queries

    #for safety purposes
    line["state"] = 'N.A.'
    line["ID"] = 'N.A.'
    line["subsc"] = 'N.A.'
    line["iSubsc"] = 'N.A.'
    line["cons"] = 'N.A.'
    line["curRate"] = 'N.A.'
    line["instInt"] = 'N.A.'
    line["maxInt"] = 'N.A.'
    line["appPow"] = 'N.A.'
    line["tGroup"] = 'N.A.'
    line["addData"] = False # additionnal info from the linky
    iterresult=iter(regex.findall(stringtest))

    for item in (iterresult):
        treatment = item
        # distributing data
        if treatment[0] == 'MOTDETAT':
            line["state"]=treatment[1]
        elif treatment[0] == 'ADCO':
            line["ID"]=treatment[1]
        elif treatment[0] == 'OPTARIF':
            line["subsc"]=treatment[1]
        elif treatment[0] == 'ISOUSC':
            line["iSubsc"]=treatment[1]
        elif treatment[0] == 'BASE':
            line["cons"]=treatment[1]
        elif treatment[0] == 'PTEC':
            line["curRate"]=treatment[1]         
        elif treatment[0] == 'IINST':
            line["instInt"]=treatment[1]
        elif treatment[0] == 'IMAX':
            line["maxInt"]=treatment[1]
        elif treatment[0] == 'PAPP':
            line["appPow"]=treatment[1]
        elif treatment[O] == 'HHPHC':
            line["tGroup"]=treatment[1]
        else:
            line["addData"]= True  
    return line         

