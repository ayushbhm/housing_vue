import os

# Define the structure
structure = {
    'backend': {
        'app': {
            '__init__.py': '',
            'config.py': '',
            'models': {
                '__init__.py': '',
                'user.py': '',
                'service.py': '',
                'service_request.py': '',
                'other_models.py': ''
            },
            'routes': {
                '__init__.py': '',
                'admin_routes.py': '',
                'customer_routes.py': '',
                'professional_routes.py': '',
                'auth_routes.py': ''
            },
            'tasks': {
                '__init__.py': '',
                'email_tasks.py': '',
                'reminder_tasks.py': '',
                'report_tasks.py': ''
            },
            'middleware': {
                '__init__.py': '',
                'authentication.py': ''
            },
            'utils': {
                '__init__.py': '',
                'email_utils.py': '',
                'notification_utils.py': ''
            },
            'static': {},
            'templates': {},
            'migrations': {},
            'instance': {}
        },
        'tests': {},
        'requirements.txt': '',
        'run.py': '',
        'README.md': ''
    }
}

# Function to create the directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # If content is a dictionary, create a folder
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursively create subfolders
        else:  # If content is a string, create a file
            with open(path, 'w') as f:
                f.write(content)

# Create the backend structure in the current directory
create_structure(os.getcwd(), structure)

print("Backend folder structure created successfully!")
