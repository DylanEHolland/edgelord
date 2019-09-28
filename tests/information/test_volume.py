import edgelord

security = edgelord.from_csv("tests/test_data/amd.csv")
print(security.volume())
print(security.volume(10))
print(security.volume(10, True))