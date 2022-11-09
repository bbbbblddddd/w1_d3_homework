def get_name(record_store):
    return record_store["name"]

# THIS LOOPS THROUGH THE DICTIONARY OF RECORD_STORE
def find_record_by_title(title, record_store):
    for record in record_store['records']:
        if record["title"] == title:
            return record
    return None