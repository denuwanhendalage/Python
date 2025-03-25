import json
from collections import deque
def read_input(file_path):
    with open(file_path, 'r') as file:
        tree = {}
        for line in file:
            line = line.strip().rstrip(',')
            key, value = line.split(':')
            key = key.strip().strip("'")
            value = value.strip().strip("[]").replace("'", "").split(',')
            value = [v.strip() for v in value if v.strip()]
            tree[key] = value
        return tree


def process_inquiries(tree):

    if not tree:
        return []
    queue = deque(['root'])
    processed_order = []
    while queue:
        # Dequeue the next inquiry
        inquiry = queue.popleft()
        # Add the inquiry to the processed order
        processed_order.append(inquiry)
        # Enqueue all follow-up inquiries
        for follow_up in tree.get(inquiry, []):
            queue.append(follow_up)
    return processed_order


input_filename = r'C:\Users\User\Desktop\AI lab 2\input.txt'
try:
    tree = read_input(input_filename)
    order = process_inquiries(tree)
    print(order)
except FileNotFoundError as e:
    print(e)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from {input_filename}: {e}")