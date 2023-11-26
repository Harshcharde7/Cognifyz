def generate_fibonacci_sequence(terms):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(terms):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("\n\t\t\tEnter the number of terms for the Fibonacci sequence: "))
        
        if num_terms <= 0:
            print("\t\t\tPlease enter a positive integer.")
        else:
            result = generate_fibonacci_sequence(num_terms)
            print(f"\t\t\tFibonacci sequence up to {num_terms} terms: {result}")

    except ValueError:
        print("\t\t\tInvalid input. Please enter a valid integer.")
