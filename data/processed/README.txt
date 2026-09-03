# ascii-art

This project generates ASCII art representations from input text using different font styles.

## Usage

Run the program with:
```
go run . <inputstring> [bannerfile.txt]
```
- `<inputstring>`: The text you want to convert to ASCII art.
- `[bannerfile.txt]`: (Optional) Banner font file. Options: `standard.txt`, `shadow.txt`, `thinkertoy.txt`. Defaults to `standard.txt`.

Example:
```
go run . "Hello\nWorld" shadow.txt
```

## Features

- Supports multiple banner styles.
- Handles multi-line input (use `\n` for newlines).
- Validates input for printable ASCII characters.

## Testing

Run all tests with:
```
go test -v
```

## Banner Files

- `standard.txt`
- `shadow.txt`
- `thinkertoy.txt`

