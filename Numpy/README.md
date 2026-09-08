# 🧮 NumPy — From Arrays to AI/ML

<p align="center">
  <b>Build the numerical foundation you need before Machine Learning and AI.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/NumPy-Learning-blue?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/AI%2FML-Foundation-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Beginner%20→%20Intermediate-green?style=for-the-badge">
</p>

---

## 🗺️ Learning Path

This section is designed to make the transition from **array fundamentals → NumPy → AI/ML** natural.

```text
                 ARRAY FOUNDATION
                       │
                       ▼
                📘 basic.ipynb
                       │
          ┌────────────┴────────────┐
          │                         │
       Scalar                    Vector
          │                         │
          └────────────┬────────────┘
                       ▼
                 2D / Matrix
                       │
                       ▼
                    3D / Tensor
                       │
                       ▼
                  Shape + Axis
                       │
                       ▼
                📓 numpy.ipynb
                       │
                       ▼
              Numerical Computing
                       │
                       ▼
                 Data Handling
                       │
                       ▼
              🤖 Machine Learning
                       │
                       ▼
                 🧠 Deep Learning
                       │
                       ▼
                       AI
```

---

# 📘 `basic.ipynb`

> **Array foundation — no general Python basics.**

This notebook focuses specifically on the concepts needed to understand NumPy.

### What you learn

- Scalar
- Vector
- 1D array
- 2D array
- Matrix
- 3D array
- 4D arrays
- Tensor basics
- Dimensions
- Shape
- Rows and columns
- Axes
- Indexing
- Slicing
- Vector operations
- Matrix operations
- Dot product intuition
- Matrix multiplication intuition
- `*` vs `@`
- Basic broadcasting
- AI/ML array shapes

### Shape examples

```text
(5,)                 → 1D vector
(3, 4)               → 2D matrix
(2, 3, 4)            → 3D array
(224, 224, 3)        → RGB image
(32, 224, 224, 3)    → batch of RGB images
```

The goal is to develop **shape awareness** before learning more advanced NumPy.

---

# 🔢 `numpy.ipynb`

> **The main NumPy learning notebook.**

The notebook follows a traditional, hands-on style:

```text
┌──────────────────────┐
│      Concept         │
├──────────────────────┤
│ Short explanation    │
├──────────────────────┤
│ Code                 │
├──────────────────────┤
│ Output               │
├──────────────────────┤
│ Next concept         │
└──────────────────────┘
```

Instead of memorizing functions, the goal is to understand **what NumPy is doing to the data**.

---

# 📚 What We Cover

<details>
<summary><b>01 — Creating NumPy Arrays</b></summary>

- `np.array()`
- 1D arrays
- 2D arrays
- 3D arrays
- Nested arrays
- Arrays from tuples

</details>

<details>
<summary><b>02 — Array Properties</b></summary>

Understanding:

```python
arr.dtype
arr.ndim
arr.shape
arr.size
arr.itemsize
arr.nbytes
```

These properties are important when working with ML data, images and numerical datasets.

</details>

<details>
<summary><b>03 — Data Types</b></summary>

- `int8`
- `int16`
- `int32`
- `int64`
- `float32`
- `float64`
- `bool`
- `astype()`

Understanding `dtype` helps with numerical precision, memory usage and model/data compatibility.

</details>

<details>
<summary><b>04 — Creating Special Arrays</b></summary>

```python
np.zeros()
np.ones()
np.full()
np.empty()
np.eye()
```

</details>

<details>
<summary><b>05 — Number Sequences</b></summary>

```python
np.arange()
np.linspace()
```

</details>

<details>
<summary><b>06 — Random Arrays</b></summary>

```python
np.random.rand()
np.random.randint()
np.random.randn()
np.random.choice()
np.random.seed()
```

Also included:

```python
np.random.default_rng()
```

</details>

<details>
<summary><b>07 — Indexing</b></summary>

1D, 2D and 3D indexing:

```python
arr[0]
arr[-1]
arr[0, 1]
arr[1, 2, 0]
arr[:, 1]
```

</details>

<details>
<summary><b>08 — Slicing</b></summary>

```python
arr[1:5]
arr[:4]
arr[3:]
arr[::2]
arr[::-1]
```

Also includes 2D slicing for rows, columns and regions.

</details>

<details>
<summary><b>09 — Boolean & Fancy Indexing</b></summary>

```python
arr[arr > 20]
arr[arr % 2 == 0]
arr[[0, 2, 4]]
```

Useful for filtering and selecting data.

</details>

<details>
<summary><b>10 — Changing Array Values</b></summary>

