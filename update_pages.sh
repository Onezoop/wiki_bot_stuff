#!/usr/bin/bash
WIKI_URL=$(cat WIKI_URL.txt)
curl -s -o pages.json "$WIKI_URL/api.php?action=query&list=allpages&aplimit=max&format=json"
