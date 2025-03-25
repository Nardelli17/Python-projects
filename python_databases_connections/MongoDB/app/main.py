from app.crud import insert_document, find_document, update_document, delete_document, list_collections

def insert_and_show():
    """Insert a document and show the inserted document ID."""
    try:
        user_data = {"name": "Tom", "role": "Data Engineer"}
        user_id = insert_document(user_data)
        print(f"Inserted Document ID: {user_id}")
    except Exception as e:
        print(f"Error inserting document: {e}")

def find_and_show():
    """Find a document by name and display it."""
    try:
        found = find_document({"name": "Tom"})
        if found:
            print(f"Found Document: {found}")
        else:
            print("Document not found.")
    except Exception as e:
        print(f"Error finding document: {e}")

def update_and_show():
    """Update a document and show the updated data."""
    try:
        updated_count = update_document({"name": "Tom"}, {"role": "Senior Data Engineer"})
        if updated_count > 0:
            print(f"Updated Documents: {updated_count}")
        else:
            print("No documents were updated.")
    except Exception as e:
        print(f"Error updating document: {e}")

def find_updated_and_show():
    """Find the updated document and show it."""
    try:
        found_updated = find_document({"name": "Tom"})
        if found_updated:
            print(f"Updated Document: {found_updated}")
        else:
            print("Updated document not found.")
    except Exception as e:
        print(f"Error finding updated document: {e}")

def delete_and_show():
    """Delete a document and display the result."""
    try:
        deleted_count = delete_document({"name": "Tom"})
        if deleted_count > 0:
            print(f"Deleted Documents: {deleted_count}")
        else:
            print("No documents were deleted.")
    except Exception as e:
        print(f"Error deleting document: {e}")

def list_and_show_collections():
    """List all collections in the database."""
    try:
        collections = list_collections()
        print(f"Collections: {collections}")
    except Exception as e:
        print(f"Error listing collections: {e}")

def main():
    """Execute all CRUD operations in sequence."""
    print("\n--- Insert Operation ---")
    insert_and_show()

    print("\n--- Find Operation ---")
    find_and_show()

    print("\n--- Update Operation ---")
    update_and_show()

    print("\n--- Find After Update ---")
    find_updated_and_show()

    print("\n--- Delete Operation ---")
    delete_and_show()

    print("\n--- List Collections ---")
    list_and_show_collections()

if __name__ == "__main__":
    main()

