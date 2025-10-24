# Requirements

___

## Version 1: Must Have Requirements

### T4E-1: New Account Management

* **T4S-1: Register a New User**
    * **Priority:** Must Have  
    * **Effort:** 1 Day  
    * **Type:** Functional  
    * **Description:** Users must be able to create an account and log in if the password/sign in requirements are met (Unique username and 6+ character password). Administrators cannot self-register.


* **T4S-2: Log in as a Registered User**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day  
    * **Type:** Functional  
    * **Description:** The user must be able to log in using their chosen username and password. The credentials must match the database and direct the user to the main shopping screen. If credentials do not match, the system must display an error message.  


* **T4S-3: Provide Admin Promotion Process**
    * **Priority:** Must Have
    * **Effort:** 1 Day  
    * **Type:** Functional  
    * **Description:** The system must include a process where an existing administrator can change a registered user's role to an administrator.
---

### T4E-2: Inventory Management and Display

* **T4S-4: Display Available Inventory**
    * **Priority:** Must Have  
    * **Effort:** 1 Day  
    * **Type:** Functional  
    * **Description:** The system must display a list of all unsold items on the main screen, sorted by highest price to lowest price.


* **T4S-5: Display Item Details**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day  
    * **Type:** Functional  
    * **Description:** For each inventory item, the system must display a name, price, brief description, and at least one picture.  


* **T4S-6: Implement Basic Inventory Search**
    * **Priority:** Must Have  
    * **Effort:** 1 Day  
    * **Type:** Functional
    * **Description:** The user must be able to search the inventory by entering desired item into a search tool where the system matches against words in either the item's name or description.


* **T4S-7: Enforce Decimal Price Storage**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day  
    * **Type:** Functional  
    * **Description:** The system must store all item prices in a base-10 decimal/currency format (not floating point) to ensure there are no errors in financial calculations.


* **T4S-8: Format Price Display**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day  
    * **Type:** Functional  
    * **Description:** All displayed prices must be formatted with a dollar sign, commas, and decimal points (e.g., $10,000.00).  


* **T4S-8A: Hide Sold Items from Inventory**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day  
    * **Type:** Functional  
    * **Description:** Once an item has been purchased, it must be removed from the visible inventory and search results so that users cannot see or attempt to purchase out of stock items.  


---

### T4E-3: Shopping Cart Functionality

* **T4S-9: Add Item to Cart**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day  
    * **Type:** Functional  
    * **Description:** The system must provide a button on each available inventory item to allow the user to add the unique item to the shopping cart.  


* **T4S-10: Initiate Checkout**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day  
    * **Type:** Functional  
    * **Description:** The system must provide a "Checkout" button and must prevent the user from clicking it if the shopping cart is empty. 


* **T4S-11: Display Shopping Cart Contents**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day  
    * **Type:** Functional  
    * **Description:** After initiating checkout, the system must display a list of all items currently in the cart and a subtotal cost in U.S. dollars. 


* **T4S-12: Remove Item from Cart**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day  
    * **Type:** Functional  
    * **Description:** The user must be able to remove individual items from the shopping cart on the cart page.
  

* **T4S-13: Return to Main on Empty Cart**
    * **Priority:** Must Have
    * **Effort:** 0.25 Day  
    * **Type:** Functional 
    * **Description:** If the user removes all items from the cart, the system must automatically return to the main inventory screen.  


---

### T4E-4: Checkout and Sale Completion

* **T4S-14: Initiate Payment**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day  
    * **Type:** Functional  
    * **Description:** The system must provide a "Pay Now" button on the shopping cart page to proceed to the payment details section.  
    

* **T4S-15: Collect Payment/Shipping Details**
    * **Priority:** Must Have  
    * **Effort:** 2 Days  
    * **Type:** Functional  
    * **Description:** The system must require the user to input their shipping address, credit card number (including expiration month/year and CVV), phone number, and select a shipping speed. All fields are required and will result in an error if they are not met.  
    

