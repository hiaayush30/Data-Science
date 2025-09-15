**all commonly used methods** for **tuple, set, and dictionary in Python** with **one-line explanations and code examples**.

---

## 🟣 Tuple Methods (only 2 built-in)

```python
t = (1, 2, 3, 2)

print(t.count(2))   # count(): returns number of occurrences of a value → 2
print(t.index(3))   # index(): returns first index of a value → 2
```

---

## 🟢 Set Methods

```python
s = {1, 2, 3}
s2 = {3, 4, 5}

s.add(4)            # add(): adds an element → {1,2,3,4}
s.remove(2)         # remove(): removes element, error if not found → {1,3,4}
s.discard(5)        # discard(): removes element, no error if not found
s.pop()             # pop(): removes & returns random element
s.clear()           # clear(): removes all elements → set()
s.copy()            # copy(): returns shallow copy of set

s.union(s2)         # union(): returns all unique elements → {1,3,4,5}
s.intersection(s2)  # intersection(): common elements → {3,4}
s.difference(s2)    # difference(): elements only in s → {1}
s.symmetric_difference(s2)  # symmetric_difference(): elements not common → {1,5}

s.issubset(s2)      # issubset(): True if all elements of s in s2
s.issuperset(s2)    # issuperset(): True if s contains all of s2
s.isdisjoint({6})   # isdisjoint(): True if no common elements
```

---

## 🟡 Dictionary Methods

```python
d = {"a": 1, "b": 2, "c": 3}

d.get("a")          # get(): returns value for key, None if not found → 1
d.keys()            # keys(): returns all keys → dict_keys(['a','b','c'])
d.values()          # values(): returns all values → dict_values([1,2,3])
d.items()           # items(): returns key-value pairs → dict_items([('a',1),...])

d.update({"d": 4})  # update(): adds/updates key-value pairs
d.pop("b")          # pop(): removes key & returns its value → 2
d.popitem()         # popitem(): removes & returns last inserted item
d.setdefault("e", 5)  # setdefault(): returns value if key exists else adds it
d.clear()           # clear(): removes all items
d.copy()            # copy(): returns shallow copy
```

---

Got it ✅ — now let’s make a **complete cheat sheet** for you:

* **Tuple methods**
* **List methods**
* **Built-in functions** (like `enumerate()`, `len()`, etc.) that can be used with **both lists & tuples**.

---

## 🟣 Tuple Methods (immutable, only 2)

```python
t = (1, 2, 3, 2)

t.count(2)   # count(): returns number of occurrences → 2
t.index(3)   # index(): returns first index of a value → 2
```

---

## 🟢 List Methods (mutable, many)

```python
lst = [1, 2, 3, 2]

lst.append(4)         # append(): adds element at end → [1,2,3,2,4]
lst.extend([5, 6])    # extend(): adds multiple elements → [1,2,3,2,4,5,6]
lst.insert(1, 10)     # insert(): inserts at index → [1,10,2,3,...]

lst.remove(2)         # remove(): removes first matching value → [1,10,3,...]
lst.pop()             # pop(): removes & returns last element → 6
lst.pop(1)            # pop(index): removes & returns element at index → 10
lst.clear()           # clear(): removes all elements → []

lst.index(3)          # index(): returns index of first match → 2
lst.count(2)          # count(): returns occurrences of a value → 1

lst.sort()            # sort(): sorts list in-place → [1,2,3,4,5]
lst.sort(reverse=True)# sort(reverse=True): descending order
lst.reverse()         # reverse(): reverses list in-place

lst.copy()            # copy(): returns shallow copy of list
```

---

## 🟡 Built-in Functions (usable with both list & tuple)

```python
lst = [10, 20, 30]
t   = (5, 15, 25)

len(lst)              # len(): number of elements → 3
max(t)                # max(): largest element → 25
min(lst)              # min(): smallest element → 10
sum(lst)              # sum(): adds all numbers → 60

sorted(t)             # sorted(): returns new sorted list → [5,15,25]
reversed(lst)         # reversed(): returns iterator in reverse order → [30,20,10]

enumerate(lst)        # enumerate(): returns (index, value) pairs
list(enumerate(lst))  # → [(0,10), (1,20), (2,30)]

any([0, 0, 1])        # any(): True if at least one True value → True
all([1, 2, 3])        # all(): True if all values are True → True

zip(lst, t)           # zip(): pairs elements from both → [(10,5),(20,15),(30,25)]

tuple(lst)            # tuple(): converts list → (10,20,30)
list(t)               # list(): converts tuple → [5,15,25]
```

