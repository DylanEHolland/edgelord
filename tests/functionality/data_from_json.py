import edgelord

exit_code = 2

security = edgelord.from_json("tests/test_data/amd.json")
print(security.data.frame())
exit(-1)
if len(security.data.frame().values) == 289:
    exit_code -= 1

    count = 0
    for column in security.data.columns.to_list():
        if column in security.data.columns_allowed:
            count += 1

    if count == len(security.data.columns_allowed):
        exit_code -= 1

exit(exit_code)