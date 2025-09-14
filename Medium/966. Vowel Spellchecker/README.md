# 966. Vowel Spellchecker

## 📌 Problem Description
We want to implement a **spellchecker** that converts a query word into a correct word based on a given **wordlist**.

The spellchecker handles **two types of mistakes**:

1. **Capitalization Errors**  
   - Words are matched case-insensitively.  
   - If matched, return the word from the wordlist with its original case.  

   **Examples**:  
   - wordlist = ["yellow"], query = "YellOw" → output = "yellow"  
   - wordlist = ["Yellow"], query = "yellow" → output = "Yellow"  

2. **Vowel Errors**  
   - All vowels `a, e, i, o, u` are considered interchangeable.  
   - If replacing vowels still matches a word, return the word from the wordlist.  

   **Examples**:  
   - wordlist = ["YellOw"], query = "yollow" → output = "YellOw"  
   - wordlist = ["YellOw"], query = "yllw" → output = "" (no match)  

---

## 🧾 Matching Rules (Precedence)
1. If the query matches **exactly** (case-sensitive), return the exact word.  
2. If the query matches by ignoring capitalization, return the **first match** from wordlist.  
3. If the query matches by ignoring vowel differences, return the **first match** from wordlist.  
4. If no match is found, return an **empty string** `""`.  

---

## 🔑 Example 1

**Input**:  
```python
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
```
### Output:
```
["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```
