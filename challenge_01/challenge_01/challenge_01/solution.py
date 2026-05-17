import re

def count_word_frequency(text):
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == "__main__":
    print("Running tests...\n")

    result = count_word_frequency("the cat sat on the mat the cat")
    assert result == {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
    print("✅ Test 1 passed:", result)

    result2 = count_word_frequency("Hello hello HELLO")
    assert result2 == {"hello": 3}
    print("✅ Test 2 passed:", result2)

    result3 = count_word_frequency("hello, world! hello.")
    assert result3 == {"hello": 2, "world": 1}
    print("✅ Test 3 passed:", result3)

    print("\n All tests passed!")
