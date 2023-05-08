from insurance.repository.input.file_system import FileSystem


def test_file_is_created():
    file = "payments.csv"
    storage = FileSystem(file=file)
    assert (
        "data/insurance/payments.csv"
        in str(storage.file_path)
    )


def test_file_exists():
    file = "payments.csv"
    storage = FileSystem(file=file)
    assert storage.file_path_exists()


def test_file_path_content():
    file = "payments.csv"
    storage = FileSystem(file=file)
    content = storage.file_path_content()
    assert len(content) > 0


def test_file_path_lines():
    file = "payments.csv"
    storage = FileSystem(file=file)
    lines = storage.file_path_lines()
    assert len(lines) > 0
