import sys
from parser import process_command
from purchase import Purchase
from billing import Billing

def main():
    if len(sys.argv)<2:
        print("Please provide input file path")
        return

    file_path=sys.argv[1]
    pm=Purchase()

    with open(file_path) as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            result=process_command(line, pm)

            if result=="PRINT":
                engine=Billing(pm.cart)
                discount, total=engine.calculate_bill()
                print(f"TOTAL_DISCOUNT {discount:.2f}")
                print(f"TOTAL_AMOUNT_TO_PAY {total:.2f}")
                continue

            if result:
                print(result)

if __name__ == "__main__":
    main()
