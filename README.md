# MQTT Client Example

Follow these steps to set up the project after cloning it from GitHub.

## Steps to Set Up the Project

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

- **On Unix or MacOS**:

  ```bash
  source venv/bin/activate
  ```

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 4. Install Dependencies

Install the necessary dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5. Run the Project

Run your project scripts. For example:

```bash
python src/main.py
```

### 6. Adding New Dependencies

If you need to install new packages, use `pip` and update the `requirements.txt` file:

```bash
pip install new_package
pip freeze > requirements.txt
```

### Example `.gitignore`

Make sure your `.gitignore` file includes the following lines to exclude the virtual environment and other unnecessary files:

```gitignore
venv/
__pycache__/
*.pyc
.DS_Store
```

By following these instructions, you can set up your development environment and ensure all necessary dependencies are installed.
