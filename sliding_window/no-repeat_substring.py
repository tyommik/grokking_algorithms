"""
Дана строка, найти длинну наибольшей подстроки, которая не имеет повторяющихся букв

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".


Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".


"""


def non_repeat_substring_my(array: str) -> int:
    max_length = 0
    char_freq = {}
    window_start = 0
    for idx, char in enumerate(array):
        char_freq[char] = char_freq.setdefault(char, 0) + 1

        if char_freq[char] > 1:
            char_freq = {}
            window_start = idx
        max_length = max(max_length, idx - window_start + 1)

    return max_length


def non_repeat_substring(array: str) -> int:
    max_length = 0
    char_freq = {}
    window_start = 0
    for idx, char in enumerate(array):
        if char in char_freq:
            window_start = max(window_start, idx)
        char_freq[char] = True
        max_length = max(max_length, idx - window_start + 1)
    return max_length


def main():
    # print("Length of the longest substring: " + str(non_repeat_substring_my("aabccbb")))
    # print("Length of the longest substring: " + str(non_repeat_substring_my("abbbb")))
    # print("Length of the longest substring: " + str(non_repeat_substring_my("abccde")))

    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()
