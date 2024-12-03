from datetime import datetime
from collections import defaultdict

def analyze_library_records(file_name):
    with open(file_name, 'r') as file:
        records = [line.strip().split(', ') for line in file]

    total_books = len(records)

    unique_borrowers = set(record[0] for record in records)

    durations = []
    borrower_durations = defaultdict(list)
    for record in records:
        borrow_date = datetime.strptime(record[2], '%Y-%m-%d')
        return_date = datetime.strptime(record[3], '%Y-%m-%d')
        duration = (return_date - borrow_date).days
        durations.append(duration)
        borrower_durations[record[0]].append(duration)

    avg_duration = round(sum(durations) / total_books, 2)

    borrower_count = defaultdict(int)
    for record in records:
        borrower_count[record[0]] += 1
    most_books_borrower = max(borrower_count, key=borrower_count.get)
    most_books_count = borrower_count[most_books_borrower]

    with open('borrow_summary.txt', 'w') as summary_file:
        for borrower, durations in borrower_durations.items():
            summary_file.write(
                f"{borrower}: Total Books Borrowed = {len(durations)}, "
                f"Average Duration = {round(sum(durations) / len(durations), 2)} days\n"
            )

    return {
        "Total Books Borrowed": total_books,
        "Unique Borrowers": list(unique_borrowers),
        "Average Borrowing Duration": avg_duration,
        "Borrower with Most Books": (most_books_borrower, most_books_count)
    }

file_name = 'library_records.txt'
results = analyze_library_records(file_name)
for key, value in results.items():
    print(f"{key}: {value}")
