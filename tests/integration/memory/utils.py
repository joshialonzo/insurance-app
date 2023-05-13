from insurance.repository.sanitizers.csv.file_sanitizer import (
    PaymentsFileSanitizer,
)
from insurance.repository.input.file_system import FileSystem
from insurance.repository.storage.memory import MemoryStorage
from insurance.services import (
    create_customer,
    create_agent,
    create_payment,
    create_policy,
    create_validity,
    register_payment_lines,
)


def get_first_line():
    """Retrieve first line from file"""
    file = "payments.csv"
    file_system = FileSystem(file=file)
    lines = file_system.file_path_lines()
    first_line = lines[0]
    return first_line


def test_create_payment_with_lines():
    # initialize the storage
    storage = MemoryStorage()

    # retrieve all the lines from file
    file = "payments.csv"
    file_system = FileSystem(file=file)
    lines = file_system.file_path_lines()
    sanitized_lines = PaymentsFileSanitizer(lines=lines).sanitize()

    # save all the lines in memory
    storage, registered = register_payment_lines(storage, sanitized_lines)

    # assert all the lines were saved
    assert len(registered) == 134
    assert len(storage.get_payments()) == 134
