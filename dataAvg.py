import pandas as pd

def average_salary_data(input_csv_file, output_csv_file):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(input_csv_file)
    df = df.dropna(subset=['salary_type', 'ten_percentile_salary', 'ninety_percentile_salary', 'fifty_percentile_salary'], how='all')
    # Group by 'salary_id' and 'salary_type', then calculate the mean for the salary columns
    averaged_df = df.groupby(['id', 'salary_type']).mean().reset_index()

    # Save the averaged data into a new CSV file
    averaged_df.to_csv(output_csv_file, index=False)

# Example usage
average_salary_data('C:/Users/Samue/Downloads/archive/Salaries.csv', 'C:/Users/Samue/Downloads/archive/Salary2.csv')
