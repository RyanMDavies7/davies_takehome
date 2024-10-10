# Project Documentation Index

Welcome to the documentation for the Roman Numeral, String Reversal, and Clock Angle Task project.

## Directory Structure Overview

This project follows a well-structured layout designed for maintainability, extensibility, and compatibility with Continuous Integration (CI) and Continuous Deployment (CD).

### Root Level

- **main.py**: Entry point for the project. This script can be run directly to execute the three tasks: Roman numeral conversion, word reversal, and clock angle calculation.
- **requirements.txt**: Specifies the Python dependencies for this project.
- **README.md**: Contains project overview, setup instructions, and usage guidelines.

### Source Code (src/)

- **clock/clockangles.py**: Contains the logic for calculating the angle between the hands of a clock.
    - [Clock Angle Calculation Documentation](clock_angle.md)
- **roman_numerals/convert.py**: Contains the logic for converting Roman numerals to integers.
    - [Roman Numeral Conversion Documentation](roman_numeral_conversion.md)
- **string_operations/reverse_words.py**: Contains the logic for reversing the words in a string.
    - [String Reversal Documentation](string_reversal.md)

### Configuration (configs/)

- **development.yaml**: Configuration for development environments.
- **production.yaml**: Configuration for production environments.

### Documentation (docs/)

This directory contains detailed documentation for the project’s individual components:

- [Roman Numeral Conversion Documentation](roman_numeral_conversion.md)
- [String Reversal Documentation](string_reversal.md)
- [Clock Angle Calculation Documentation](clock_angle.md)

### Tests (tests/)

Contains unit tests for each of the three tasks, ensuring that all components of the project function correctly:

- **test_roman_numerals.py**: Unit tests for Roman numeral conversion.
- **test_string_ops.py**: Unit tests for string reversal functionality.
- **test_clock_angle.py**: Unit tests for the clock angle calculation.

### GitHub Actions (CI/CD) Configuration (.github/)

- **workflows/main.yml**: GitHub Actions workflow for Continuous Integration. This file contains the configuration for running tests and linting the code on every push or pull request.

### Virtual Environment (.venv/)

- **.venv/**: Contains the virtual environment files (Python dependencies and environment configuration). This folder is typically ignored by version control using `.gitignore`.

### Other Files

- **.gitignore**: Specifies files and directories to be ignored by Git for this project (e.g., `.venv/`).
