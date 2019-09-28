import edgelord

risk_free = 0.02
for f in ["amd", "msft", "spy"]:
    security = edgelord.from_csv("tests/test_data/%s.csv" % (f))
    print(security.sharpe())