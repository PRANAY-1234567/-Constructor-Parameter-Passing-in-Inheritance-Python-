# 🧬 Constructor Parameter Passing in Inheritance (Python)

## 📌 Description

This Python program demonstrates how a child class passes a value to the parent class constructor using `super()`.

The value received by the child constructor is forwarded to the parent constructor during object creation.

---

## 🚀 Features

* Demonstrates inheritance
* Uses parameterized constructors
* Passes constructor arguments dynamically
* Uses `super()` for constructor chaining

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Base`

Contains parameterized constructor:

```python id="z4m8pl"
def __init__(self, x)
```

Receives value and prints it.

---

### 2️⃣ Child Class – `Derived`

```python id="q7x2mv"
class Derived(Base)
```

Contains constructor:

```python id="m1q9qa"
def __init__(self, v)
```

Uses:

```python id="p5m3zx"
super().__init__(v)
```

👉 Passes value of `v` to parent constructor.

---

## 💻 Code

```python id="r8m2pl"
class Base:
    def __init__(self, x):
        print("Inside class Base constructor, value is", x)


class Derived(Base):
    def __init__(self, v):
        super().__init__(v)
        print("Inside class Derived constructor")


if __name__ == "__main__":
    obj = Derived(157)
```

---

## ▶️ Output

```id="x6m4qa"
Inside class Base constructor, value is 157
Inside class Derived constructor
```

---

## 🧠 Key Concepts

### ✔ Parameterized Constructor

Constructors that accept arguments.

---

### ✔ Constructor Chaining

Execution flow:

```text id="n2q8mv"
Derived(157)
      ↓
Base(157)
      ↓
Derived()
```

---

### ✔ `super()` Keyword

```python id="k9m1pl"
super().__init__(v)
```

👉 Calls parent constructor and forwards argument.

---

## 📚 Concepts Used

* Inheritance
* Constructor chaining
* Parameterized constructor
* `super()` method

---

## ⚠️ Important Understanding

The value:

```python id="a4m7zx"
157
```

travels like this:

```text id="d8q3pt"
obj → Derived(v) → Base(x)
```

So:

```python id="v1m9qa"
v = 157
x = 157
```

---

## 🎯 Real-World Importance

This pattern is widely used in:

* GUI frameworks
* Game development
* Web frameworks
* Parent-child configuration systems

---

## 🔧 Future Improvements

* Store values in variables
* Add methods in both classes
* Add multilevel inheritance
* Pass multiple parameters

---

## 📄 License

This project is open-source and free to use.


<img width="658" height="685" alt="image" src="https://github.com/user-attachments/assets/da00b54c-341d-46e3-8fad-e5f7b2f705eb" />
