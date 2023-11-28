#!/usr/bin/env python3
def max_stocks_dp(stocks_and_values, amount):
    n = len(stocks_and_values)
    # Initialize a 2D DP array with all zeros
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

    # Build the table in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, amount + 1):
            stock_count, stock_value = stocks_and_values[i - 1]
            if stock_value <= w:
                # Maximum of including or not including the current stock
                dp[i][w] = max(stock_count + dp[i - 1]
                               [w - stock_value], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][amount]

# Function to process the file inputs and outputs


def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    outputs = []
    i = 0
    while i < len(lines):
        # Check if the line is not empty before trying to convert to an integer
        if lines[i].strip():
            N = int(lines[i].strip())
            stocks_and_values = eval(lines[i + 1].strip())
            amount = int(lines[i + 2].strip())
            result = max_stocks_dp(stocks_and_values, amount)
            outputs.append(result)
            i += 3
        else:
            # skip the empty lines
            i += 1

    with open(output_file, 'w') as file:
        for output in outputs:
            file.write(str(output) + '\n')

    return outputs

# Example usage:
# process_file("Input.txt", "OutputDP.txt")


def main():
    # Process the input file and write results to the output file
    process_file('input.txt', 'outputDP.txt')


if __name__ == '__main__':
    main()
