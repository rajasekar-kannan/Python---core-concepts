"""
generators_real_world_examples.py

Real-world use cases for generators and lazy iteration:
1. API-style paginated responses
2. Heavy data processing
3. Large file reading
"""

# =========================
# Generator Logic Section
# =========================

def api_response_generator(pages):
    """
    Simulates a paginated API response.
    Each page is fetched only when needed.
    """
    for page in pages:
        yield page


def heavy_data_generator(size):
    """
    Simulates processing a heavy dataset lazily.
    Avoids loading everything into memory.
    """
    for i in range(size):
        yield i * i


def read_large_file_lazy(file_path):
    """
    Reads a file line by line lazily.
    Very common real-world generator usage.
    """
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


def filter_errors(log_lines):
    """
    Generator pipeline to filter log errors.
    """
    for line in log_lines:
        if "ERROR" in line:
            yield line


# =========================
# Pytest Test Section
# =========================

def test_api_response_generator():
    pages = [
        {"page": 1, "data": ["a", "b"]},
        {"page": 2, "data": ["c", "d"]},
    ]

    gen = api_response_generator(pages)
    assert next(gen)["page"] == 1
    assert next(gen)["page"] == 2


def test_heavy_data_generator():
    gen = heavy_data_generator(5)
    assert list(gen) == [0, 1, 4, 9, 16]


def test_read_large_file_lazy(tmp_path):
    file = tmp_path / "sample.log"
    file.write_text(
        "INFO start\n"
        "ERROR something failed\n"
        "INFO end\n"
    )

    gen = read_large_file_lazy(file)
    assert list(gen) == [
        "INFO start",
        "ERROR something failed",
        "INFO end",
    ]


def test_generator_pipeline_file_filter(tmp_path):
    file = tmp_path / "app.log"
    file.write_text(
        "INFO init\n"
        "ERROR db connection\n"
        "ERROR timeout\n"
        "INFO shutdown\n"
    )

    lines = read_large_file_lazy(file)
    errors = filter_errors(lines)

    assert list(errors) == [
        "ERROR db connection",
        "ERROR timeout",
    ]
