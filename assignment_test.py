from random import uniform

# Company name/info
company_name = "PIXELL RIVER FINANCIAL"
program_name = "ATM Simulator"

# User Info
user_current_balance = uniform(-1_000, 10_000)

# ATM Interface 
transaction_options = ['D', 'W', 'Q']
interface_width = 40
interface_balance = f"Your current balance is: ${user_current_balance:,.2f}"
interface_deposit = f"Deposit: {transaction_options[0]}"
interface_withdraw = f"Withdraw: {transaction_options[1]}"
interface_quit = f"To Quit: {transaction_options[2]}"
asterisk_fill = '*' * interface_width
invalid_selection = ["INVALID SELECTION", "INSUFFICIENT FUNDS"]
quit_selection = "No action is required at this time."

# ATM Output 
print(f"{asterisk_fill}\n"
      f"{company_name.center(interface_width)}\n"
      f"{program_name.center(interface_width)}\n"
      f"{interface_balance.center(interface_width)}\n\n"
      f"{interface_deposit.center(interface_width)}\n"
      f"{interface_withdraw.center(interface_width)}\n"
      f"{interface_quit.center(interface_width)}\n"
      f"{asterisk_fill}")