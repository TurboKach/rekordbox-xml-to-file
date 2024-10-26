# Rekordbox Playlist Export Script

This Python script parses a Rekordbox XML export file, locates each track by `TrackID`, and copies the tracks into subfolders organized by playlist. It’s particularly useful for DJs and music enthusiasts who want to arrange tracks on disk by playlist structure from Rekordbox.

## Features
- Parses Rekordbox XML files to extract playlists and track locations.
- Creates a folder for each playlist and copies the corresponding tracks.
- Supports recursive playlists (sub-playlists).
- Compatible with macOS.

## Requirements
- Python 3.x
- Modules used: `xml.etree.ElementTree`, `os`, `urllib.parse`, `shutil`

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TurboKach/rekordbox-playlist-xml-file-export.git
   cd rekordbox-playlist-xml-file-export
   ```

2. **Ensure Python 3 is Installed**:
   Check your Python version:
   ```bash
   python3 --version
   ```

3. **Run the Script**:
   Execute the script with:
   ```bash
   python3 main.py
   ```

## Usage

The script will prompt for:
- **Path to Rekordbox XML file**: Full path to the XML export file from Rekordbox.
- **Output Directory**: Directory where playlist folders and copied tracks will be created.

### Example Usage

1. **Run the Script**:
   ```bash
   python3 main.py
   ```

2. **Input Paths**:
   ```
   Enter the full path to your Rekordbox XML file: /Users/yourusername/Documents/rekordbox.xml
   Enter the full path to the output directory: /Users/yourusername/Music/RekordboxPlaylists
   ```

   The script will create a folder for each playlist within the specified output directory and copy the relevant tracks into each folder.

### Folder Structure Example

If your Rekordbox XML file contains the following playlists:

- `House`
- `Techno`
  - `Acid Techno` (sub-playlist)

The output directory will look like:

```
/Users/yourusername/Music/RekordboxPlaylists/
├── House/
│   ├── track1.mp3
│   └── track2.mp3
├── Techno/
│   └── Acid Techno/
│       ├── track3.mp3
│       └── track4.mp3
```

## Troubleshooting

- **File Not Found Warnings**: If you see warnings about missing files, ensure that the paths in your Rekordbox XML file are valid and accessible on your system.
- **Empty Folders**: If no files are copied to the playlist folders, verify that the playlist structure and `TrackID` associations in your XML file are correct.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add my feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Instructions for Adding to GitHub
1. Create a new repository on GitHub.
2. Copy and paste this `README.md` into your repository.
3. Add the script and commit the files.
4. Push the repository to GitHub with `git push origin main`.

This `README.md` should help users understand the purpose, setup, and usage of your script. Let me know if you’d like any specific adjustments!
