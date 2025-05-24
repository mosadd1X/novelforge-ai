# Active Writer Profiles

This directory stores user-created and currently active writer profiles.

## Purpose
- Stores custom writer profiles created by users
- Managed by the `WriterProfileManager` class
- Profiles saved here are used for dynamic author selection

## File Format
Profiles are stored as JSON files with the naming convention:
`{author_name}_{profile_id}.json`

## Usage
- Automatically managed by the application
- Users can create custom profiles through the UI
- Profiles are loaded when generating books with specific author styles

## Status
Currently empty - profiles will be created here when users generate custom author profiles.