* **T4S-16: Calculate Order Totals**
    * **Priority:** Must Have  
    * **Effort:** 1 Day
    * **Type:** Functional  
    * **Description:** The system must calculate and display the subtotal, Tax (6% of subtotal), shipping cost, and the grand total.
    

* **T4S-17: Display Order Confirmation**
    * **Priority:** Must Have  
    * **Effort:** 1 Day
    * **Type:** Functional  
    * **Description:** The system must display a confirm order page showing item names, prices, and the detailed breakdown of all calculated totals for final review.
    

* **T4S-18: Record Completed Sale**
    * **Priority:** Must Have  
    * **Effort:** 2 Days  
    * **Type:** Functional  
    * **Description:** Upon clicking "Complete Order", the system must create a permanent sales record, link the items to the sales inventory item table, and remove the purchased items from the available inventory.
    

* **T4S-19: Display Receipt**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day
    * **Type:** Functional  
    * **Description:** The system must display a receipt that includes all details from the confirm order page, plus the last four digits of the credit card and the shipping address.  
    

* **T4S-20: Handle Emailed Receipt**
    * **Priority:** Must Have  
    * **Effort:** 0.5 Day
    * **Type:** Functional
    * **Description:** After the sales completion, the system must display the receipt in the browser for the user’s records.
    

* **T4S-21: Prevent Repeated Checkout on Completion**
    * **Priority:** Must Have
    * **Effort:** 0.25 Day
    * **Type:** Functional  
    * **Description:** After the user completes an order, the user cannot return to the previous checkout or old cart pages. The user must be directed back to the main inventory screen.  
    

* **T4S-22: Define Overnight Shipping Cost**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day
    * **Type:** Data  
    * **Description:** The cost of overnight shipping must be defined as $29.00 for order calculations.


* **T4S-23: Define 3-Day Shipping Cost**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day
    * **Type:** Data  
    * **Description:** The cost of 3-Day shipping must be defined as $19.00 for order calculations.  


* **T4S-24: Define Ground Shipping Cost**
    * **Priority:** Must Have  
    * **Effort:** 0.25 Day  
    * **Type:** Data
    * **Description:** The cost of ground shipping must be defined as $0.00 for order calculations.  


---

### T4E-5: Administrator Actions

* **T4S-25: Run Sales History Report**
    * **Priority:** Must Have  
    * **Effort:** 1 Day  
    * **Type:** Functional
    * **Description:** The administrator must be able to run a report that displays a record of items purchased and the user who purchased it.


* **T4S-26: Admin Inventory Creation**
    * **Priority:** Must Have
    * **Effort:** 2 Day
    * **Type:** Functional  
    * **Description:** The administrator must be able to add new items into the system's inventory.


* **T4S-27: Enforce Admin Inventory Rule**
    * **Priority:** Must Have 
    * **Effort:** 0.25 Day  
    * **Type:** Non-Functional  
    * **Description:** The system must ensure that only an administrator has permission to create, update, and remove inventory items depending on if the item is in stock.


---

## Version 2: Future Improvements

### T4E-6: Inventory & Admin Enhancements

* **T4S-28: Add Multiple Item Images**
    * **Priority:** Needs to Have  
    * **Effort:** 2 Days
    * **Type:** Functional  
    * **Description:** The system must allow for inventory items to be associated with and display multiple related images.
    

* **T4S-29: Implement CSV Sales Export**
    * **Priority:** Needs to Have  
    * **Effort:** 1 Days  
    * **Type:** Functional  
    * **Description:** The administrator must be able to export the sales report data to a CSV file for external data analysis.


* **T4S-30: Implement UI for Inventory Creation**
    * **Priority:** Wants to Have  
    * **Effort:** 3 Days  
    * **Type:** Functional  
    * **Description:** The administrator must be able to add new inventory items through a dedicated user interface page.


* **T4S-31: Link Receipt from Sales Report**
    * **Priority:** Wants to Have  
    * **Effort:** 1 Day  
    * **Type:** Functional  
    * **Description:** The administrator must be able to click on a sold item within the sales report to view the corresponding sale receipt.  


---