Learn how to modify individual values and use conditions to update multiple values.

</details>

<details>
<summary><b>11 — Copy vs View</b></summary>

Understand the difference between:

```python
b = a
```

and:

```python
b = a.copy()
```

This prevents unexpected changes between arrays.

</details>

<details>
<summary><b>12 — Reshaping</b></summary>

```python
reshape()
flatten()
ravel()
```

Example:

```text
(12,)
  ↓
(3, 4)
  ↓
(2, 2, 3)
```

</details>

<details>
<summary><b>13 — Transpose & Axes</b></summary>

```python
arr.T
np.transpose()
np.swapaxes()
```

Learn how the arrangement of dimensions changes.

</details>

<details>
<summary><b>14 — Combining & Splitting Arrays</b></summary>

```python
np.concatenate()
np.vstack()
np.hstack()
np.stack()
np.split()
```

</details>

<details>
<summary><b>15 — Array Arithmetic</b></summary>

```python
+
-
*
/
**
```

and:

```python
np.add()
np.subtract()
np.multiply()
np.divide()
```

</details>

<details>
<summary><b>16 — Comparison & Logical Operations</b></summary>

```python
>
<
==
!=
```

and:

```python
np.logical_and()
np.logical_or()
np.logical_not()
```

</details>

<details>
<summary><b>17 — Universal Functions</b></summary>

```python
np.sqrt()
np.square()
np.exp()
np.sin()
np.cos()
np.floor()
np.ceil()
np.round()
```

</details>

<details>
<summary><b>18 — Aggregation & Statistics</b></summary>

```python
np.sum()
np.mean()
np.min()
np.max()
np.std()
np.var()
```

Also learn aggregation using `axis`.

</details>

<details>
<summary><b>19 — Finding Positions</b></summary>

```python
np.argmin()
np.argmax()
```

</details>

<details>
<summary><b>20 — Conditional Operations</b></summary>

```python
np.where()
```

Useful for condition-based selection and replacement.

</details>

<details>
<summary><b>21 — Sorting & Unique Values</b></summary>

```python
np.sort()
np.unique()
```

Including unique-value counts.

</details>

<details>
<summary><b>22 — Broadcasting</b></summary>

One of the most important NumPy concepts for AI/ML.

Example:

```text
Matrix              Vector

1  2  3       +     10  20  30
4  5  6

              ↓

11  22  33
14  25  36
```

You learn how NumPy performs operations between compatible shapes.

</details>

<details>
<summary><b>23 — Adding & Removing Dimensions</b></summary>

```python
np.newaxis
np.expand_dims()
np.squeeze()
```

Very useful when preparing data for ML models.

</details>

<details>
<summary><b>24 — Matrix Operations</b></summary>

Understand the important difference:

```python
A * B
```

versus:

```python
A @ B
```

Also:

```python
np.dot()
```

</details>

<details>
<summary><b>25 — Linear Algebra</b></summary>

Basic operations including:

```python
np.linalg.det()
np.linalg.inv()
np.linalg.eig()
np.linalg.solve()
```

These provide useful mathematical foundations for ML.

</details>

<details>
<summary><b>26 — NaN & Infinity</b></summary>

```python
np.nan
np.inf
np.isnan()
np.isinf()
np.isfinite()
np.nanmean()
```

Useful when working with real-world numerical data.

</details>

<details>
<summary><b>27 — Saving & Loading Arrays</b></summary>

```python
np.save()
np.load()
np.savez()
```

</details>

<details>
<summary><b>28 — NumPy Performance</b></summary>

Learn the idea behind efficient array-based, vectorized computation.

Instead of manually processing values one by one:

```python
arr * 2
```

can operate on the whole array.

</details>

---

# 🤖 Why NumPy Helps in AI/ML

Machine Learning is fundamentally built around **numbers**.

A dataset can be represented as an array:

```text
height   weight   age
 170       65      20
 180       80      25
 160       55      19
 175       70      30
```

Conceptually:

```python
X.shape
```

```text
(4, 3)
```

Meaning:

```text
4 samples
3 features
```

NumPy gives us tools to efficiently:

| Task | NumPy helps with |
|---|---|
| Store data | Numerical arrays |
| Transform data | Reshape, transpose, concatenate |
| Filter data | Boolean indexing |
| Calculate statistics | Mean, sum, std, variance |
| Scale data | Mathematical operations |
| Matrix calculations | `@`, `dot`, `linalg` |
| Prepare data | Shape and dimension manipulation |
| Work with images | Multi-dimensional arrays |

---

# 🖼️ NumPy & Computer Vision

