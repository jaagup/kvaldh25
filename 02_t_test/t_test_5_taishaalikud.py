from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Kooliõpetaja kutsus mõlemad oma tuppa kõneles nendega  natuke aega, käskis Arnol hoolas ja korralik ja seadis ta siis pinki ühe pikkade juustega poisi kõrvale istuma"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa Ei leia mina iial tääl see suure laia ilma pääl"

th="aeiouöäõü"
print(lause1.lower())
print([t for t in "koolimajja" if t in th])
print(len([t for t in "koolimajja" if t in th]))

def t_arv(sona):
    return len([t for t in sona if t in th])

print(t_arv("kalamaja"))
arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)
#Kuva ka teise teksti iga sõna täishäälikute arv, kontrolli pisteliselt
#Võrdle nende arvude aritmeetilisi keskmisi t-testiga
#Kuva kummagi arvujada aritmeetiline keskmine välja
