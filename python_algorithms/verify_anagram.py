def are_anagrams(s1: str, s2: str) -> bool:
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    # Assuming only lowercase letters a-z
    count = [0] * 26

    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1
        count[ord(s2[i]) - ord('a')] -= 1

    # If all counts return to zero, it's an anagram
    for c in count:
        if c != 0:
            return False

    return True

# Test cases
print(are_anagrams("listen", "silent"))      # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("hello", "bello"))        # False