Images are numerical data too.

A color image can be represented as:

```text
(height, width, channels)
```

For example:

```text
(224, 224, 3)
```

means:

```text
224 → height
224 → width
3   → RGB channels
```

A batch of images could be:

```text
(32, 224, 224, 3)
```

meaning:

```text
32 images
224 height
224 width
3 channels
```

This is why understanding **higher-dimensional arrays** is important before learning deep learning and computer vision.

---

# 📊 NumPy & Machine Learning Data

A very common ML representation is:

```text
(samples, features)
```

For example:

```text
(1000, 20)
```

means:

```text
1000 samples
20 features
```

A typical pipeline can be thought of as:

```text
Raw Data
   │
   ▼
NumPy Arrays
   │
   ▼
Cleaning / Filtering
   │
   ▼
Transformation
   │
   ▼
Scaling
   │
   ▼
Machine Learning Model
```

---

# 🧠 The Big Picture

The important relationship is:

```text
Numbers
   ↓
Arrays
   ↓
NumPy
   ↓
Numerical Computation
   ↓
Data Preparation
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
AI
```

> **NumPy is not a Machine Learning library.**

Its importance is that it provides a powerful foundation for working with numerical data.

Many Python data-science and ML tools also work with array-like numerical structures, so understanding NumPy makes later concepts much easier.

---

# 🎯 What You Should Understand After This

You should be able to look at:

```python
X.shape
```

and understand what it represents.

### Example 1

```text
(1000, 20)
```

→ **1000 samples × 20 features**

### Example 2

```text
(224, 224, 3)
```

→ **one RGB image**

### Example 3

```text
(32, 224, 224, 3)
```

→ **32 RGB images**

This ability to understand **shape, dimensions and data structure** is one of the most important foundations for Machine Learning and Deep Learning.

---

# 🛣️ Learning Order

```text
01  📘 basic.ipynb
       Array fundamentals
              ↓
02  🔢 numpy.ipynb
       NumPy foundation
              ↓
03  🐼 Pandas
       Data handling
              ↓
04  📊 Data Visualization
       Understand data visually
              ↓
05  📐 Statistics
       Understand data mathematically
              ↓
06  🤖 Machine Learning
       Train models
              ↓
07  🧠 Deep Learning
       Neural networks
              ↓
08  🚀 AI
       Larger AI concepts & applications
```

---

# ✅ NumPy Checklist

### Foundation

- [ ] Understand scalar
- [ ] Understand vector
- [ ] Understand 1D arrays
- [ ] Understand 2D arrays
- [ ] Understand matrices
- [ ] Understand 3D arrays
- [ ] Understand tensors
- [ ] Understand dimensions
- [ ] Understand shape
- [ ] Understand axes

### NumPy

- [ ] Create NumPy arrays
- [ ] Understand `dtype`
- [ ] Understand `ndim`
- [ ] Understand `shape`
- [ ] Understand `size`
- [ ] Understand `itemsize`
- [ ] Understand `nbytes`
- [ ] Create zeros / ones / full arrays
- [ ] Use `arange()`
- [ ] Use `linspace()`
- [ ] Generate random arrays
- [ ] Use indexing
- [ ] Use slicing
- [ ] Use boolean indexing
- [ ] Use fancy indexing
- [ ] Modify arrays
- [ ] Understand copy vs view
- [ ] Reshape arrays
- [ ] Flatten arrays
- [ ] Transpose arrays
- [ ] Combine arrays
- [ ] Split arrays
- [ ] Perform arithmetic
- [ ] Use universal functions
- [ ] Calculate statistics
- [ ] Understand `axis`
- [ ] Use `where()`
- [ ] Sort arrays
- [ ] Find unique values
- [ ] Understand broadcasting
- [ ] Add/remove dimensions
- [ ] Understand matrix multiplication
- [ ] Use basic linear algebra
- [ ] Handle NaN and infinity
- [ ] Save and load arrays
- [ ] Understand ML dataset shapes
- [ ] Understand image shapes

---

# 🧪 Practice Mindset

Don't learn NumPy by only memorizing:

```python
np.mean()
np.reshape()
np.concatenate()
```

Instead, always ask:

> **What is the shape of my data?**

> **What does each dimension represent?**

> **Which axis am I working on?**

> **What will the output shape be?**

For AI/ML, this way of thinking is often more important than memorizing individual functions.

---

<div align="center">

### 🚀 Goal

**Understand the data → Understand the shape → Understand the operation → Build toward AI/ML**

⭐ Keep practicing. Build intuition, not just a list of functions.

</div>

