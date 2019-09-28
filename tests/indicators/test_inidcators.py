import edgelord

security = edgelord.from_csv("tests/test_data/amd.csv")
print(security.indicators())