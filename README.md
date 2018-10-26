# pyextract
Automatically extract compressed torrents on completion

### Rational
In my home I have set Radarr & Sonarr as download managers for torrents.
Problem is, that some movies/episodes are compressed and Radarr & Sonarr don't know how to extract them.
This script is configured to run on Torrent download completion and extract the torrent.

### Features
Uncompress ZIP & RAR files
Support uncompressing to specific output directory.
Uncompress folders recursively (IE. Season Box sets)

### Installation
In order to work, the p7zip executable needs to be available:
#### Installation in Ubuntu:
```
sudo apt-get install p7zip-full
```

## Integration with Torrent clients

### Qbittorent
Tools -> Preferences -> Downloads -> "Run external program on torrent completion".
```
"/usr/local/bin/pyextract.py %F"
```

## Additional options
You can set a speicifc output folder by providing `"-o <FOLDER>"`to the `pyextract.py` script.
