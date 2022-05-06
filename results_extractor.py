import re, csv

num_folds = 5
fields = ["Training Data %", "Epochs", "Pseudo-Thresh", "Y-Thresh", "Average", "STD"]
data = []

with open('allout.txt', 'r') as f:
    contents = f.read()
    
    indices_object = re.finditer(pattern='-fold cross validation', string=contents)
    indices = [index.start() for index in indices_object]
    
    for ind in indices:
        results = contents[ind-1:24+(5*31)+122+ind]
        lines = results.split("\n")
        if lines[-1] == "":
            lines = lines[:-1]
        hps = lines[-2].split(": ")[-1].split(" ")
        if len(hps) != 4:
            hps = lines[-3].split(": ")[-1].split(" ")
        tp, ep, pt, yt = hps
        if tp == "0.1":
            print(lines[-6:])
        avg = lines[-5].split("=")[-1]
        std = lines[-4].split("=")[-1]
        data += [[tp, ep, pt, yt, avg, std]]
        
       
    f.close()
    with open("results.csv", 'w') as out_file:
        csvwriter = csv.writer(out_file) 
        csvwriter.writerow(fields)
        csvwriter.writerows(data)
        out_file.close()
