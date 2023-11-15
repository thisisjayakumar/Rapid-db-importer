import psycopg2
import concurrent.futures
import csv
import io
import multiprocessing

# Database connection parameters
db_params = {
    "host": "localhost",
    "port": "5432",
    "database": "testdb",
    "user": "postgres",
    "password": '1234'
}

# CSV file path
csv_file_path = "/home/csvfile/updated_csv_1m.csv"

# Table name in the database
table_name = "newtab"

# Number of processes and threads
num_processes = 2
num_threads_per_process = 5

# Function to process and insert a chunk of rows into the database
def process_and_insert_chunk(chunk):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Use COPY command to insert data efficiently
        copy_sql = f"COPY {table_name} FROM stdin WITH CSV HEADER DELIMITER as ','"
        csv_data = io.StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerows(chunk)
        csv_data.seek(0)

        cursor.copy_expert(sql=copy_sql, file=csv_data)
        conn.commit()

        cursor.close()
        conn.close()
        print(f"Inserted {len(chunk)} rows.")

    except Exception as e:
        print(f"Error writing data to the '{table_name}' table: {str(e)}")

# Function to read and process the CSV file in chunks
def read_and_process_csv(start, end):
    chunk_size = 10000
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header
        count = 0
        chunk = []

        for row in csv_reader:
            count += 1
            if not (start < count <= end):  # Adjusted the condition for inclusivity
                continue
            if not row[0] or (not row[4] and int(row[5]) < 550):  # Fix condition for filtering
                continue

            chunk.append(row)

            if len(chunk) == chunk_size:
                process_and_insert_chunk(chunk)
                chunk = []

        if chunk:
            process_and_insert_chunk(chunk)

# Function to run multithreading within each multiprocessing process
def run_multithreading(start, end):
    threading_size = (end - start + 1) // num_threads_per_process
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=num_threads_per_process
    ) as executor:
        futures = []

        for i in range(num_threads_per_process):
            thread_start = start + i * threading_size
            thread_end = start + (i + 1) * threading_size - 1

            if i == num_threads_per_process - 1:
                thread_end = end

            future = executor.submit(read_and_process_csv, thread_start, thread_end)
            futures.append(future)

        concurrent.futures.wait(futures)

def main():
    total_rows = sum(1 for _ in open(csv_file_path))
    process_size = total_rows // num_processes
    processes = []

    for i in range(num_processes):
        start = i * process_size
        end = (i + 1) * process_size
        process = multiprocessing.Process(target=run_multithreading, args=(start, end))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    import time

    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total processing time: {elapsed_time:.2f} seconds")
