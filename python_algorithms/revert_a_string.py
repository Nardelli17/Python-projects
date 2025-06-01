def revert_string(s1: str):
    reversed_str = ""
    normal_str = ""
    for char in s1:
        normal_str = normal_str + char  # coloca o caractere no início da nova string
        reversed_str = char + reversed_str
    print(reversed_str)
    print(normal_str)

# Test cases
print(revert_string("listen"))