class DecisionTable:
   def __init__(self, is_username_unique, is_password_valid, is_item_in_stock, is_item_in_cart, is_user_admin,
                is_shipping_info_present, is_payment_provided, is_username_taken,is_account_created,
                is_mode_admin,is_item_added_to_cart,
                is_item_out_of_stock,is_shipping_type_selected,is_sale_completed):

       self.is_username_unique = is_username_unique
       self.is_password_valid = is_password_valid
       self.is_item_in_stock = is_item_in_stock
       self.is_item_in_cart = is_item_in_cart
       self.is_user_admin = is_user_admin
       self.is_shipping_info_present = is_shipping_info_present
       self.is_payment_provided = is_payment_provided
       self.is_username_taken = is_username_taken
       self.is_account_created = is_account_created
       self.is_mode_admin = is_mode_admin
       self.is_item_added_to_cart = is_item_added_to_cart
       self.is_item_out_of_stock = is_item_out_of_stock
       self.is_shipping_type_selected = is_shipping_type_selected
       self.is_sale_completed = is_sale_completed

def detect(question):
    result = input(question + " (y/n) ").strip().lower()
    return result == "y"

while True:
    is_username_unique = detect("Is the username unique?")
    is_password_valid = detect("Is the password valid?")

    if not is_username_unique or not is_password_valid:
        print("Cannot proceed")
        break
    is_item_in_stock = detect("Is the item in stock?")
    is_item_in_cart = detect("Is the item in the cart")
    is_user_admin = detect("Is the user admin?")
    is_shipping_info_present = detect("Is the shipping information present?")
    is_payment_provided = detect("Is the payment provided?")
    is_username_taken = not is_username_unique
    is_account_created = True
    is_mode_admin = is_user_admin
    is_item_added_to_cart = is_item_in_cart
    is_item_out_of_stock = not is_item_in_stock
    is_shipping_type_selected = is_shipping_info_present
    is_sale_completed = True

    R = DecisionTable(is_username_unique, is_password_valid, is_item_in_stock, is_item_in_cart,
       is_user_admin, is_shipping_info_present, is_payment_provided, is_username_taken,is_account_created,is_mode_admin,
       is_item_added_to_cart,is_item_out_of_stock,is_shipping_type_selected,is_sale_completed)
    if (R.is_username_unique and R.is_password_valid
        and R.is_item_in_stock and  R.is_item_in_cart and
        R.is_shipping_info_present and R.is_payment_provided):
        print("All conditions are satisified")

        if R.is_sale_completed:
            print("Sale has been completed")
        else:
            print("Error")
            break
    else:
        print("The sale has not been completed")
        break




