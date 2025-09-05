## `hackthefender.txt` (Python script)

# Hack the Fender
Simulated security exercise: extract usernames, leave a boss message, and overwrite passwords with ASCII art.

## Usage
```bash
mv hackthefender.txt hackthefender.py
python hackthefender.py
```
## Notes
Reads passwords.csv and extracts Username values.

Writes compromised usernames to compromised_users.txt.

Saves JSON message for “The Boss”.

Writes ASCII art signature into new_passwords.csv.

## Skills Practiced
File I/O with CSV and JSON.

Iterating with csv.DictReader.

Writing multiple file formats in one program.

String handling and ASCII art embedding.
