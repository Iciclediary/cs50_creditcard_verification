def main():
    credit_card_number = input("Enter a credit card number: ").strip()
    if check_input_validity(credit_card_number):
        card_type = check_card_type(credit_card_number)
        if card_type and luhns_algorithm(credit_card_number):
            print(f"{card_type}")
        else:
            print("INVALID")
    else:
        print("please enter a valid credit card number")


def check_input_validity(number):
    return number.isdigit() and 13 <= len(number) <= 16


def check_card_type(number):
    AMERICAN_EXPRESS_START = ["34", "37"]
    VISA_START = "4"
    MASTERCARD_START = ["51", "52", "53", "54", "55"]

    if 13 <= len(number) >= 16 and number[0] == VISA_START:
        return "VISA"
    elif len(number) == 16 and number[:2] in MASTERCARD_START:
        return "MASTERCARD"
    elif len(number) == 15 and number[:2] in AMERICAN_EXPRESS_START:
        return "AMEX"


def luhns_algorithm(number):
    number_list = [int(i) for i in number]
    reversed_number_list = number_list[::-1]
    reversed_number_list[1::2] = [i*2 for i in reversed_number_list[1::2]]
    reversed_number_list = [i-9 if i > 9 else i for i in reversed_number_list]
    return sum(reversed_number_list) % 10 == 0


while True:
    if __name__ == "__main__":
        main()
