import edgelord

risk_free = 0.02
security = edgelord.from_csv("tests/test_data/amd.csv")
print(security.simple_moving_average())