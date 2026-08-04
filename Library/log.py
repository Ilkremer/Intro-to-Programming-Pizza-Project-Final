from datetime import datetime

def writetoerrorlog(page, inst):
    with open("ErrorLog.txt", 'a', encoding='utf-8') as file:
        line_to_write = f"From {page} Unexpected {inst=},\n {type(inst)=} on {datetime.now()}\n"
        file.write(line_to_write + '\n')
