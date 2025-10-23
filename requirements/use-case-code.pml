@startuml
left to right direction

actor User
actor "Payment Processor"
actor Administrator

rectangle "Sales System" {
    User --> (Create Account)
    User --> (Search for Items)
    User --> (Add Item to Cart)
    User --> (Select Shipping Type)
    User --> (Checkout)


    Administrator --> (Add New Item)
    Administrator --> (Remove Item)
    Administrator --> (View Sale History Report)
    Administrator --> (Export Sales Report to CSV File)
    Administrator --> (Update Item)


    "Payment Processor" --> (Checkout)
    "Payment Processor" --> (Generate Receipt)
    "Payment Processor" --> (Generate Sales Record)
}
@enduml

