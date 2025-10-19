import os
import sys

def process_project_files(root_dir='.'):
    
    # Define the file extensions to target
    target_extensions = ('.html', '.css', '.js')
    
    print(f"--- Rovidgh Project File Processor ---")
    print(f"Starting search and processing in: {os.path.abspath(root_dir)}")
    print("-" * 60)
    
    files_processed_count = 0

    # os.walk yields (current directory path, directory names in it, file names in it)
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            
            # Check if the file has one of the target extensions
            if filename.lower().endswith(target_extensions):
                file_path = os.path.join(dirpath, filename)
                
                # Skip system files or hidden files common on various OSs (e.g., in version control)
                if filename.startswith('.') or os.path.islink(file_path):
                    continue

                print(f"Processing: {file_path}")
                
                try:
                    # Attempt to read the file content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    modified_lines = []
                    changes_made = False
                    
                    for line in lines:
                        # Operation 1: Remove entire line if it contains the text 'empty-line'
                        if 'HTTrack' in line:
                            changes_made = True
                            continue # Skip adding this line to modified_lines
                        
                        # Operation 2: Replace all text 'template' with 'gooming'
                        new_line = line.replace('Assan', 'Rovid')
                        
                        if new_line != line:
                            changes_made = True
                            
                        modified_lines.append(new_line)

                    # Overwrite the original file only if changes were made
                    if changes_made:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(modified_lines)
                        print(f"  -> SUCCESS: Changes applied and file updated.")
                        files_processed_count += 1
                    else:
                        print(f"  -> SKIPPED: No relevant changes needed.")
                        
                except IOError as e:
                    # Handle file I/O errors (e.g., permission denied)
                    print(f"  -> ERROR (IO): Could not read/write file: {e}", file=sys.stderr)
                except UnicodeDecodeError as e:
                    # Handle encoding issues (e.g., binary file detected)
                    print(f"  -> ERROR (Encoding): File is not standard UTF-8 text: {e}", file=sys.stderr)
                except Exception as e:
                    # Handle any other unexpected errors
                    print(f"  -> ERROR (General): An unexpected error occurred: {e}", file=sys.stderr)
                    
    print("-" * 60)
    print(f"Processing complete. Total files modified: {files_processed_count}.")

if __name__ == "__main__":
    # Execute the function, starting the search from the current working directory
    process_project_files(root_dir='.')