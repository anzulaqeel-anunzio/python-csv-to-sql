# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import CsvToSql

def main():
    parser = argparse.ArgumentParser(description="CSV to SQL Insert Generator")
    parser.add_argument("file", help="Input CSV file")
    parser.add_argument("--table", "-t", help="Target SQL table name (default: filename)")
    parser.add_argument("--output", "-o", help="Output SQL file")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    table_name = args.table
    if not table_name:
        base = os.path.basename(args.file)
        table_name = os.path.splitext(base)[0]
        # Sanitize table name (replace spaces with _, remove weird chars)
        table_name = "".join(c if c.isalnum() else "_" for c in table_name)

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            csv_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    sql_output, error = CsvToSql.generate(csv_content, table_name)

    if error:
        print(error)
        sys.exit(1)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(sql_output)
            print(f"SQL statements saved to {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
    else:
        print(sql_output)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
