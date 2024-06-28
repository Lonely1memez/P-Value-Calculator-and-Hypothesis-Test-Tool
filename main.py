#Name: Antonio Mora
#Date: 6/27/2024
#Description: This program will ask the user for a number and then print the multiplication table for that number
import scipy.stats as stats

def calculate_p_value(sample_size, test_statistic):
    # Degrees of freedom
    df = sample_size - 1

    # Calculate the p-value
    p_value = 2 * (1 - stats.t.cdf(abs(test_statistic), df))

    return p_value

def main():
    # Input from the user
    sample_size = int(input("Enter the sample size (n): "))
    test_statistic = float(input("Enter the test statistic (T): "))
    alpha = float(input("Enter the significance level (alpha): "))

    # Calculate the p-value
    p_value = calculate_p_value(sample_size, test_statistic)

    # Print the p-value
    print(f"The p-value is: {p_value}")

    # Determine if the null hypothesis is rejected
    if p_value < alpha:
        print("Reject the null hypothesis.")
    else:
        print("Do not reject the null hypothesis.")

if __name__ == "__main__":
    main()