# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import csv
import re

class CsvToSql:
    @staticmethod
    def _escape_sql(value):
        if value is None:
            return "NULL"
        
        # Simple heuristic: try to convert to number
        if re.match(r'^-?\d+(\.\d+)?$', value):
            return value
            
        # Treat as string
        # Escape single quotes
        value = value.replace("'", "''")
        return f"'{value}'"

    @staticmethod
    def generate(csv_content, table_name, dialect='mysql'):
        # dialect could support 'mysql', 'postgres', 'sqlite' (mainly for quoting identifiers)
        # We'll default to standard SQL
        
        lines = csv_content.splitlines()
        reader = csv.reader(lines)
        
        try:
            headers = next(reader)
        except StopIteration:
            return None, "Error: CSV is empty."

        # Sanitize headers
        columns = [h.strip() for h in headers]
        col_str = ", ".join(columns)
        
        statements = []
        for row in reader:
            if not row: continue
            
            # Map values
            # Handle potential mismatch in length?
            if len(row) != len(columns):
                 # Skip or pad? Let's skip and log? 
                 # For now, just trunc/pad to match
                 pass
            
            values = [CsvToSql._escape_sql(val) for val in row]
            val_str = ", ".join(values)
            
            stmt = f"INSERT INTO {table_name} ({col_str}) VALUES ({val_str});"
            statements.append(stmt)
            
        return "\n".join(statements), None

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
