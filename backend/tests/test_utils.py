from app.utils.formatting import to_shorter_number


def test_human_readable_number_trillions():
    assert to_shorter_number(1_500_000_000_000) == "1.50T"
    assert to_shorter_number(-2_300_000_000_000) == "-2.30T"
    assert to_shorter_number(999_999_999_999) == "1000.00B"


def test_human_readable_number_billions():
    assert to_shorter_number(1_500_000_000) == "1.50B"
    assert to_shorter_number(-2_300_000_000) == "-2.30B"
    assert to_shorter_number(999_999_999) == "1000.00M"


def test_human_readable_number_millions():
    assert to_shorter_number(1_500_000) == "1.50M"
    assert to_shorter_number(-2_300_000) == "-2.30M"
    assert to_shorter_number(999_999) == "1000.00K"


def test_human_readable_number_thousands():
    assert to_shorter_number(1_500) == "1.50K"
    assert to_shorter_number(-2_300) == "-2.30K"
    assert to_shorter_number(999) == "999"


def test_human_readable_number_less_than_thousand():
    assert to_shorter_number(500) == "500"
    assert to_shorter_number(-300) == "-300"
    assert to_shorter_number(999.99) == "999.99"
    assert to_shorter_number(0) == "0"


def test_human_readable_number_decimal_places():
    assert to_shorter_number(1_234_567_890) == "1.23B"
    assert to_shorter_number(1_234_567) == "1.23M"
    assert to_shorter_number(1_234) == "1.23K"
    assert to_shorter_number(1.234) == "1.23"
