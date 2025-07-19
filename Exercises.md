# Number System
    - 

# Python Expressions and Functions:
    - Calculate Interest
## Calculate Hypotense
    
    ### 🧠 Topic: **Calculate Hypotenuse**

    #### 📘 Understanding the Terms (in simple language):

    When you have a right-angled triangle (a triangle where one of the angles is exactly 90 degrees), the longest side of the triangle is called the **hypotenuse**. It’s the side that is **opposite the right angle**.

    The other two sides (the ones that make the right angle) are usually called the **base** and the **height** (or **perpendicular**).

    To calculate the length of the hypotenuse, we use something called the **Pythagorean Theorem**.

    The formula is:

    ```
    hypotenuse² = base² + height²
    ```

    To find the hypotenuse, we need to take the square root of the sum of the squares of the base and height:

    ```
    hypotenuse = √(base² + height²)
    ```

    #### 🔧 Task:

    Write a function named `calculate_hypotenuse` that takes two arguments:

    * `base`: the length of the base (a number)
    * `height`: the length of the height/perpendicular side (a number)

    It should return the length of the hypotenuse (a number).

    Use the formula:

    ```
    hypotenuse = (base² + height²) ** 0.5
    ```

    #### 💡 Examples:

    ```python
    Input: calculate_hypotenuse(3, 4)
    Output: 5.0
    ```

    Why?
    Because √(3² + 4²) = √(9 + 16) = √25 = 5.0

    ---

    ```python
    Input: calculate_hypotenuse(5, 12)
    Output: 13.0
    ```

    Why?
    Because √(25 + 144) = √169 = 13.0

    ---

    ```python
    Input: calculate_hypotenuse(0, 0)
    Output: 0.0
    ```

## Find Distance 2D
    **Topic:** *Find Distance in 2D*

    ### 🧠 Explanation:

    In everyday life, when we move from one place to another, we cover a certain *distance*. In math, especially in geometry, we often want to calculate the distance between two points on a flat surface (called a 2D plane).

    Each point on this plane can be represented by two numbers:

    * the **x-coordinate** (horizontal position)
    * the **y-coordinate** (vertical position)

    Come up with the formula to calculate the distance between two points $(x1, y1)$ and $(x2, y2)$ based on the **Pythagorean Theorem**, just like finding the hypotenuse of a right triangle.

    ---

    ### ✍️ Exercise:

    Write a function `find_distance_2d(x1, y1, x2, y2)` that returns the distance between the two points. Use the formula mentioned above. You can use the `math.sqrt` function to calculate the square root.

    ---

    ### 💡 Examples:

    ```python
    find_distance_2d(0, 0, 3, 4)     # Output: 5.0
    find_distance_2d(1, 2, 4, 6)     # Output: 5.0
    ```

## Find Distance 3D

    **Topic:** *Find Distance in 3D*

    ---

    ### 🧠 **Explanation:**

    In everyday life, we often measure the distance between two points—like how far your house is from school. In **3D space**, we do the same, but we also consider height or depth in addition to length and width.

    A point in 3D space is defined using three coordinates:

    * `x` (horizontal)
    * `y` (vertical)
    * `z` (depth)

    To calculate the **distance between two points** in 3D, say:

    * Point A: `(x1, y1, z1)`
    * Point B: `(x2, y2, z2)`

    Come up with 3D distance formula using the Pythagorean theorem into three dimensions.

    ---

    ### 🧪 **Exercise:**

    Write a function called `calculate_distance_3d(x1, y1, z1, x2, y2, z2)` that returns the distance between two 3D points.

    * The function should return the result as a float.
    * You can use the built-in `math.sqrt()` function to calculate the square root.

    ---

    ### ✅ **Examples:**

    ```python
    calculate_distance_3d(0, 0, 0, 1, 1, 1)  # Output: 1.7320508075688772
    calculate_distance_3d(2, 3, 5, 2, 3, 5)  # Output: 0.0
    calculate_distance_3d(1, 2, 3, 4, 6, 9)  # Output: 7.810249675906654
    ```


## Find Manhatten Distance

    ### **Topic:** *Find Manhattan Distance*

    ---

    ### **Explanation:**

    When you want to measure the distance between two points on a grid (like in a city with square blocks), you don’t move diagonally. Instead, you move only **horizontally** and **vertically**, like a taxi driving along streets and avenues. This kind of distance is called the **Manhattan Distance**.

    The formula to calculate the Manhattan Distance between two points $(x1, y1)$ and $(x2, y2)$ is:

    $$
    \text{Manhattan Distance} = |x1 - x2| + |y1 - y2|
    $$

    Here, $|a|$ means the absolute value of $a$ — in other words, how far the number is from zero.

    For example:

    * From (2, 3) to (5, 1):
    $|2 - 5| = 3$ and $|3 - 1| = 2$, so distance = $3 + 2 = 5$

    ---

    ### **Exercise:**

    Write a function `manhattan_distance(x1, y1, x2, y2)` that takes the coordinates of two points and returns their Manhattan Distance.

    ---

    ### **Example:**

    ```python
    manhattan_distance(2, 3, 5, 1)  # Output: 5
    manhattan_distance(0, 0, 0, 0)  # Output: 0
    manhattan_distance(-1, -1, 1, 1)  # Output: 4
    ```

    
