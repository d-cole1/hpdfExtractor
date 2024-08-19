import os
import PyPDF2
from pathlib import Path


# MAIN FUNCTION
def extract_func(window, values):
    try:
        filepaths = hpdf_finder(values['source'])
        if not filepaths:
            window.write_event_value("Error", "no_files_found")

        for file in filepaths:
            handler = open(file, 'rb')  # open file
            reader = PyPDF2.PdfReader(handler)
            dictionary = get_attachments(reader)

            output_dir = os.path.join(values['source'], Path(file).stem)
            os.makedirs(output_dir, exist_ok=True)  # Make output directory

            for f_name, f_data in dictionary.items():
                with open(os.path.join(output_dir, f_name), 'wb') as outfile:
                    outfile.write(f_data)  # Save Data

        window.write_event_value("Done", None)

    except Exception as e:
        window.write_event_value("Error", str(e))


# HELPER FUNCTIONS
def hpdf_finder(source_dir):
    hpdf_files = []
    extensions = (".hpdf", ".HPDF")
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(extensions):
                hpdf_files.append(os.path.join(root, file))
    hpdf_files = [item.replace("\\", "/") for item in hpdf_files]
    return hpdf_files


def get_attachments(reader):

    # Retrieves the file attachments of the HPDF as a dictionary of file names
    # and the file data as a bytestring.
    # :return: dictionary of filenames and byte strings

    catalog = reader.trailer["/Root"]  # get catalog of all items inside PDF Structure
    file_names = catalog['/Names']['/EmbeddedFiles']['/Kids']  # get list of embedded filenames
    attachments = {}  # create a blank dictionary for output data
    for f in range(len(file_names)):
        f_dict = file_names[f].get_object()
        name = f_dict['/Names'][0]
        f_more = f_dict['/Names'][1].get_object()
        f_data = f_more['/EF']['/F'].get_data()
        attachments[name] = f_data

    return attachments
