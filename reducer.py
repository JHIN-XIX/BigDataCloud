# Step 2: Reducer function
from collections import Counter
def reducer(mapped_data):
    """
    Aggregates the counts for each passenger_id.
    """
    counter = Counter()
    for passenger_id, count in mapped_data:
        counter[passenger_id] += count
    return counter
