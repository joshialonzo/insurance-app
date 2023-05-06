from insurance.repository.file_system import Storage


def test_file_is_created():
    file = "payments.csv"
    storage = Storage(file=file)
    assert (
        "data/insurance/payments.csv"
        in str(storage.file_path)
    )


def test_file_exists():
    file = "payments.csv"
    storage = Storage(file=file)
    assert storage.file_path_exists()


def test_file_path_content():
    file = "payments.csv"
    storage = Storage(file=file)
    content = storage.file_path_content()
    assert len(content) > 0
