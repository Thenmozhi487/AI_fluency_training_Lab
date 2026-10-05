def read_private_data():
    with open("private_data.txt", "r") as file:
        return file.read()


data = read_private_data()

print("=== Rule-Based Workflow ===")

question = input("Enter your question: ")

if "CS101" in question and "10%" in question:
    fee = 12000
    discount = fee * 0.10
    final_fee = fee - discount

    print("\nWorkflow Answer:")
    print(f"CS101 fee = ₹{fee}")
    print(f"After 10% merit scholarship = ₹{final_fee:.0f}")

elif "AI202" in question:
    print("\nWorkflow Answer:")
    print("AI202 fee = ₹18000")

elif "DS303" in question:
    print("\nWorkflow Answer:")
    print("DS303 fee = ₹15000")

else:
    print("\nWorkflow Answer:")
    print("Sorry, this rule-based workflow cannot handle that question.")