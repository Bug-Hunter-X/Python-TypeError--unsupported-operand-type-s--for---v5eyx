def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, (int, float)):
            if b == 0:
                print("Error: Division by zero")
                return None
            else:
                result = a / b
                return result
        else:
            print("Error: Unsupported operand type(s) for / ")
            return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage with improved error handling
result1 = function_with_uncommon_error(10, 2)
result2 = function_with_uncommon_error(10, 0)
result3 = function_with_uncommon_error(10, 'a')
result4 = function_with_uncommon_error(10, 2.5) #Test with float
print(result1, result2, result3, result4) 