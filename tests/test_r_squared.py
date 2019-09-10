import edgelord

risk_free = 0.02
security = edgelord.from_csv("tests/test_data/amd.csv")
benchmark = edgelord.from_csv("tests/test_data/msft.csv")
print(security.benchmark(benchmark).r_squared())