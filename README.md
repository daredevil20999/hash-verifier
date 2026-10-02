# File Hash Verifier

A small Python command line tool that checks a file's integrity by comparing its SHA256 hash against an expected value. Useful for confirming a download wasn't corrupted or tampered with, for example an ISO or installer whose publisher lists a checksum.

## Requirements

Python 3.11 or newer. No external packages needed. The script uses `hashlib.file_digest`, which was added in 3.11.

## Usage

```
python hashverifier.py <file> <expected_sha256>
```

To get a known hash to test with:

```
# Linux
sha256sum test.txt

# macOS
shasum -a 256 test.txt

# Windows (PowerShell)
Get-FileHash test.txt -Algorithm SHA256
```

## Example output

Match:

```
$ python hashverifier.py test.txt 5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03
Calculated Hash: 5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03
Expected Hash: 5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03
Hash verification successful
```

Mismatch:

```
$ python hashverifier.py test.txt abc123
Calculated Hash: 5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03
Expected Hash: abc123
Hash verification failed.
```

Missing file:

```
$ python hashverifier.py nope.txt abc123
Error: The file at nope.txt was not found.
Hash verification failed.
```

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Hash matches |
| 1 | Hash mismatch or error (missing file, permission denied, path is a directory) |

This makes the tool usable in shell scripts, for example `python hashverifier.py file.iso <hash> && echo safe`.

## How it works

The script opens the file in binary mode and computes its SHA256 digest with `hashlib.file_digest`, which reads the file in chunks so large files don't need to fit in memory. The expected hash is stripped of whitespace and lowercased, so values pasted from websites compare correctly. Any change to the file, even a single bit, produces a completely different hash.

## Possible improvements

- `--algorithm` flag for MD5, SHA1, and SHA512
- Separate exit code for errors versus mismatches
- Support for checksum files containing multiple hashes

## License

MIT
