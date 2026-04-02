def filter_by_currency():
    pass


@pytest.mark.parametrize("input_set, output_set", [
    ("1234123412341234", "1234 12** **** 1234"),
    ("12341234123412344", ""),
    ("123412341234123t", ""),
    ("123412342341234", "")
])
def transaction_descriptions():
    pass


@pytest.mark.parametrize("input_set, output_set", [
    ("1234123412341234", "1234 12** **** 1234"),
    ("12341234123412344", ""),
    ("123412341234123t", ""),
    ("123412342341234", "")
])
def card_number_generator():
    pass