#!/usr/bin/env python3
"""Binary search implementation variations"""


def binary_search_basic(nums: list[int], target: int) -> int:
    """Very basic/common implementation of binary search."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
    return -1


def binary_search_fave(nums: list[int], target: int) -> int:
    """My personal favorite implementation of binary search."""
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1


def binary_search_alt_fake(nums: list[int], target: int) -> int:
    """Alternative implementation (that doesn't actually work). Just to prove a point."""
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m
        else:
            return m
    return -1

