import edgelord

for b in ["spy", "msft", "amd"]:
    security = edgelord.from_csv("tests/test_data/%s.csv" % b)
    print(security.value_at_risk(confidence=0.99))