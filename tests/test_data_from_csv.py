import edgelord

exit_code = 2

data = edgelord.data().from_csv("tests/test_data/amd.csv")

if len(data.dataframe().values) == 241:
    exit_code -= 1

    count = 0
    for column in data.columns.to_list():
        if column in data.columns_allowed:
            count += 1

    if count == len(data.columns_allowed):
        exit_code -= 1

exit(exit_code)