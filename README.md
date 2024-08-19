## Use
This code is designed to extract embedded files from HPDF documents. The extract_func 
function identifies these files in a specified directory, reads them using PyPDF2, and retrieves any embedded 
attachments. These attachments are then saved to a newly created directory named after the original file. The helper 
functions hpdf_finder and get_attachments assist in locating the .hpdf files and extracting the embedded files, 
respectively. The code also handles errors and updates a GUI window with the process status.
