#!/usr/bin/env python3
"""Syntax Shaman - Because your IDE is napping and your code is crying."""

import sys
import re
from pathlib import Path

def find_syntax_sins(filepath):
    """Summon the spirits to reveal your punctuation crimes."""
    issues = []
    
    # Common syntax patterns that haunt developers
    patterns = {
        'missing_semicolon': r'[^;{}]\s*$',  # Lines ending without ; or {}
        'unclosed_paren': r'\([^)]*$',       # ( without matching )
        'unclosed_brace': r'\{[^}]*$',       # { without matching }
        'unclosed_bracket': r'\[[^\]]*$',   # [ without matching ]
        'dangling_comma': r',\s*$',          # Comma at line end (JS trauma)
    }
    
    try:
        with open(filepath, 'r') as f:
            for i, line in enumerate(f, 1):
                line = line.rstrip('\n')
                
                # Skip empty lines and comments (even shamans need breaks)
                if not line.strip() or line.strip().startswith(('//', '#', '/*')):
                    continue
                
                for sin_type, pattern in patterns.items():
                    if re.search(pattern, line):
                        issues.append({
                            'line': i,
                            'content': line[:50] + ('...' if len(line) > 50 else ''),
                            'type': sin_type,
                            'confidence': 'medium'  # We're guessing, not omnipotent
                        })
                        break  # One sin per line is enough shame
    except Exception as e:
        return [{'error': f"Shaman can't read this scroll: {e}"}]
    
    return issues

def main():
    """Main ritual - cast syntax detection spell on target file."""
    if len(sys.argv) != 2:
        print("Usage: python syntax_shaman.py <filename>")
        print("Example: python syntax_shaman.py crying.js")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"File '{filepath}' not found. Even ghosts need to exist.")
        sys.exit(1)
    
    issues = find_syntax_sins(filepath)
    
    if issues and 'error' in issues[0]:
        print(issues[0]['error'])
        return
    
    if not issues:
        print(f"\n✨ No obvious syntax sins found in {filepath.name}!")
        print("The code spirits are pleased (for now).")
        return
    
    print(f"\n🔮 Syntax Shaman reveals {len(issues)} potential issues in {filepath.name}:")
    print("=" * 60)
    
    for issue in issues:
        sin_desc = {
            'missing_semicolon': "Missing semicolon (the classic)",
            'unclosed_paren': "Unclosed parenthesis",
            'unclosed_brace': "Unclosed curly brace",
            'unclosed_bracket': "Unclosed square bracket",
            'dangling_comma': "Dangling comma (JS PTSD trigger)"
        }.get(issue['type'], issue['type'])
        
        print(f"Line {issue['line']}: {sin_desc}")
        print(f"    {issue['content']}")
        print()
    
    print(f"\n💡 Remember: I'm a shaman, not a compiler. Double-check these!")

if __name__ == "__main__":
    main()
