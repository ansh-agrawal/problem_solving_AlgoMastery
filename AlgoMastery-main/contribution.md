# Contributing to AlgoMastery

Thank you for your interest in contributing to **AlgoMastery**! This guide will help you add new problems, tests, or improve existing ones.

---

## 📝 How to Contribute

1. **Fork the repository** and clone your fork locally.

2. **Add a new problem:**
   - Place the problem in the appropriate folder:
     - `problems/easy/`
     - `problems/medium/`
     - `problems/hard/`
   - Follow the naming convention: `pXXX_problem_name.py`
   - Include a **docstring**, **function stub**, and **type hints**.

3. **Add corresponding tests:**
   - Place tests in `tests/` folder matching the problem difficulty.
   - Follow the naming convention: `test_pXXX_problem_name.py`
   - Include **at least 3 canonical test cases** using `pytest`.

4. **Ensure consistency:**
   - Clear problem description with examples.
   - Maintain function signature and typing.
   - Avoid ambiguity in indexing or input/output descriptions.

5. **Run tests:**
```bash
pytest tests/
```
   - Ensure all existing tests pass before submitting your changes.

6. **Submit a Pull Request:**
   - Provide a descriptive title and explanation of your changes.

---

## ⚡ Coding Guidelines

- Use **snake_case** for function names.
- Use **type hints** for all function parameters and return types.
- Include **docstrings** with:
  - Problem description
  - Args / Returns
  - Example input/output
- Keep code **readable and modular**.

---

## 🙏 Thank You
Your contributions help learners worldwide practice and master algorithms efficiently. Keep solving, keep learning!

