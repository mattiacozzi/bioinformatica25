#Traccia:
#Come sopra, ma salva in formato XLSX.
import pandas as pd

attori = pd.read_csv("best-actor-age.csv")

#creo due dict
nuoviValoriFemale ={
    "Gender": "Female",
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Age": [29, 61, 45, 51, 64, 45, 61, 55, 45],
    "Name": ["Emma Stone", "Frances McDormand", "Olivia Colman", "Renee Zellweger", "Frances McDormand", "Jessica Chastain", "Michelle Yeoh", "Cate Blanchett", "Michelle Williams"],
    "Movie": ["La La Land", "Three Billboards Outside Ebbing, Missouri", "The Favourite", "Judy", "Nomadland", "The Eyes of Tammy Faye", "Everything Everywhere All at Once", "Tár", "The Fabelmans"]
}
nuoviValoriMale = {
    "Gender": "Male",
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Age": [39, 52, 44, 49, 84, 53, 60, 48, 52],
    "Name": ["Casey Affleck", "Gary Oldman", "Rami Malek", "Joaquin Phoenix", "Anthony Hopkins", "Will Smith", "Brendan Fraser", "Cillian Murphy", "Adrien Brody"],
    "Movie": ["Manchester by the Sea", "Darkest Hour", "Bohemian Rhapsody", "Joker", "The Father", "King Richard", "The Whale", "Oppenheimer", "The Brutalist"]
}

#costruisco i dataframe
dfFemale = pd.DataFrame(nuoviValoriFemale)
dfMale = pd.DataFrame(nuoviValoriMale)

#concateno tutto
final = pd.concat([attori,dfFemale,dfMale])

#salvo in XLSX
final.to_excel("best-actor-age-updated.xlsx")