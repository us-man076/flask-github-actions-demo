# Flask GitHub Actions Demo Project

A simple Flask project to practice GitHub Actions workflows.

## Setup
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Run app: `python app.py`

## GitHub Actions Workflows
- **push-workflow.yml**: Runs tests on push to main branch
- **pr-workflow.yml**: Runs tests on pull requests to main branch