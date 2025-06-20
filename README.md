# 🧠 Student Assessment: Python, ML, and Deep Learning

Welcome to the **Student Assessment Repo**! This project is designed to evaluate your understanding of three core areas:

- 🐍 Python Programming  
- 📊 Machine Learning (ML)  
- 🧠 Deep Learning (DL) with PyTorch  

Each section has problems to solve and automated tests to verify your solutions.

---

## 📁 Repository Structure

```
engages-onboarding/  
├── README.md  
├── requirements.txt  
├── run_all_tests.py

├── python/  
│   ├── problems/  
│   └── tests/

├── ml/  
│   ├── problems/  
│   └── tests/

├── deep_learning/  
│   ├── problems/  
│   └── tests/
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/meilongzhang/engages-onboarding.git
cd engages-onboarding
```

### 2. (Optional) Create a Virtual Environment

```bash
conda create -n onboarding python=3.10
conda activate onboarding
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running Tests

### Run All Tests

```bash
python run_all_tests.py
```

### Run a Specific Test File

```bash
python -m unittest python/tests/test_q1_sum.py
```

---

## 📝 How to Solve Problems

Each problem is located in its respective `problems/` folder.

```python
# Example: python/problems/q1_sum.py

def sum_two_numbers(a, b):
    """Return the sum of a and b."""
    pass  # Replace this with your implementation
```

- Only fill in the function body.
- Do **not** rename files or functions.
- Use the test files in `tests/` to check correctness.

---

## 🧠 Problem Categories

### 🐍 Python
- Variables and arithmetic
- Conditionals and loops
- Strings, lists, and dictionaries
- Writing functions

### 📊 Machine Learning
- Manual implementation of models (e.g., linear regression, k-NN)
- Accuracy calculation
- Basic data processing with pandas
- Plotting with matplotlib

### 🧠 Deep Learning
- Build and train neural networks using PyTorch
- Understand layers, activations, loss functions, optimizers
- Load and preprocess datasets (e.g., MNIST)

---

## 🧪 Example Workflow

1. Open `python/problems/q1_sum.py` and write your solution.
2. Run:

```bash
python -m unittest python/tests/test_q1_sum.py
```

3. Repeat for each problem and check that the tests pass.

---

## 📤 Submitting Your Work
After cloning this repository, please create your own private GitHub repository to store your work.

Create a new private repository on your GitHub account (e.g., yourname-onboarding).

Remove the existing remote from this repo:

```
git remote remove origin
```
Add your own GitHub repo as the new remote:
```
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```
Add, commit and push your code:
```
git add .
git commit -m "new submission"
git push -u origin main
```

Then, share your new repo with me.

## 🙌 Good Luck!

This assessment is designed to help you build confidence in programming and ML. Don’t worry if you don’t know something yet — read, experiment, and ask questions when needed!
