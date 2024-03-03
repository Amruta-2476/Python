# 3) WAP to prevent print() to print a new line at the end
print("hello world")
print("new line")
'''def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None'''
# Solution= just change the default value of end
print("hello world", end=" ")
print("new line")