# Contact Management Application

This application is a Contact Management System built using Python and Streamlit. It leverages a Binary Search Tree (BST) to store, retrieve, update, and delete contacts efficiently. Additionally, it stores all contact data in an Excel file for persistence across sessions.

---

## Features

### Core Functionalities
1. **Add Contact**: Insert a new contact with a name, phone number, and email address. The contact is stored in both the BST and an Excel file (`contacts.xlsx`).
2. **Search Contact**: Retrieve details of a contact by name using the BST search mechanism.
3. **Update Contact**: Modify the phone number or email address of an existing contact.
4. **Delete Contact**: Remove a contact from both the BST and the Excel file.
5. **Display Contacts**: Display all contacts stored in the BST in alphabetical order.

### Additional Features
- **Persistent Storage**: Contacts are saved in an Excel file (`contacts.xlsx`), ensuring data persistence across sessions.
- **Interactive UI**: Built with Streamlit, the application provides a user-friendly interface for managing contacts.

---

## Technologies Used
- **Python**
- **Streamlit**: For building the interactive user interface.
- **Pandas**: For handling and storing contact data in an Excel file.
- **OpenPyXL**: Backend library used by Pandas for Excel file operations.

---

## Installation and Setup

### Prerequisites
1. Install Python (version 3.7 or higher).
2. Install required libraries using pip:
   ```bash
   pip install streamlit pandas openpyxl
   ```

### Running the Application
1. Save the script as `app.py`.
2. Run the following command in your terminal:
   ```bash
   streamlit run app.py
   ```
3. Open the displayed local URL in your web browser to use the application.

---

## File Structure
- **`app.py`**: Main application script containing the implementation of the BST and the Streamlit UI.
- **`contacts.xlsx`**: Excel file used to persistently store contact data.

---

## Usage Instructions

1. **Add Contact**
   - Navigate to the "Add Contact" section in the sidebar.
   - Fill in the contact's name, phone number, and email address.
   - Click the "Add" button to save the contact.

2. **Search Contact**
   - Navigate to the "Search Contact" section in the sidebar.
   - Enter the name of the contact you want to search for.
   - Click the "Search" button to display the contact details.

3. **Update Contact**
   - Navigate to the "Update Contact" section in the sidebar.
   - Enter the name of the contact to update and provide the new phone number and/or email address.
   - Click the "Update" button to save the changes.

4. **Delete Contact**
   - Navigate to the "Delete Contact" section in the sidebar.
   - Enter the name of the contact to delete.
   - Click the "Delete" button to remove the contact.

5. **Display Contacts**
   - Navigate to the "Display Contacts" section in the sidebar.
   - View all contacts in alphabetical order.

---

## Example Workflow
1. Add the following contacts:
   - Name: Alice, Phone: 1234567890, Email: alice@example.com
   - Name: Bob, Phone: 2345678901, Email: bob@example.com
   - Name: Charlie, Phone: 3456789012, Email: charlie@example.com
2. Search for "Bob" to view his details.
3. Update Charlie's phone number to `9876543210`.
4. Delete Alice's contact.
5. Display the updated list of contacts.

---

## Known Issues and Future Enhancements

### Known Issues
- Contacts with duplicate names are not allowed.
- Displayed contacts only include those stored in the BST (Excel file is not directly displayed).

### Future Enhancements
- Enable partial search by name or other fields.
- Import contacts from an external file to populate the BST.
- Export all contacts to an external file (e.g., CSV or Excel).
- Add error handling for invalid inputs and file operations.

---

## License
This project is open-source and available under the MIT License.

---

## Contributions
Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

---

## Author
Developed by Shyam Rao Sindhia

