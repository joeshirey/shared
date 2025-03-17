from google.cloud import firestore

def add_document(db, collection_name, document_id, data):
    """
    Adds a new document to the specified collection with the given ID and data.

    Args:
        collection_name: The name of the Firestore collection.
        document_id: The ID for the new document.
        data: A dictionary containing the data to be stored in the document.
    """
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.set(data)

def get_document(db, collection_name, document_id):
    """
    Retrieves a document from the specified collection with the given ID.

    Args:
        collection_name: The name of the Firestore collection.
        document_id: The ID of the document to retrieve.

    Returns:
        A dictionary containing the document data, or None if the document doesn't exist.
    """
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def update_document(db, collection_name, document_id, data):
    """
    Updates an existing document in the specified collection with the given ID and data.

    Args:
        collection_name: The name of the Firestore collection.
        document_id: The ID of the document to update.
        data: A dictionary containing the fields to update and their new values.
    """
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.update(data)

def delete_document(db, collection_name, document_id):
    """
    Deletes a document from the specified collection with the given ID.

    Args:
        collection_name: The name of the Firestore collection.
        document_id: The ID of the document to delete.
    """
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.delete()

def get_db(project_name, db_name):
    return firestore.Client(project=project_name, database=db_name)

def main(project_name, db_name):
    return firestore.Client(project=project_name, database=db_name)
