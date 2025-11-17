







def can_divide_evenly(input: list, i: int) -> bool:

    if input[i] % 2 == 0:  # Check if the weight at index i is even
        print("YES")
        return True
    
    else:
        print("NO")
        return False
    
if __name__ == "__main__":
    # Example usage:
    input = [8, 3, 2]
    for i in range(len(input)):
        can_divide_evenly(input, i)