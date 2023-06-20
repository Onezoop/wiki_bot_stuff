#!/usr/bin/bash
if [[ $* == *-u* ]]; then
  echo "Update triggered!"
  ./update_pages.sh
fi
echo "starting bot..."
python3 main.py
