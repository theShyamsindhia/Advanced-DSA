import streamlit as st
import pandas as pd
import os

# Define the Contact class to store contact details
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.left = None
        self.right = None

# Define the BST class to manage the binary search tree of contacts
class BST:
    def __init__(self):
        self.root = None

    # Insert a new contact into the BST and save it to an Excel file
    def insert(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        if not self.root:
            self.root = new_contact
        else:
            self._insert(self.root, new_contact)
        self.save_to_excel(name, phone, email)

    # Helper method to insert a new contact into the BST
    def _insert(self, current, new_contact):
        if new_contact.name < current.name:
            if current.left:
                self._insert(current.left, new_contact)
            else:
                current.left = new_contact
        elif new_contact.name > current.name:
            if current.right:
                self._insert(current.right, new_contact)
            else:
                current.right = new_contact
        else:
            st.warning(f"Contact with name {new_contact.name} already exists.")

    # Search for a contact by name
    def search(self, name):
        return self._search(self.root, name)

    # Helper method to search for a contact by name
    def _search(self, current, name):
        if not current:
            return None
        if current.name == name:
            return current
        elif name < current.name:
            return self._search(current.left, name)
        else:
            return self._search(current.right, name)

    # Update an existing contact's phone and/or email
    def update(self, name, phone=None, email=None):
        contact = self.search(name)
        if contact:
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            self.update_in_excel(name, phone, email)
            st.success(f"Contact {name} updated successfully.")
        else:
            st.error(f"Contact with name {name} not found.")

    # Delete a contact by name
    def delete(self, name):
        self.root = self._delete(self.root, name)
        self.delete_from_excel(name)

    # Helper method to delete a contact by name
    def _delete(self, current, name):
        if not current:
            return current
        if name < current.name:
            current.left = self._delete(current.left, name)
        elif name > current.name:
            current.right = self._delete(current.right, name)
        else:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left

            temp = self._min_value_node(current.right)
            current.name = temp.name
            current.phone = temp.phone
            current.email = temp.email
            current.right = self._delete(current.right, temp.name)
        return current

    # Helper method to find the node with the minimum value
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Display all contacts in the BST
    def display(self):
        contacts = []
        self._in_order_traversal(self.root, contacts)
        return contacts

    # Helper method for in-order traversal of the BST
    def _in_order_traversal(self, current, contacts):
        if current:
            self._in_order_traversal(current.left, contacts)
            contacts.append(f"Name: {current.name}, Phone: {current.phone}, Email: {current.email}")
            self._in_order_traversal(current.right, contacts)

    # Save a new contact to an Excel file
    def save_to_excel(self, name, phone, email):
        file_name = "contacts.xlsx"
        new_data = pd.DataFrame([{"Name": name, "Phone": phone, "Email": email}])
        if os.path.exists(file_name):
            df = pd.read_excel(file_name)
            df = pd.concat([df, new_data], ignore_index=True)
        else:
            df = new_data
        df.to_excel(file_name, index=False)

    # Update an existing contact in the Excel file
    def update_in_excel(self, name, phone, email):
        file_name = "contacts.xlsx"
        if os.path.exists(file_name):
            df = pd.read_excel(file_name)
            if name in df["Name"].values:
                idx = df[df["Name"] == name].index[0]
                if phone:
                    df.at[idx, "Phone"] = phone
                if email:
                    df.at[idx, "Email"] = email
                df.to_excel(file_name, index=False)

    # Delete a contact from the Excel file
    def delete_from_excel(self, name):
        file_name = "contacts.xlsx"
        if os.path.exists(file_name):
            df = pd.read_excel(file_name)
            df = df[df["Name"] != name]
            df.to_excel(file_name, index=False)

# Streamlit UI
if __name__ == "__main__":
    bst = BST()

    st.title("Contact Management Application")

    menu = ["Add Contact", "Search Contact", "Update Contact", "Delete Contact", "Display Contacts"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Contact":
        st.subheader("Add Contact")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        if st.button("Add"):
            if name and phone and email:
                bst.insert(name, phone, email)
                st.success(f"Contact {name} added successfully.")
            else:
                st.error("Please fill all fields.")

    elif choice == "Search Contact":
        st.subheader("Search Contact")
        name = st.text_input("Enter name to search")
        if st.button("Search"):
            contact = bst.search(name)
            if contact:
                st.write(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            else:
                st.error("Contact not found.")

    elif choice == "Update Contact":
        st.subheader("Update Contact")
        name = st.text_input("Enter name to update")
        phone = st.text_input("New Phone (optional)")
        email = st.text_input("New Email (optional)")
        if st.button("Update"):
            if name:
                bst.update(name, phone, email)
            else:
                st.error("Please enter a name to update.")

    elif choice == "Delete Contact":
        st.subheader("Delete Contact")
        name = st.text_input("Enter name to delete")
        if st.button("Delete"):
            if name:
                bst.delete(name)
                st.success(f"Contact {name} deleted successfully.")
            else:
                st.error("Please enter a name to delete.")

    elif choice == "Display Contacts":
        st.subheader("All Contacts")
        file_name = "contacts.xlsx"
        if os.path.exists(file_name):
            df = pd.read_excel(file_name)
        if not df.empty:
            st.dataframe(df)
        else:
            st.info("No contacts to display.")
    else:
        st.info("No contacts to display.")

