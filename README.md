# CSV to SQL Insert Generator

A utility to generate SQL `INSERT` statements from a CSV file. It automatically infers table names and handles basic string escaping.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Custom Table Names**: Defaults to filename, but can be overridden.
*   **Smart Escaping**: Automatically detects numbers vs strings and escapes single quotes.
*   **Standard SQL**: Generates queries compatible with MySQL, PostgreSQL, and SQLite.

## Usage

```bash
python run_generator.py [file] [options]
```

### Options

*   `--table`, `-t`: Specify the target table name.
*   `--output`, `-o`: Save the result to a SQL file.

### Examples

**1. Basic Generation**
```bash
python run_generator.py users.csv
```

**2. Custom Table and Output**
```bash
python run_generator.py data.csv -t my_users -o seed_data.sql
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
