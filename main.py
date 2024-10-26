import xml.etree.ElementTree as ET
import os
import urllib.parse
import shutil

# Function to expand paths if they contain '~'
def expand_path(path):
    return os.path.expanduser(path)

# Ask for input file and output directory
xml_file_path = expand_path(input("Enter the full path to your Rekordbox XML file: ").strip())
output_base_path = expand_path(input("Enter the full path to the output directory: ").strip())

# Check if the XML file exists
if not os.path.isfile(xml_file_path):
    print(f"Error: The file '{xml_file_path}' does not exist.")
    exit(1)

# Check if the output directory exists; create it if it does not
if not os.path.exists(output_base_path):
    os.makedirs(output_base_path)
    print(f"Created output directory: {output_base_path}")
else:
    print(f"Output directory already exists: {output_base_path}")

# Parse the Rekordbox XML file
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
except ET.ParseError as e:
    print(f"Error parsing XML file: {e}")
    exit(1)

# Step 1: Store track locations from COLLECTION by TrackID
tracks = {}
for track in root.findall("./COLLECTION/TRACK"):
    track_id = track.get("TrackID")
    track_location = track.get("Location")
    track_location = urllib.parse.unquote(track_location.replace("file://localhost", ""))  # Decoding URL encoding
    tracks[track_id] = track_location
    print(f"Found track: ID={track_id}, Location={track_location}")

# Step 2: Process each playlist, creating folders and copying associated tracks
def process_playlist(node, parent_folder):
    playlist_name = node.get("Name")
    playlist_folder = os.path.join(parent_folder, playlist_name)
    os.makedirs(playlist_folder, exist_ok=True)
    print(f"\nCreated folder for playlist '{playlist_name}': {playlist_folder}")

    tracks_copied = 0
    # Copy tracks in this playlist node
    for track_ref in node.findall("TRACK"):
        track_id = track_ref.get("Key")
        track_path = tracks.get(track_id)
        
        if track_path:
            if os.path.isfile(track_path):
                shutil.copy2(track_path, playlist_folder)
                print(f"  Copied '{track_path}' to '{playlist_folder}'")
                tracks_copied += 1
            else:
                print(f"  Warning: File path '{track_path}' for TrackID {track_id} does not exist on disk.")
        else:
            print(f"  Warning: TrackID {track_id} not found in COLLECTION.")

    if tracks_copied == 0:
        print(f"  No tracks copied for playlist '{playlist_name}' (possibly empty or missing files)")

    # Recursively process sub-playlists if they exist
    for child_node in node.findall("NODE"):
        process_playlist(child_node, playlist_folder)

# Start processing playlists from the root <NODE> in <PLAYLISTS>
for root_node in root.findall("./PLAYLISTS/NODE[@Type='0']"):
    process_playlist(root_node, output_base_path)

print("\nProcessing complete.")
