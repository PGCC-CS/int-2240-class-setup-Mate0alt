def main():
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly pay rate: "))

    # Using a simple if/else to pick the function
    if hours > 40:
        calcPayWithOvertime(hours, rate)
    else:
        calcRegularPay(hours, rate)


def calcPayWithOvertime(hours, rate):
    overtime_hours = hours - 40
    # Combine regular pay (40 * rate) and overtime (extra hours * rate * 1.5)
    gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)

    print(f"Regular hours: 40\nOvertime hours: {overtime_hours}")
    print(f"Gross pay (including overtime): ${gross_pay:,.2f}")


def calcRegularPay(hours, rate):
    print(f"Gross pay: ${hours * rate:,.2f}")


if __name__ == "__main__":
    main()