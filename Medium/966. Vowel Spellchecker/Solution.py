class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """

        # Helper function: replace all vowels with '*'
        def devowel(word):
            return ''.join('*' if ch in 'aeiou' else ch for ch in word.lower())

        # 1. Exact words
        words_set = set(wordlist)

        # 2. Case-insensitive mapping
        case_map = {}
        # 3. Vowel-error mapping
        vowel_map = {}

        for word in wordlist:
            lower_word = word.lower()
            devowel_word = devowel(word)

            # Store first occurrence only
            if lower_word not in case_map:
                case_map[lower_word] = word
            if devowel_word not in vowel_map:
                vowel_map[devowel_word] = word

        # Process queries
        ans = []
        for query in queries:
            if query in words_set:  # Rule 1: exact match
                ans.append(query)
            elif query.lower() in case_map:  # Rule 2: case-insensitive
                ans.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:  # Rule 3: vowel error
                ans.append(vowel_map[devowel(query)])
            else:  # No match
                ans.append("")
        return ans
