#programme qui lit un fichier texte, 
#supprime les returns se trouvant entre deux guillemets
#dans un fichier de sortie que l'on nomeras du meme nom
#augmenté d'une extension .out
import re
import csv
with open("folderin.csv", mode ='r') as f_in, open("folderout.txt", mode='w', newline='') as f_out:
    f_reader = csv.reader(f_in, delimiter=',', dialect=csv.excel_tab)
    f_writer = csv.writer(f_out, dialect=csv.excel_tab)
    for line in f_reader:
                for col in line:
                    
                    if "\n" in col:
                        sup = re.sub('^\n', "", str(line))
                        f_writer.writerow(sup)

