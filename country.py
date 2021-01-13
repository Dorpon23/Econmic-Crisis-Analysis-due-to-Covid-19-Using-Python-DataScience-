import pandas

data = pandas.read_csv("covid19.csv")


country = list(data["দেশের নাম"])
print(country)