#!/bin/bash
echo "Current directory: $(pwd)"
echo "Files in current directory:"
ls -l
python3 Parser_exel/parser.py
