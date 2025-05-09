# PDF Merger for Experiment Documentation

This Python tool helps you merge write-ups and optional code PDFs for a series of experiments in an academic project. It also supports adding a combined certificate and rubrics PDF (`[subject]_initials.pdf`) and optional assignment PDFs.

---

## Table of Contents
- [Folder Structure Requirements](#folder-structure-requirements)
- [Installation](#installation)
- [1. Interactive Script (Main Tool)](#1-interactive-script-main-tool)
- [2. CLI Tool Usage](#2-cli-tool-usage)
- [3. File Renamer Utility](#3-file-renamer-utility)
- [Author](#author)

---

## Folder Structure Requirements

The directory structure should follow this format:

```bash

[target_dir]/
├── [subject]_initials.pdf                  # Optional certificate + rubrics file
├── [subject]_Assignment 1.pdf             # Optional assignment PDFs
├── [subject]_Assignment 2.pdf
├── ...
├── Experiment 1/
│   ├── [subject]_Writeup 1.pdf
│   └── [subject]_Codes 1.pdf              # Optional
├── Experiment 2/
│   ├── [subject]_Writeup 2.pdf
│   └── [subject]_Codes 2.pdf
└── ...

```
Where:
* `[target_dir]` is the root directory containing all subject folders.
* `[subject]_initials.pdf` is the combined certificate and rubrics PDF.
* `[subject]_Assignment_1.pdf` and `[subject]_Assignment_2.pdf` are optional assignment PDFs.

---

## Installation

First, clone the repository:

```bash
git clone https://github.com/ayaantuts/expt-pdf-merger
cd expt-pdf-merger
```

It is recommended to use [uv](https://docs.astral.sh/uv/) for this project. You can install it using [the installation guide](https://docs.astral.sh/uv/getting-started/installation/) 

Setup the project using:
```bash
uv sync
```

OR

If you prefer not to use `uv`, you can use `pip` to install the required packages:

But first you need to activate the virtual environment:
```bash
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux
```

Then install the required packages:
```bash
pip install -r requirements.txt
```

---

## 1. Interactive Script (Main Tool)

Run the interactive version:

```bash
python merger_main.py
```

You will be prompted for:

* Target directory path
* Subject name (e.g., DS, OS)
* Number of experiments
* Whether to include code PDFs
* Number of assignments (enter 0 if none)
* Whether to include `[subject]_initials.pdf`

### Output

After execution:

```
[target_dir]/output/
├── C026_[subject]_Full_Merged.pdf
└── individual_merges/
    ├── C026_[subject]_Experiment_1.pdf
    ├── C026_[subject]_Experiment_2.pdf
    └── ...
```

---

## 2. CLI Tool Usage

Use this version if you prefer command-line flags or scripting integration:

```bash
python merge_tool_cli.py \
  --target-dir "/path/to/root" \
  --subject "[subject]" \
  --num 8 \
  --include-code \
  --include-initials \
  --num-assignments 2
```

### CLI Flags

| Flag                 | Description                                                         | Required |
| -------------------- | ------------------------------------------------------------------- | -------- |
| `--target-dir`       | Root directory containing subject folders and PDF files             | Yes      |
| `--subject`          | Subject name (e.g., `[subject]`, `OS`)                              | Yes      |
| `--num`              | Number of experiments                                               | Yes      |
| `--include-code`     | If set, includes code PDFs (`Subject_Codes X.pdf`)                  | No       |
| `--include-initials` | If set, prepen[subject] `[subject]_initials.pdf` to the final merge | No       |
| `--num-assignments`  | Number of assignments (e.g., 2 for `Subject_Assignment_1.pdf`)      | No       |

---

## 3. File Renamer Utility

This utility renames specific PDFs in `Experiment $` folders by prepending a given string, where `$` is the experiment number.

### Interactive Version

```bash
python file_renamer_main.py
```

Prompts you for:

* Parent directory path
* File pattern to match (e.g., `Codes $.pdf`)
* Prefix to prepend (e.g., `ML_`)

### CLI Version

```bash
python file_renamer_cli.py "/path/to/root" "Codes $.pdf" "ML_"
```

Renames files like:

```
Experiment 1/Codes 1.pdf -> Experiment 1/ML_Codes 1.pdf
```

Only affects folders named `Experiment *`.

---

## Author

Created by [Ayaan Shaikh](https://github.com/ayaantuts), DJ Sanghvi College of Engineering.