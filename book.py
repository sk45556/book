import streamlit as st

# Admin Credentials
admin_username = "admin"
admin_password = "1234"

# Initialize Session State
if "book_ids" not in st.session_state:
    st.session_state.book_ids = [1, 2, 3, 4, 5]
    st.session_state.titles = ["Python Basics", "AI & ML", "Data Science", "Web Development", "Cyber Security"]
    st.session_state.stocks = [10, 5, 8, 6, 4]
    st.session_state.prices = [250, 400, 300, 350, 500]

# Shortcuts
book_ids = st.session_state.book_ids
titles = st.session_state.titles
stocks = st.session_state.stocks
prices = st.session_state.prices

# App UI
st.title("📚 Python Book Store")
menu = st.sidebar.selectbox("Menu", ["Show All Books", "Buy a Book", "Add New Book (Admin Only)", "Exit"])

# Option 1: Show All Books
if menu == "Show All Books":
    st.subheader("📖 All Available Books")
    st.write("### ID | Title | Stock | Price (Rs.)")
    for i in range(len(book_ids)):
        st.write(f"{book_ids[i]} | {titles[i]} | {stocks[i]} | Rs.{prices[i]}")

# Option 2: Buy a Book
elif menu == "Buy a Book":
    st.subheader("🛒 Buy a Book")
    st.write("### Available Books")
    for i in range(len(book_ids)):
        st.write(f"{book_ids[i]}. {titles[i]} ({stocks[i]} in stock) - Rs.{prices[i]}")
    
    book_id = st.number_input("Enter Book ID to buy", min_value=1, max_value=max(book_ids), step=1)
    if book_id in book_ids:
        index = book_ids.index(book_id)
        if stocks[index] > 0:
            name = st.text_input("Enter your name")
            if name:
                confirm = st.radio(f"Do you want to buy '{titles[index]}' for Rs.{prices[index]}?", ("Yes", "No"))
                if confirm == "Yes":
                    st.session_state.stocks[index] -= 1  # Reduce stock
                    st.success("--- Bill Generated ---")
                    st.write(f"**Customer:** {name}")
                    st.write(f"**Book:** {titles[index]}")
                    st.write(f"**Amount:** Rs.{prices[index]}")
                    st.success("Thank you for your purchase!")
                else:
                    st.warning("Purchase cancelled.")
        else:
            st.error("Sorry, this book is out of stock.")
    else:
        st.error("Invalid Book ID.")

# Option 3: Add New Book (Admin Only)
elif menu == "Add New Book (Admin Only)":
    st.subheader("🔐 Add New Book (Admin Only)")
    username = st.text_input("Enter admin username")
    password = st.text_input("Enter admin password", type="password")
    if username == admin_username and password == admin_password:
        new_title = st.text_input("Enter new book title")
        new_stock = st.number_input("Enter stock quantity", min_value=1, step=1)
        new_price = st.number_input("Enter price (Rs.)", min_value=1, step=1)
        if new_title and new_stock and new_price:
            if st.button("Add Book"):
                new_id = max(book_ids) + 1
                st.session_state.book_ids.append(new_id)
                st.session_state.titles.append(new_title)
                st.session_state.stocks.append(int(new_stock))
                st.session_state.prices.append(int(new_price))
                st.success(f"Book '{new_title}' added successfully.")
    elif username or password:
        st.error("Invalid admin credentials.")

# Option 4: Exit
elif menu == "Exit":
    st.subheader("👋 Exit")
    st.info("Thank you for visiting the Python Book Store!")
