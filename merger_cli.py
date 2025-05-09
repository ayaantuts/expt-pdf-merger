import os
import argparse
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list:list[str], output_path:str)->None:
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
	parser = argparse.ArgumentParser(description="Merge experiment PDFs into one complete document.")
	parser.add_argument("--target-dir", required=True, help="Root directory containing subject folders")
	parser.add_argument("--subject", required=True, help="Subject name (folder under root)")
	parser.add_argument("--num", type=int, required=True, help="Number of experiments")
	parser.add_argument("--include-code", action="store_true", help="Include Codes PDFs if available")
	parser.add_argument("--include-initials", action="store_true", help="Prepend initials.pdf if available")
	parser.add_argument("--num-assignments", type=int, default=0, help="Number of assignments (default: 0)")

	args = parser.parse_args()

	output_dir:str = os.path.join(args.target_dir, "output", "individual_merges")
	os.makedirs(output_dir, exist_ok=True)

	all_merged_paths:list[str] = []
	if args.include_initials:
		initials_path = os.path.join(args.target_dir, f"{args.subject}_initials.pdf")
		if os.path.exists(initials_path):
			all_merged_paths.append(initials_path)
			print(f"Initials PDF added to merge list: {initials_path}")
		else:
			print(f"Warning: {initials_path} not found. Skipping initials PDF.")

	for i in range(1, args.num + 1):
		exp_folder = os.path.join(args.target_dir, f"Experiment {i}")
		writeup = os.path.join(exp_folder, f"{args.subject}_Writeup {i}.pdf")
		code = os.path.join(exp_folder, f"{args.subject}_Codes {i}.pdf")

		pdfs_to_merge = [writeup]
		if args.include_code:
			if os.path.exists(code):
				pdfs_to_merge.append(code)
			else:
				print(f"Warning: {code} not found. Skipping code PDF.")

		merged_path = os.path.join(output_dir, f"C026_{args.subject}_Experiment_{i}_merged.pdf")
		merge_pdfs(pdfs_to_merge, merged_path)
		all_merged_paths.append(merged_path)
		print(f"Merged {writeup} and {code if args.include_code else ''} into {merged_path}")

	# Handle assignments if any
	if args.num_assignments > 0:
		for i in range(1, args.num_assignments + 1):
			assignment_path = os.path.join(args.target_dir, f"{args.subject}_Assignment {i}.pdf")
			if os.path.exists(assignment_path):
				all_merged_paths.append(assignment_path)
				print(f"Added assignment PDF to merge list: {assignment_path}")
			else:
				print(f"Warning: {assignment_path} not found. Skipping assignment PDF.")
	# Final full merge

	full_merge_path = os.path.join(args.target_dir, "output", f"C026_{args.subject}_Full_Merged.pdf")
	merge_pdfs(all_merged_paths, full_merge_path)

	print(f"\nCLI merge complete.")
	print(f"Individual merges stored in: {output_dir}")
	print(f"Final full merged PDF: {full_merge_path}")

if __name__ == "__main__":
	main()