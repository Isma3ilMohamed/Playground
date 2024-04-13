## Fixed-Size vs. Variable-Size Sliding Window

| Aspect                | Fixed-Size Sliding Window                                                                                        | Variable-Size Sliding Window                                                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Window Size**       | Constant size. The window size does not change.                                                                  | Variable size. The window expands and contracts based on certain conditions.                                                                       |
| **Use Case**          | Used when the problem specifies a fixed length or size for the subarray or substring to be considered.           | Used when the problem requires finding a subarray or substring that meets a condition, without specifying a fixed size.                            |
| **Examples**          | - Maximum sum subarray of size K<br>- Average of all subarrays of size K<br>- Maximum product subarray of size K | - Longest substring without repeating characters<br>- Smallest subarray with a given sum<br>- Longest substring with at most K distinct characters |
| **Adjustment Method** | The window slides one element at a time, maintaining the same size.                                              | The start and end of the window adjust dynamically to satisfy a condition (like a sum or number of distinct elements).                             |
| **Decision Criteria** | Use when the problem explicitly states a size or when you need to evaluate every fixed-size segment.             | Use when the goal is to meet a condition (e.g., sum, number of distinct elements) and the optimal size is unknown.                                 |

### Examples of Variable-Size Sliding Window

1. **Longest Substring Without Repeating Characters**
    - Find the length of the longest substring without repeating characters in a given string.
    - The window expands when a new, non-repeating character is encountered and contracts when a character repeats.

2. **Smallest Subarray with a Given Sum**
    - Find the minimal length of a contiguous subarray of which the sum is greater than or equal to a given integer.
    - The window expands by adding elements to the right to increase the sum and contracts from the left to minimize the
      size once the sum exceeds the target.

3. **Longest Substring with At Most K Distinct Characters**
    - Find the length of the longest substring that contains no more than K distinct characters.
    - The window expands to include new characters as long as the distinct character count does not exceed K and
      contracts when the condition is violated to try and drop a character.

### How to Choose the Right Technique

1. **Problem Specification**:
    - **Fixed-Size**: If the problem specifies a fixed length/size for the segment (e.g., "subarray of size K"), use a
      fixed-size sliding window.
    - **Variable-Size**: If the problem involves conditions like a maximum or minimum sum, or a maximum number of
      distinct characters without specifying segment size, a variable-size window is likely more appropriate.

2. **Goal of the Problem**:
    - Use a **fixed-size** window when you need to calculate something for every segment of a specific size (e.g.,
      maximum, minimum, average).
    - Use a **variable-size** window when you need to find a segment that meets certain conditions (like sum or number
      of distinct elements) and the optimal segment size is not predetermined.

3. **Nature of the Data**:
    - **Fixed-Size** is straightforward for problems with uniform data where every segment needs evaluation.
    - **Variable-Size** is essential when the solution depends on dynamically changing conditions influenced by the
      data's nature (e.g., sum exceeding a target, character repetitions).

Choosing the right technique depends on understanding the problem's requirements and constraints. By identifying whether
the problem's focus is on analyzing every fixed-size segment or finding segments that meet specific conditions, you can
select the most appropriate sliding window approach.
