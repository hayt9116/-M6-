import random

options1 = {"r":"Välj en maträtt slumpmässigt", "q": "Avsluta"}
def menu(title, prompt, options):
    print(title)
    print()
    for option in options:
        print(f"{option}) {options[option]}")
        
    print()
    inpt = input(prompt)
    
    while inpt not in options:
        inpt = input(prompt)
    
    print(f"Du valde alternativ {inpt}")
        
    return inpt

mat_dict = {
    "Pasta": ["Köttfärssås och spaghetti", "Pasta carbonara", "Köttbullar och makaroner", "Korv och makaroner"],
    "Vegetariskt": ["Falafel", "Ostpaj", "Bönbiffar med ris"],
    "Kött": ["Köttfärssås och spaghetti", "Pasta carbonara", "Köttbullar och makaroner", "Korv och makaroner"]}


print("Alternativ: Pasta, Kött eller Vegetariskt")

mat = input("Vad är du sugen på?: ")

while True:

    if mat in mat_dict:
        print(f"Maträtter som innehåller {mat}: ")
        print(mat_dict[mat])
        
        meny = menu("Välj ett alternativ", "Alternativ: ", options1)
        
        if meny == "r":
            mat1 = random.choice(mat_dict[mat])
            if mat1 in mat_dict[mat]:
                print("Din maträtt är:", mat1)
                if mat1 == "Köttfärssås och spaghetti":
                    print()
                    print(f"Recept för {mat1}")
                    print()
                    print('''500 g blandfärs
1 msk smör
1 st lök
1 st Morot
2 dl passerade tomater
1,5 dl matlagningsgrädde
1 dl riven ost
oregano
salt
400 g spaghetti
svartpeppar''')
                    print('''
1. Hacka löken och stek lök och färs i smör tills den fått färg. Riv i en morot, häll på passerade tomater och grädde.


2. Tillsätt riven ost och krydda med oregano, salt och peppar. Låt koka 5-10 minuter. Servera med spaghetti och paprika- och morotsstavar.''')
                if mat1 == "Pasta carbonara":
                    print()
                    print(f" Recept för {mat1}")
                    print()
                    print('''1 st gul lök
1/2 st röd paprika
1 paket bacon
3 dl vispgrädde, 40 %
1 msk smör
1 nypa salt
1 nypa svartpeppar
1 dl Ost
1 st färsk persilja
2 st äggula
Spaghetti 1/2 paket''')
                    print('''Klar
1. Finhacka löken och bryn i smöret tills den får lite färg, i med bacon och låt bryna tillsammans en liten stund.


2. Hacka resten av grönsakerna och blanda i. Låt bryna i ca 8 min på hög värme.


3. Tillsätt grädden och sänk värmen något. Salta och peppra efter smak. Låt puttra på svag värme i ca 15 min.


4. Ta bort från plattan och blanda i osten, äggulorna och persiljan. Dekorera gärna med knaprig bacon och några persiljeblad.


5. Klart! Smaklig måltid!''')
                
                if mat1 == "Köttbullar och makaroner":
                    print()
                    print(f" Recept för {mat1}")
                    print()
                    print('''600 g köttbullar
400 g makaroner
1,5 l vatten
2 st Morot
1/2 kruka Basilika
2 dl lättcreme fraiche
salt
peppar''')
                    print('''1. Koka upp vatten och salt.


2. Skär morötterna i små bitar. Koka morötter och makaroner tillsammans tills de blir mjuka.


3. Värm köttbullarna i ugnen i ca 10 minuter.


4. Värm upp makaronerna och morötterna tillsammans med crème fraiche och basilika. Smaka av med salt och peppar.''')
                
                if mat1 == "Korv och makaroner":
                    print()
                    print(f" Recept för {mat1}")
                    print()
                    print('''600 g
falukorv
5 dl
Idealmakaroner
smör''')
                    print('''1. Fyll en stor kastrull med ca. 2 liter vatten och låt vattnet koka upp medan du förbereder korven.


2. Skär korven i skivor.


3. Koka makaronerna enligt förpackningen.


4. Värm upp stekpannan och klicka i en matsked smör.


5. Stek korvskivorna (kom ihåg att sänka temperaturen på plattan så inte korven bränns).


6. Lägg upp färdigstekta korvslantar på ett fat eller tallrik.


7. Häll av vattnet från makaronerna i ett durkslag i diskhon.


8. Häll tillbaka makaronerna i kastrullen. Klicka i en matsked smör och rör om, då klibbar de ihop mindre!''')
                
                if mat1 == "Falafel":
                    print()
                    print(f" Recept för {mat1}")
                    print()
                    print('''2 st sötpotatis
240 g kikärtor, kokta
250 g färsk spenat
200 g gröna ärtor
1 dl Oatly iFraiche''')
                    print('''1. Sätt ugnen på 225 grader.


2. Skala potatisen och skär den i klyftor.


3. Lägg på en plåt med bakplåtspapper och ringla över olja (oliv- eller kokosolja), salt och peppar.


4. Gratinera i ugnen i 20 minuter.


5. Under tiden mixar du kikärtor, spenat, olja och 1 tsk torkad timjan till en formbar smet.


6. Forma till bollar (ca. 14 stycken blir lagom storlek) och lägg på samma plåt vid sidan av sötpotatisen som nu varit inne i 20 minuter.


7. Sänk ugnen till 200 grader och baka i 20 minuter.


8. Under tiden mixar du tinade gröna ärtor med havre fraiche. Smaka av med citronpeppar, salt, och peppar eller lite pressad citron.''')
                
                if mat1 == "Ostpaj":
                    print()
                    print(f" Recept för {mat1}")
                    print()
                    print('''1 st pajdeg
4 st ägg
2,5 dl matlagningsgrädde
3 dl västerbottensost
salt
peppar''')
                    print('''1. Sätt ugnen på 180 grader.


2. Förgrädda pajskalet i 5 minuter.


3. Vispa samman ägg, grädde och riven ost. Salta och peppra. Slå stanningen i pajskalet och grädda i 45-50 minuter.


4. Känn i mitten om stanningen stannat. Om pajen börjar få för mörk färg men fortfarande inte är färdig så täck med folie eller lock.''')
                
                if mat1 =="Bönbiffar med ris":
                    print()
                    print(f" Recept för {mat1}")
                    print()
                    print('''1 burk kidneybönor
1/2 st gul lök
1 st vitlöksklyfta
1 st ägg
2 msk potatismjöl
2 msk sesamfrö
1/2 tsk salt
1 krm svartpeppar
2 dl ris''')
                    print('''1. Mixa bönorna med skalad lök och vitlök i en matberedare.


2. Tillsätt ägg, potatismjöl och sesamfrön och blanda till en smet. Smaka av med salt och peppar.


3. Forma färsen till 8 runda biffar. Stek biffarna i oljan i en stekpanna ca 3 min per sida


4. Koka riset i 10-12 min''')
                break
        if meny == "q":
            print("Programmet avslutas")
            break
            

        else:
            print(f" {mat1} är inte ett alternativ")
            mat1 = input("Välj ett av alternativen: ")
                
    else:
        print("Ogiltigt alternativ! Försök igen.")
        mat = input("Vad är du sugen på?: ")


