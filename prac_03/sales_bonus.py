def main():
    sales = float(input("Enter Sales: $"))

    while sales >= 0:
        calculate_bonus(sales)
        sales = float(input("Enter Sales: $"))


def calculate_bonus(sales):
    if sales < 1000:
        print("10% bonus totalling ${:.2f}".format(sales * .1))
    else:
        print("15% bonus totalling ${:.2f}".format(sales * .15))



main()