## Write a function to return value of y given x on a straight line in 2D. It should take three arguments: m, c, x. 

    **Topic:** *Predict Y on a Straight Line (2D)*

    ---

    ### **Simple Explanation:**

    In math, a straight line in 2D is usually written in this form:

    ```
    y = m * x + c
    ```

    Here’s what the terms mean:

    * `x` is the input (like a point on the horizontal axis).
    * `y` is the output (like a point on the vertical axis).
    * `m` is the *slope* of the line, which tells us how steep the line is.
    * `c` is the *intercept*, or where the line crosses the y-axis.

    For example:
    If `m = 2`, `c = 3`, and `x = 4`, then:

    ```
    y = 2 * 4 + 3 = 8 + 3 = 11
    ```

    So, the value of `y` is `11`.

    ---

    ### **Exercise:**

    Write a function `predict(m, c, x)` that returns the value of `y` based on the formula:

    ```
    y = m * x + c
    ```

    #### **Arguments:**

    * `m` – slope of the line (a number)
    * `c` – y-intercept of the line (a number)
    * `x` – the x-coordinate (a number)

    #### **Return:**

    * The value of `y` calculated from the formula `y = m * x + c`

    ---

    ### **Example Usage:**

    ```python
    predict(2, 3, 4)     # Output: 11
    predict(-1, 5, 2)    # Output: 3
    ```


## Given two points, write a function fit() to learn slope and intercept of the line going through them

    ### **Topic:** *Learn Line Equation from Two Points*

    ### **Explanation:**

    A straight line in a 2D plane can be described by the equation:

    $$
    y = mx + c
    $$

    Where:

    * `m` is the **slope** of the line.
    * `c` is the **intercept** — the value of `y` when `x = 0`.

    If you're given **two points** on the line, say `(x1, y1)` and `(x2, y2)`, you can calculate the **slope** `m` like this:

    $$
    m = \frac{y2 - y1}{x2 - x1}
    $$

    Once you have the slope, you can use one of the points (say `(x1, y1)`) to calculate the intercept `c` using:

    $$
    c = y1 - m \times x1
    $$

    For example, if your two points are (1, 2) and (3, 6):

    * Slope: `(6 - 2)/(3 - 1) = 4/2 = 2`
    * Intercept: `2 - (2 × 1) = 0`
    * So, the equation of the line is: `y = 2x + 0`

    ---

    ### **Exercise:**

    Write a function `fit(x1, y1, x2, y2)` that returns a tuple `(m, c)` representing the slope and intercept of the line passing through the two points `(x1, y1)` and `(x2, y2)`.

    ---

    ### **Function Signature:**

    ```python
    def fit(x1, y1, x2, y2):
        # Your code here
    ```

    ---

    ### **Example:**

    ```python
    fit(1, 2, 3, 6)       # Output: (2.0, 0.0)
    fit(0, 5, 2, 9)       # Output: (2.0, 5.0)
    ```

    > 💡 **Hint:** Make sure `x1` is not equal to `x2`, otherwise the slope would be undefined (vertical line). You may handle this case as you see fit.


# Chapter - if - else
## Huber Distance
    ---

    ### **Topic:** *Compute Huber Distance*

    ---

    ### **Explanation:**

    In machine learning and statistics, **Huber distance** is a special way of measuring the error between two values — typically the *actual* and the *predicted*. It’s designed to be *less sensitive to outliers* than the usual squared error.

    The idea is simple:

    * If the difference between the actual and predicted value is **small**, we treat the error like **squared error**.
    * If the difference is **large**, we treat it more like **absolute error**.

    The point where we switch between these two behaviors is decided by a value called **delta**.

    To compute the Huber distance:

    1. First, find the **error** by subtracting the predicted value from the actual value.
    2. If the absolute value of the error is **less than or equal to delta**, use the squared error formula.
    3. Otherwise, use a modified absolute error formula that uses delta.

    ---

    ### **Exercise:**

    Write a function named `compute_huber_distance(actual, predicted, delta)` that:

    * Takes three arguments:

    * `actual`: the true value (a number)
    * `predicted`: the predicted value (a number)
    * `delta`: the threshold that decides when to switch error formulas
    * Returns the Huber distance between the actual and predicted value using the rules described above.

    ---

    ### **Example Usage:**

    ```python
    compute_huber_distance(10, 8, 1.5)   # Output: 2.125  
    compute_huber_distance(10, 9.5, 1.5) # Output: 0.125  
    compute_huber_distance(5, 5, 1)      # Output: 0.0  
    ```

## Check if a point P is closer to point A or point B in 3D

    - Is point on line?
    - Are lines overlapping or touching
    - Is a point inside a rectangle?
    - Are rectangles intersecting?

# If - Else - Recursion:
    - Factorial
    - Multiplication using recursion
    - Compute Sqrt
    - Compute CubeRoot
    - Compute nth Root
    - Compute Log base 10, you can use ** for power.
    - Compute log base n, you can use ** for power.
    - Tower of hanoi

# Loops and Array
    - Compute mean
    - Compute SD
    - 
