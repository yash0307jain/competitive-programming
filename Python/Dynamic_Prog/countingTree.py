def bar(n: int) -> int:
    if n <= 1:
        return n
    bar(n - 1)
    bar(n - 1)