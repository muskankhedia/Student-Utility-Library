def calculate_percentage(total_marks, obtained_marks):
    if total_marks <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if obtained_marks < 0:
        raise ValueError("Obtained marks cannot be negative.")

    percentage = (obtained_marks / total_marks) * 100
    return round(percentage, 2)


if __name__ == "__main__":
    result = calculate_percentage(500, 420)
    print("Percentage:", result)