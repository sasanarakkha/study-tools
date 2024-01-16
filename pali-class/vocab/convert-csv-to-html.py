import pandas as pd
import os
from string import Template

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get all CSV files in the current directory
csv_files = [file for file in os.listdir(current_directory) if file.endswith('.csv')]

for csv_file in csv_files:
    csv_path = os.path.join(current_directory, csv_file)

    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Replace NaN values with an empty string
    df = df.fillna("")

    # Sort by 'sbs_class'
    df = df.sort_values(by='cl.')

    # Convert DataFrame to HTML table
    html_table = df.to_html(index=False, classes='sortable')

    # Extract class number from filename
    class_number = os.path.splitext(csv_file)[0].split('-')[-1]

    # HTML template for the table
    html_template = Template('''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Vocabulary List for $class_number</title>
        <style>
        table {
            width: 100%;
            word-wrap: break-word;
        }
        th {
            text-align: center;
        }
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.1/js/jquery.tablesorter.min.js"></script>
        <script>
        $(document).ready(function() {
        $('table.sortable').tablesorter();
        });
        </script>
        </head>
        <body>
        <h1>Vocabulary List for $class_number</h1>
        <a href="https://sasanarakkha.github.io/study-tools/pali-class/vocab/index-vocab.html">go to index of vocabulary related to each class</a>
        <br>
        <br>
        $table
        </body>
        </html>
    ''')

    # Substitute the class number placeholder with the actual class number
    html_content = html_template.safe_substitute(table=html_table, class_number=class_number)

    # Generate output HTML file name
    html_output_file = os.path.splitext(csv_file)[0] + '.html'

    # Write the HTML content to the file in the same directory
    html_output_path = os.path.join(current_directory, html_output_file)
    with open(html_output_path, 'w') as file:
        file.write(html_content)

    print(f"HTML file '{html_output_file}' created successfully.")