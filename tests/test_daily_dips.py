import edgelord

risk_free = 0.02
security = edgelord.from_csv("tests/test_data/amd.csv")
print(security.indicators().daily_dips())
print(security.indicators().daily_dips(5))