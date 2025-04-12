# Maximum Fibonacci value
MAX_TERM_VALUE = 10000  # 10,000 سے زیادہ نمبر شامل نہیں ہوں گے

def main():
    curr_term = 0
    next_term = 1

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # نمبروں کو ایک لائن میں پرنٹ کریں
        curr_term, next_term = next_term, curr_term + next_term  # Fibonacci logic

if __name__ == "__main__":
    main()
