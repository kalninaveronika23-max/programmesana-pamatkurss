"""
Programma aprēķina spēlētāja atlikušos dzīvības punktus pēc saņemtā uzbrukuma
Autore: Veronika Kalniņa
"""

# Spēlētāja sākotnējie dati pirms cīņas sākuma
speletaja_vards = "Anna"
hp_punkti = 100
uzbrukuma_jauda = 25

# Aprēķinām veselības stāvoki pēc pretinieka sitiena
atlikusie_hp_punkti = hp_punkti - uzbrukuma_jauda

# Parādām aktuālo informāciju spēlētājam uz ekrāna
print(speletaja_vards)
print(hp_punkti)
print(uzbrukuma_jauda)
print(atlikusie_hp_punkti)
