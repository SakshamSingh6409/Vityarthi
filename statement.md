## Problem
Readers and students often need a lightweight tool to keep track of their books and the page they reached, using only local files and without a full database.

## Scope
1) Manage a small catalog of books stored in a JSON file
2) Provide a simple command-line interface for adding, editing, opening, and listing books
3) Allow backup and restore of book records to prevent accidental data loss
4) Modular structure so future improvements (like a GUI) are easy

## Target Users
1) Students and casual readers who want to track reading progress
2) Educators and reviewers looking for a clean, testable reference project

## High-Level Features
1) Open a book and check (or update) current page
2) Add or edit book records on disk
3) Backup and restore all book data
4) Simple help and error messages
5) Unit tests for core behavior