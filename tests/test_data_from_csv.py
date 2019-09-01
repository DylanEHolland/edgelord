import edgelord

exit_code = 2

security = edgelord.from_csv("tests/test_data/amd.csv")
print(security)
if len(security.data.frame().values) == 241:
    exit_code -= 1

    count = 0
    for column in security.data.columns.to_list():
        if column in security.data.columns_allowed:
            count += 1

    if count == len(security.data.columns_allowed):
        exit_code -= 1

exit(exit_code)