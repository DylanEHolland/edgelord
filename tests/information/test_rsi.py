import edgelord

security = edgelord.from_csv("tests/test_data/amd.csv")

for b in ["spy", "msft"]:
    benchmark = edgelord.from_csv("tests/test_data/%s.csv" % b)
    print(security.indicators().rsi())