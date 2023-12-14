from pymarc import MARCReader

# Specify the path to your downloaded XML file
xml_file_path = 'path/to/your/file.xml'

# Open the XML file for reading
with open(xml_file_path, 'rb') as file:
    # Create a MARCReader instance
    reader = MARCReader(file)

    # Iterate through each MARC record in the file
    for record in reader:
        # Access and print information from the record
        title = record['245']['a'] if '245' in record else 'N/A'
        author = record['100']['a'] if '100' in record else 'N/A'

        print(f"Title: {title}, Author: {author}")


from pymarc import MARCReader

# Specify the path to your downloaded XML file
xml_file_path = 'path/to/your/file.xml'

# Open the XML file for reading
with open(xml_file_path, 'rb') as file:
    # Create a MARCReader instance
    reader = MARCReader(file)

    # Iterate through each MARC record in the file
    for record in reader:
        # Access and print information from the record
        title = record['245']['a'] if '245' in record else 'N/A'
        author = record['100']['a'] if '100' in record else 'N/A'

        print(f"Title: {title}, Author: {author}")


from pymarc import MARCReader

# Specify the path to your downloaded XML file
xml_file_path = 'Downloads/Books.All.2016.part01.xml'

# Open the XML file for reading
with open(xml_file_path, 'rb') as file:
    # Create a MARCReader instance
    reader = MARCReader(file)

    # Iterate through each MARC record in the file
    for record in reader:
        # Check if the record is not None before processing
        if record is not None:
            try:
                # Accessing specific fields or properties
                title = record['245']['a'] if '245' in record else 'N/A'
                author = record['100']['a'] if '100' in record else 'N/A'

                # Print information from the record (you can customize this part)
                print(f"Title: {title}, Author: {author}")

                # Perform additional processing or analysis as needed
            except Exception as e:
                print(f"Error processing record: {e}")
                print(record)
        else:
            print("Error: Unable to read a record.")

