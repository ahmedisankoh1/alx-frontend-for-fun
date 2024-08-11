#!/usr/bin/python3

import sys
import os
import markdown

def main():
    # Step 1: Handle Command-Line Arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Step 2: Check if the File Exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Step 3: Convert Markdown to HTML
    with open(input_file, 'r') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)

    # Step 4: Write to Output File
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    # Step 5: Exit Gracefully
    sys.exit(0)

if __name__ == "__main__":
    main()
