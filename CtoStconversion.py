import re
import argparse

def convert_c_to_st(c_code):
    """Converts basic C code into Structured Text (ST)"""
    
    # Convert variable declarations (int, float, bool)
    c_code = re.sub(r'\bint\s+(\w+)\s*=\s*(.+?);', r'VAR \1: INT := \2;', c_code)
    c_code = re.sub(r'\bfloat\s+(\w+)\s*=\s*(.+?);', r'VAR \1: REAL := \2;', c_code)
    c_code = re.sub(r'\bbool\s+(\w+)\s*=\s*(.+?);', r'VAR \1: BOOL := \2;', c_code)

    # Convert if-else statements
    c_code = re.sub(r'if\s*\((.+?)\)\s*{', r'IF \1 THEN', c_code)
    c_code = re.sub(r'}\s*else\s*{', r'ELSE', c_code)
    c_code = re.sub(r'}', r'END_IF;', c_code)

    # Convert while loops
    c_code = re.sub(r'while\s*\((.+?)\)\s*{', r'WHILE \1 DO', c_code)
    c_code = re.sub(r'}', r'END_WHILE;', c_code)

    # Convert for loops
    c_code = re.sub(r'for\s*\((int\s+)?(\w+)\s*=\s*(\d+);(.+?);(.+?)\)\s*{',
                    r'FOR \2 := \3 TO \4 DO', c_code)
    c_code = re.sub(r'}', r'END_FOR;', c_code)

    # Convert switch-case statements
    c_code = re.sub(r'switch\s*\((\w+)\)\s*{', r'CASE \1 OF', c_code)
    c_code = re.sub(r'case\s+(\w+):', r'\1:', c_code)
    c_code = re.sub(r'default:', r'ELSE', c_code)
    c_code = re.sub(r'break;', r'', c_code)
    c_code = re.sub(r'}', r'END_CASE;', c_code)

    # Convert function definitions
    c_code = re.sub(r'void\s+(\w+)\s*\((.*?)\)\s*{', r'FUNCTION \1\nVAR_INPUT \2\nEND_VAR\nBEGIN', c_code)
    c_code = re.sub(r'}', r'END_FUNCTION', c_code)

    return c_code

def process_file(input_file, output_file):
    """Reads C code from file, converts to ST, and writes to output file"""
    try:
        with open(input_file, 'r') as f:
            c_code = f.read()
        st_code = convert_c_to_st(c_code)
        with open(output_file, 'w') as f:
            f.write(st_code)
        print(f"Conversion successful! ST code saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert C code to Structured Text (ST).")
    parser.add_argument("input", help="Input C file")
    parser.add_argument("output", help="Output ST file")
    args = parser.parse_args()
    
    process_file(args.input, args.output)

if __name__ == "__main__":
    main()
