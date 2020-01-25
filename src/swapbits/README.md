# Swap bits - Visually
##### Code that takes as input an integer (x) and swaps the bits at indices (i) and (j).

Following code is from EPI 4.2
```
def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        # ith and jth bits differ. We will swap them by flipping their values
        # Select the bits to flip with bit mask. 
        # Since x^1 = 0 when x = 1 and 1 when x = 0 we can perform flip XOR
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x
```
----
# Visual Explanation

##### 1. Most Significant bit and Least Significant bit of the integer (x)
In this problem x = 73. The bits to be swapped are at positions 6 and 1. So i = 6 and j = 1.

![](./MSB_LSB.jpg)

##### 2. ```x >> i```
Move the relevant bit at index i to the LSB position.

![](./RShift_i.jpg)

##### 3. ```(x >> i) & 1```
Perform a bit AND operation to extract the bit value. In this case it gives 1.

![](./RShift_i_and_1.jpg)

##### 4. ```x >> j```
Move the relevant bit at index j to the LSB position.

![](./RShift_j.jpg)


##### 5. ```(x >> j) & 1```
Perform a bit AND operation to extract the bit value. In this case it gives 0.

![](./RShift_j_and_1.jpg)

##### 6. ```(x >> i) & 1 != (x >> j) & 1```

At this point it is clear that the two bits to be swapped are different. Hence they need to be interchanged. If the bits were same we would simply return (x).

![](./NotEqual.jpg)

##### 7. Bit mask ```(i << i) | (i << j)``` 
Use a bit mask to mark the position of the indices.

- ###### 7a. ```(i << i)```  

> Mark the first index position i with 1  

![](./LShift_i.jpg)

- ###### 7b. ```(i << j)``` 

> Mark the second index position j with j 1

![](./LShift_j.jpg)

- ###### 7c. ```(i << i) | (i << j)``` 

> Perform a bitwise OR to mark both the index positions in the bitmask

![](./LShift_i_and_j_OR.jpg)

##### 8. ```x ^= bit_mask``` ( XOR to toggle the bits )

> Toggle the bits to perform the swap operation. Use the bitmask with the index positions marked and perform bitwise XOR. Return the result.

![](/images/Final_BitMask_Swap.jpg?raw=true)

&copy; vidyabhandary.github.io
 




