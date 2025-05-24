# Archived Writer Profiles

This directory stores archived/deleted writer profiles.

## Purpose
- Stores profiles that have been archived or deleted
- Managed by the `WriterProfileManager` class
- Allows recovery of previously used profiles

## File Format
Archived profiles are stored as JSON files with the naming convention:
`{author_name}_{profile_id}.json`

## Usage
- Profiles are moved here when archived through the WriterProfileManager
- Can be loaded when `include_archived=True` is specified
- Provides a safety net for accidentally deleted profiles

## Status
Currently empty - profiles will be moved here when users archive custom profiles.
