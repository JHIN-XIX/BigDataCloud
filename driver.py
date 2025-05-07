import csv
from collections import Counter
from mapper import mapper  # Importing the mapper function from mapper.py
from reducer import reducer  # Importing the reducer function from reducer.py

#  Find the passengers with the most flights
def find_top_n_flights(counter, n):
    """
    Finds the top n passengers with the highest number of flights.
    """
    sorted_passengers = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    top_n_passengers = sorted_passengers[:n]
    return top_n_passengers

# Main function As Driver
if __name__ == "__main__":
    # File path to the CSV file
    file_path = r"e:\ACA\reading_second\BigData\coursework\data\AComp_Passenger_data_no_error(1).csv"
    
    # Step 1: Map phase
    mapped_data = mapper(file_path)
    
    # Step 2: Reduce phase
    reduced_data = reducer(mapped_data)
    
    # Step 3: Find the top n passengers with the most flights
    n = 5  # Example: Find the top 3 passengers
    top_n_passengers = find_top_n_flights(reduced_data, n)
    
    # Output the result
    print("Top passengers with the most flights:")
    for passenger, flights in top_n_passengers:
        print(f"{passenger}: {flights} flights")