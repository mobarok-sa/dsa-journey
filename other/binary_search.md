### Binary search pseudocode
Binary search is a fast way to find something in a sorted list. The list must be sorted. The idea
of Binary Search is, You don’t check one by one.  You always check the middle. Then you throw away half of the list.

**Check middle → go left or right → repeat.** 

```text
BinarySearch(list, target):

    left  ← 0
    right ← length(list) - 1

    while left ≤ right:

        mid ← (left + right) // 2

        if list[mid] == target:
            return mid     (found)

        else if target < list[mid]:
            right ← mid - 1

        else:
            left ← mid + 1

    return -1   (not found)
```

### Meaning

* `left`  → start of the list
* `right` → end of the list
* `mid`   → middle index

Loop:

* check the middle
* if your value is smaller → go left
* if your value is bigger → go right


**Note: Binary Search only works if the list is sorted.**
