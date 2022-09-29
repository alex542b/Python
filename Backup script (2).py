# De forskellige biblioteker som der bliver brugt
import shutil
import os

# Scriptet bliver ved med at prompte brugeren indtil de siger at det skal afslutte
while True:
    # Spørger brugeren om de vil lave full backup eller se en smiley eller afslutte
    backup = int(input('Vil du lave full backup (1) eller se en meget flot smiley (2) eller afslutte (3)'))

# Full backup metode som der sker hvis brugeren trykker 1
    def full_backup():
        # Stierne på source og destination som ligger lokalt på computeren
        source = 'C:\\Users\\Alexander\\Desktop\\Python file transfer'
        destination = 'C:\\Users\\Alexander\\Desktop\\Receiver folder'
# For hver fil i source kopiere den over i destination
        for file in os.listdir(source):
            shutil.copy(source + '/' + file, destination)
        print('der er blevet taget backup af alle filer!')

# Smiley metode. Printer en smiley hvis brugeren trykker 2.
    def Smiley():

        print('\U0001F606')

# Tager brugerens input i en if else og laver nedenstående ud fra hvilket input brugeren valgte
    if backup == 1:
        full_backup()
    elif backup == 2:
        Smiley()
    elif backup == 3:
        print('Du afsluttede programmet')
        break
    else:
        print('Du skal vælge 1 eller 2 eller 3 prøv igen')
