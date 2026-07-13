# Activity 318604 MP3 Metadata Placeholder Fix

META:
date=2026-07-13T13:01:16+02:00
host=fedora
system=Fedora_44_Workstation
activity_id=318604
file=/home/daniele/Downloads/no title piece.mp3
backup=/home/daniele/Downloads/metadata-fix-318604-20260713-125742/no title piece.mp3.backup
workdir=/home/daniele/Downloads/metadata-fix-318604-20260713-125742
default_player=org.gnome.Decibels.desktop
player_package=decibels-49.6.1-1.fc44.noarch
status=PASS_CON_WARNING

SUMMARY:
root_cause=the file initially had conflicting ID3v1 placeholder tags and ID3v2.3 real tags; user clarified that placeholders are the desired metadata.
change=set ID3v2.3 Title/Artist/Album to placeholders and removed ID3v1 duplicate family.
format=single ID3v2.3 tag family; no ID3v1; no ID3v2.4; no APEv2 observed.
audio=not_recoded; stream MD5 remained 59fc24f0be6ac33ec6b4330b744c5f95.
cache=Decibels GApplication in-memory state was terminated and file reopened; LocalSearch/TinySPARQL reindexed updated values for interpreted audio object.
warning=Decibels UI text was not fully exposed through AT-SPI automation, but Decibels reopened from a clean process and LocalSearch plus file metadata agree.

FINAL_TAGS:
TITLE=no title
ARTIST=no artist
ALBUM=no album
ALBUMARTIST=absent
DATE=2004
GENRE=Classical
COMMENT=absent
TRACK=10/13
cover_art=none_observed
encoding=ID3v2.3; text values ASCII-compatible placeholder strings

EVIDENCE:
ffprobe=title no title; artist no artist; album no album; genre Classical; date 2004; duration 373.368125; bitrate 128006.
exiftool=ID3v2_3 Title no title; Artist no artist; Album no album; Year 2004; Genre Classical; no ID3v1 output after fix.
mediainfo=Title no title; Album no album; Performer no artist; Genre Classical; Recorded date 2004; duration 6 min 13 s; overall bit rate 128 kb/s.
tinysparql=nie:title no title; nmm:artist urn:artist:no%20artist; nmm:musicAlbum placeholder album resource for recorded year 2004.
player=org.gnome.Decibels.desktop reopened via gio open after killing prior GApplication process.
