# 1935. Maximum Number of Words You Can Type

## 📘 Problem Statement
There is a malfunctioning keyboard where some letter keys do not work.  
All other keys on the keyboard work properly.  

Given:
- A string `text` of words separated by a single space (no leading or trailing spaces).
- A string `brokenLetters` of all distinct letter keys that are broken.  

Return the **number of words in `text` you can fully type** using this keyboard.

---

## 🔹 Examples

### Example 1
**Input:**  
```py
text = "hello world", brokenLetters = "ad"
```
**Output:**  
```py
1
```
**Explanation:**  
We cannot type `"world"` because the `'d'` key is broken.

---
## 🔹 Constraints
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- `brokenLetters` consists of distinct lowercase English letters.

---

## 💡 Approach
1. Convert `brokenLetters` into a **set** for fast lookup.  
2. Split the sentence into words using `.split()`.  
3. For each word, check if it contains any broken letter.  
   - If not, it is a valid word and contributes to the count.  
4. Return the count of such words.

This approach runs in **O(n * m)** where `n` is the number of words and `m` is the average word length.  
Since each letter is checked at most once per word, it’s efficient for the given constraints.

---
