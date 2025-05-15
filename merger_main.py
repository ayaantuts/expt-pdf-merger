import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list:list[str], output_path:str)-> None:
    """
    Merges a list of PDFs into a single PDF.
    This function takes a list of PDF file paths and merges them into a single PDF file.
    It uses the PyPDF2 library to handle the merging process.
    If a PDF file does not exist, it will be skipped with a warning message.
    Args:
        pdf_list (list[str]): List of PDF file paths to merge.
        output_path (str): Path where the merged PDF will be saved.
    """
    merger = PdfMerger()
    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"Warning: {pdf} not found. Skipping.")
    merger.write(output_path)
    merger.close()

def main():
    print("\nIndividual file name format: <roll_no>_<subject>_Experiment_<experiment_number>.pdf")
    print("Full file name format: <roll_no>_<subject>_Full_Merged.pdf")
    roll_no = int(input("Enter roll number: (to help in renaming) ").strip())
    roll_no_str = "C0" + str(roll_no) if roll_no < 100 else "C" + str(roll_no)
    target_dir = input("Enter target directory path: ").strip()
    subject = input("Enter the subject name (e.g., DS, OS): ").strip()
    num_experiments = int(input("Enter number of experiments: "))
    include_code = input("Are there code PDFs? (yes/no): ").strip().lower() == 'yes'
    num_assignments = int(input("Enter number of assignments (enter 0 if none): "))
    include_initials = input("Include initials.pdf? (yes/no): ").strip().lower() == 'yes'
    initials_path = os.path.join(target_dir, f"{subject}_initials.pdf")
    print("Merging PDFs...")
    output_dir = os.path.join(target_dir, "output", "individual_merges")
    os.makedirs(output_dir, exist_ok=True)

    all_merged_paths:list[str] = []
    if include_initials and os.path.exists(initials_path):
        all_merged_paths.append(initials_path)
        print(f"Initials PDF added to merge list: {initials_path}")
    for i in range(1, num_experiments + 1):
        exp_folder = os.path.join(target_dir, f"Experiment {i}")
        writeup = os.path.join(exp_folder, f"{subject}_Writeup {i}.pdf")        
        code = os.path.join(exp_folder, f"{subject}_Codes {i}.pdf")

        pdfs_to_merge = [writeup]
        if include_code:
            if os.path.exists(code):
                pdfs_to_merge.append(code)
            else:
                print(f"Warning: {code} not found. Skipping code PDF.")

        merged_path = os.path.join(output_dir, f"{roll_no_str}_{subject}_Experiment_{i}.pdf")
        merge_pdfs(pdfs_to_merge, merged_path)
        all_merged_paths.append(merged_path)
        print(f"Merged {writeup} and {code if include_code else ''} into {merged_path}")

    # Handle assignments if any
    if num_assignments > 0:
        for i in range(1, num_assignments + 1):
            assignment_path = os.path.join(target_dir, f"{subject}_Assignment {i}.pdf")
            if os.path.exists(assignment_path):
                all_merged_paths.append(assignment_path)
                print(f"Added assignment PDF to merge list: {assignment_path}")
            else:
                print(f"Warning: {assignment_path} not found. Skipping assignment PDF.")
    # Final full merge
    full_merge_path = os.path.join(target_dir, "output", f"{roll_no_str}_{subject}_Full_Merged.pdf")
    merge_pdfs(all_merged_paths, full_merge_path)

    print(f"\nAll PDFs merged successfully!\nOutput stored in: {os.path.join(target_dir, 'output')}")

if __name__ == "__main__":
    main()