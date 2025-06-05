# 📊 DocuControl

**DocuControl** is a Python application designed to automate report execution and document control in technical or administrative environments. It provides a simple and visual interface using `Tkinter`, with features to run scripts, track statuses, and manage generated files.

## 🎯 Main Features

- 📂 **Automated Script Execution**: Run external scripts that generate reports and control files.
- 📊 **Status Display**: Show real-time messages and success/error feedback.
- 🧾 **Generated File Management**: Copy and open Excel files directly from the interface.
- 📁 **Integrated File Viewer**: View Excel files in a new dedicated window.
- ⚙️ **User-Friendly GUI**: Clean buttons, intuitive workflow, and real-time status updates.

## 🗂️ Project Structure
```
DocuControl/
├── main.py # Launches the main GUI window
├── funciones.py # Handles script execution, file copying, and status logic
├── visor_excel.py # Manages the integrated Excel file viewer
├── estilo.py # Defines the visual style of the GUI and tables
├── recursos/
│ └── icono.ico # Application icon
└── README.md # This documentation file
```

## 🧠 Module Overview

### `main.py`

- Starts the main application window.
- Includes buttons to:
  - Execute defined scripts.
  - Display system messages.
  - Open the integrated Excel viewer.

### `funciones.py`

- Backend logic for:
  - Running external scripts.
  - Copying output Excel files to target directories.
  - Showing feedback messages with color indicators (success, warning, error).

### `visor_excel.py`

- A standalone window to browse and open `.xlsx` files.
- Displays files in a scrollable table with file names and open buttons.

### `estilo.py`

- Defines the visual styling of tables:
  - Conditional formatting based on document status (Approved, Commented, Rejected, etc.).
  - Dark blue headers with white text.
  - Light blue cells for visual consistency.

## 🛠️ Requirements

- Python 3.7 or higher
- Standard libraries:
  - `tkinter`
  - `subprocess`
  - `os`
  - `shutil`
  - `openpyxl` (for Excel file operations)

## 🤝 Contributions

Contributions are welcome! You can:
Suggest improvements
Report bugs
Propose new features

Feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License.

Built with 💻 by @jparedesDS
