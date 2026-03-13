# Contributing Guide

Thank you for your interest in contributing to the Student Utility Library! This guide will help you make your first contribution.

---

## 🎯 How to Contribute

### 1. Choose a Function

Look for functions marked with:

```python
# TODO: Implement this function
```

Start with easy ones, then move to harder ones.

---

### 2. Recommended Order

**Easy:**
- `src/string_utils/`: `reverse_string()`, `count_words()`, `capitalize_words()`
- `src/math_utils/`: `factorial()`, `is_prime()`, `mean()`

**Intermediate:**
- `src/string_utils/`: `is_palindrome()`, `count_characters()`, `is_anagram()`
- `src/math_utils/`: `gcd()`, `lcm()`, `fibonacci()`, `median()`
- `src/file_utils/`: `read_file()`, `write_file()`, `count_lines()`

**Advanced:**
- `src/data_structures/`: `Stack`, `Queue`, `LinkedList`, etc.
- `src/algorithms/`: Sorting and searching
- `src/file_utils/`: CSV/JSON handling

---

### 3. Steps to Implement

1. **Read the docstring**
   - What the function does  
   - Inputs and outputs  
   - Examples  

2. **Check the tests**
   - Look in `tests/` to understand expected output  

3. **Write the code**
   - Replace `pass` with your logic  

4. **Test your function**

```bash
python -m pytest tests/test_string_utils.py::TestStringUtils::test_reverse_string -v
```

5. **Run all tests**

```bash
python -m pytest tests/ -v
```

---

## 🔧 Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run tests:

```bash
python -m pytest tests/ -v
```

3. Run examples:

```bash
python examples/basic_usage.py
```

---

## 📝 Coding Rules

- Follow PEP 8  
- Use clear variable names  
- Add type hints  
- Write docstrings for new functions  

---

### Example

```python
def reverse_string(text: str) -> str:
    """
    Reverse the given string.
    """
    return text[::-1]
```

---

### Test Example

```python
from src.string_utils import reverse_string
print(reverse_string("hello"))  # olleh
```

---

## 🏆 Recognition

- Your name in README  
- Your commits in Git history  
- Useful for your portfolio  

---

## 🐛 Found a Bug?

1. Create an issue  
2. Fix it (optional)  
3. Add test cases  

---

## 💡 Tips

### Beginners:
- Start small  
- Read docstrings carefully  
- Check test cases  
- Use print for debugging  

### Experienced:
- Handle edge cases  
- Focus on readability  
- Add extra tests  
- Help others  

---

### Avoid These Mistakes:
- Ignoring edge cases  
- Changing function signature  
- Not following docstring  
- Not testing code  

---

## 📚 Resources

- Python Tutorial  
- PEP 8  
- Type Hints  
- pytest docs  
- Algorithms (Visualgo)  

---

## 🤝 Need Help?

- Read docstring again  
- Check test cases  
- Look at TODO hints  
- Ask in discussions  
- Search online  

---

## 🎉 First Contribution

1. Pick `reverse_string()`  
2. Understand it  
3. Check tests  
4. Implement  
5. Run tests  
6. Done 🎊  

---

Every expert started as a beginner—just start 🚀