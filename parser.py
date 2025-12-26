def process_command(line, purchase):
    tokens=line.split()
    if len(tokens)==0:
        return None
    command=tokens[0]
    if command=="ADD_ITEM":
        if len(tokens)!=3:
            return "ERROR_INVALID_COMMAND"
        item=tokens[1]
        try:
            quantity=int(tokens[2])
        except ValueError:
            return "ERROR_INVALID_COMMAND"
        if quantity<=0:
            return "ERROR_INVALID_COMMAND"

        return purchase.add_item(item, quantity)
    elif command=="PRINT_BILL":
        if len(tokens)!=1:
            return "ERROR_INVALID_COMMAND"
        return "PRINT"
    else:
        return "ERROR_INVALID_COMMAND"
