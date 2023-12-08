import csv
from matplotlib import pyplot as plt
import numpy as np

communes=[]
with open('metadonnees_communes.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        communes.append(row)
        
communes=[[communes[i+118][2],communes[i+118][3]] for i in range(len(communes)-121)]


#Traitement de l'année 2008
communes_2008=[]
with open('donnees_2008.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        communes_2008.append(row)
communes_2008=[[communes_2008[i+1][2]+communes_2008[i+1][5],int(communes_2008[i+1][9])] for i in range(len(communes_2008)-1)]

#Traitement de l'année 2016
communes_2016=[]
with open('donnees_2016.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        communes_2016.append(row)
communes_2016=[[communes_2016[i+1][2]+communes_2016[i+1][5],int(communes_2016[i+1][9])] for i in range(len(communes_2016)-1)]

#Traitement de l'année 2021
communes_2021=[]
with open('donnees_2021.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        communes_2021.append(row)
communes_2021=[[communes_2021[i+1][2],int(communes_2021[i+1][5])] for i in range(len(communes_2021)-1)]
#print(communes_2021)

#Calcul de la population d'Auxerre pour 2008,2016 et 2021
A=0
for i in range(len(communes)):
	if communes[i][1]=='Auxerre':
		#print(communes[i][0],'Auxerre',i)
		A=communes[i][0]
   
population_auxerre={
    '2008': 0,
    '2016': 0,
    '2021': 0
}

for commune in communes_2008:
    if commune[0]==A:
        population_auxerre['2008']=commune[1]

for commune in communes_2016:
    if commune[0]==A:
        population_auxerre['2016']=commune[1]

for commune in communes_2021:
    if commune[0]==A:
        population_auxerre['2021']=commune[1]


#Affichage du graphique
dates=['2008', '2016', '2021']
population_auxerre=[population_auxerre['2008'], population_auxerre['2016'], population_auxerre['2021']]
plt.plot(dates, population_auxerre,color='b')
plt.scatter(dates,population_auxerre,color='b')
plt.title('Évolution de la population de Auxerre')
plt.xlabel('Années')
plt.ylabel('Population')
plt.show()

# ~ dates_new=[2008,2050]

# ~ #affiche les estimations d'evolution de la populations d'auxerre et de sens

# ~ plt.scatter(dates,population_auxerre,color='b')
# ~ plt.title("Population à Auxerre")
# ~ plt.ylabel('Population')
# ~ plt.xlabel('Années')
# ~ coefA=np.polyfit(dates,population_auxerre,1)
# ~ poly1d_fnA=np.poly1d(coefA)
# ~ plt.plot(dates_new, poly1d_fnA(dates_new),color='b',linestyle='dashed')
# ~ plt.show()

#On a essayé pour faire l'évolution d'Auxerre et de son agglomération immédiate mais on a pas eu le temps de finir
# ~ communes_agglomeration = ['Appoigny', 'Auxerre', 'Monéteau', 'Perrigny', 'Saint-Georges-sur-Baulche']
# ~ AI=0
# ~ for i in range(len(communes)):
	# ~ if communes[i][1]==communes_agglomeration:
		# ~ AI=communes[i][0]

# ~ population_auxerreI={
    # ~ '2008': 0,
    # ~ '2016': 0,
    # ~ '2021': 0
# ~ }

# ~ for commune in communes_2008:
    # ~ if commune[0]==AI:
        # ~ population_auxerreI['2008']=commune[1]

# ~ for commune in communes_2016:
    # ~ if commune[0]==AI:
        # ~ population_auxerreI['2016']=commune[1]

# ~ for commune in communes_2021:
    # ~ if commune[0]==AI:
        # ~ population_auxerreI['2021']=commune[1]   

# ~ #Affichage du graphique
# ~ dates2=['2008', '2016', '2021']
# ~ population_auxerreI=[population_auxerreI['2008'], population_auxerreI['2016'], population_auxerreI['2021']]
# ~ plt.plot(dates, population_auxerreI,color='b')
# ~ plt.scatter(dates,population_auxerreI,color='b')
# ~ plt.title('Évolution de la population de Auxerre et son agglomération immédiate')
# ~ plt.xlabel('Années')
# ~ plt.ylabel('Population')
# ~ plt.show()

