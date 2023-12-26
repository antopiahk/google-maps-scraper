import os
import pandas as pd
import shutil

# Combine all CSV files in a given folder (recursively) into a single file 
def combine_csv_files(input_folder, output_file):
    all_csv_dataframes = []

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):  # Check if the file exists
                    try:
                        # Read each CSV file into a DataFrame and append to the list
                        df = pd.read_csv(file_path)
                        if not df.empty:
                            # print(f'CSV file added to merge: {file_path}')
                            all_csv_dataframes.append(df)
                        else:
                            # If the file is empty, delete its parent folder
                            delete_folder = os.path.dirname(os.path.dirname(file_path))
                            if not 'all' in file_path and delete_folder != 'output':
                                print(f'Deleting folder: {delete_folder}')
                                shutil.rmtree(delete_folder)
                    except pd.errors.EmptyDataError:
                        # If the file is empty, delete its parent folder
                        delete_folder = os.path.dirname(os.path.dirname(file_path))
                        if not 'all' in file_path and delete_folder != 'output':
                            print(f'Deleting folder: {delete_folder}')
                            shutil.rmtree(delete_folder)
                else:
                    print(f'File not found: {file_path}')
    if all_csv_dataframes:
        # Combine all DataFrames into one
        combined_df = pd.concat(all_csv_dataframes, ignore_index=True)
        cleaned_df = combined_df.drop_duplicates()

        print(f"combined: {combined_df.shape[0]} cleaned: {cleaned_df.shape[0]}")

        # Write the combined DataFrame to a new CSV file
        cleaned_df.to_csv(output_file, index=False)
        print(f'Combined CSV saved to: {output_file}')
    else:
        print('No non-empty CSV files found.')


# Split a large CSV file into smaller files
def split_csv_file(file_path, chunk_size):
    '''
        Split a large CSV file into smaller files
        file_path: path to the CSV file
        chunk_size: rows per file
    '''

    # Create a reader object for the large CSV file
    reader = pd.read_csv(file_path, chunksize=chunk_size)

    for i, chunk in enumerate(reader):
        # Each chunk will be a DataFrame
        # Savee it to a CSV file
        chunk.to_csv(f'output/all/csv/merged-all-chunk_{i}.csv', index=False)

if __name__ == '__main__':

    # Specify the input folder and output file
    input_folder = '.'
    output_file = 'output/all/csv/merged-all-1.csv'

    # Call the function to combine CSV files
    combine_csv_files(input_folder, output_file)
