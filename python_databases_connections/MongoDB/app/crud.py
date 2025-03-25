from app.database import collection

def insert_document(data):
    """Insert a document into the collection."""
    result = collection.insert_one(data)
    return str(result.inserted_id)

def find_document(query):
    """Find a document based on a query."""
    return collection.find_one(query)

def update_document(query, update_data):
    """Update a document in the collection."""
    result = collection.update_one(query, {"$set": update_data})
    return result.modified_count

def delete_document(query):
    """Delete a document from the collection."""
    result = collection.delete_one(query)
    return result.deleted_count

def list_collections():
    """List all collections in the database."""
    return collection.database.list_collection_names()