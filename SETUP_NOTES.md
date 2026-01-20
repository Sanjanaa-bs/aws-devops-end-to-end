# Local Development Setup Notes

## Python Dependencies Installation

The project uses Pydantic v2 which requires Rust compilation on some systems.

### Option 1: Use Docker (Recommended)
The Dockerfile includes all necessary build tools. Simply build and run:
```bash
docker build -t devops-platform:latest .
docker run -p 8000:8000 devops-platform:latest
```

### Option 2: Install Pre-built Wheels
Use Python 3.9-3.11 (not 3.13) for better wheel availability:
```bash
python3.11 -m venv .venv
.venv\Scripts\activate
pip install -r app/requirements.txt
```

### Option 3: Install Rust Toolchain
If you need to compile from source:
```bash
# Windows: Download from https://rustup.rs/
# Linux/Mac:
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Then install dependencies
pip install -r app/requirements.txt
```

### Option 4: Use Alternative Versions
Modify `app/requirements.txt` to use older versions with pre-built wheels:
```
fastapi==0.100.0
pydantic==1.10.13
```

## Production Deployment

In production (ECS Fargate), the Docker container handles all dependencies automatically. The multi-stage build includes gcc and build tools in the builder stage.

## Verification

Once dependencies are installed, verify the application:
```bash
cd app
python main.py
```

Visit http://localhost:8000/docs for API documentation.