---

✅ **Summary:**

* **Tuple:** `.count()`, `.index()`
* **List:** `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.clear()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()`
* **Functions usable with both:** `len()`, `max()`, `min()`, `sum()`, `sorted()`, `reversed()`, `enumerate()`, `any()`, `all()`, `zip()`, `tuple()`, `list()`

---
Let’s now add **all operators** (along with methods + functions) for **list, tuple, set, and dict** in Python.

---

### Operators

```python
(1, 2) + (3, 4)     # + : concatenation → (1,2,3,4)
(1, 2) * 3          # * : repetition → (1,2,1,2,1,2)
3 in (1, 2, 3)      # in : membership test → True
2 not in (4, 5)     # not in : membership test → True
```

---

# 🟢 List

👉 **Mutable sequence** → rich set of methods and operators.

### Methods

```python
lst = [1, 2, 3]
lst.append(4)      # add element at end
lst.extend([5, 6]) # add multiple elements
lst.insert(1, 10)  # insert at index
lst.remove(2)      # remove first occurrence
lst.pop()          # remove last (or index) element
lst.clear()        # remove all elements
lst.index(3)       # find index of first occurrence
lst.count(3)       # count occurrences
lst.sort()         # sort ascending
lst.reverse()      # reverse order
lst.copy()         # shallow copy
```

### Operators

```python
[1, 2] + [3, 4]     # + : concatenation → [1,2,3,4]
[1, 2] * 2          # * : repetition → [1,2,1,2]
3 in [1, 2, 3]      # in : membership test → True
```

---

# 🟠 Set

👉 **Unordered, unique elements** → many methods + operators.

### Methods

```python
s = {1, 2, 3}; s2 = {3, 4, 5}
s.add(4)                # add element
s.remove(1)             # remove (error if not found)
s.discard(10)           # remove (no error if not found)
s.pop()                 # remove & return random element
s.clear()               # clear all elements
s.copy()                # shallow copy

s.union(s2)             # union
s.intersection(s2)      # intersection
s.difference(s2)        # difference
s.symmetric_difference(s2)  # symmetric difference

s.issubset(s2)          # subset test
s.issuperset(s2)        # superset test
s.isdisjoint(s2)        # no common elements?
```

### Operators

```python
{1, 2} | {2, 3}     # | : union → {1,2,3}
{1, 2} & {2, 3}     # & : intersection → {2}
{1, 2} - {2, 3}     # - : difference → {1}
{1, 2} ^ {2, 3}     # ^ : symmetric difference → {1,3}

2 in {1, 2, 3}      # in : membership test → True
```

---

# 🟡 Dictionary

👉 **Key-value pairs** → rich methods + merging operator.

### Methods

```python
d = {"a": 1, "b": 2}

d.get("a")          # get value safely → 1
d.keys()            # all keys
d.values()          # all values
d.items()           # all key-value pairs
d.update({"c": 3})  # add/update key-value
d.pop("b")          # remove by key
d.popitem()         # remove last inserted
d.setdefault("d", 4) # get or insert default
d.clear()           # clear all items
d.copy()            # shallow copy
```

### Operators

```python
{"a": 1} | {"b": 2}     # | : merge dicts → {'a':1, 'b':2}
{"a": 1} | {"a": 5}     # | : right-side overwrites → {'a':5}

"a" in {"a": 1}         # in : check key existence → True
```

---

# 🟢 Common Built-in Functions (for all sequences + sets + dicts)

```python
len([1,2,3])        # number of elements → 3
max((1,5,2))        # largest element → 5
min([1,5,2])        # smallest element → 1
sum([1,2,3])        # sum → 6

sorted({3,1,2})     # returns sorted list → [1,2,3]
reversed((1,2,3))   # reverse iterator → [3,2,1]

enumerate(["a","b"]) # index-value pairs → [(0,'a'),(1,'b')]
any([0,1,0])        # True if any element is True → True
all([1,2,3])        # True if all are True → True

zip([1,2],[3,4])    # pairs → [(1,3),(2,4)]
list((1,2,3))       # convert tuple → [1,2,3]
tuple([1,2,3])      # convert list → (1,2,3)
set([1,2,2,3])      # convert & remove duplicates → {1,2,3}
dict([("a",1),("b",2)]) # create dict from pairs → {'a':1,'b':2}
```

---

✅ Now you have **methods + operators + built-in functions** for **list, tuple, set, and dict** in one place.

👉 Do you want me to prepare a **single comparison table** (object type × methods × operators × functions) so you can **revise quickly for interviews/exams**?
