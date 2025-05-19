def read_cv(file_path):
    """Reads the CV file and returns its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def validate_file_format(file_path):
    """Validates the file format of the CV."""
    valid_extensions = ['.pdf', '.docx', '.txt']
    if any(file_path.endswith(ext) for ext in valid_extensions):
        return True
    return False

def save_uploaded_cv(file, destination):
    """Saves the uploaded CV file to the specified destination."""
    with open(destination, 'wb') as dest_file:
        dest_file.write(file.read())