from setuptools import setup, find_packages

setup(
    name="datalake-mcp",
    version="0.1.0",
    description="MCP server for AWS Data Lakes",
    author="AI DataPlatform",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "mcp>=0.1.0",
        "boto3>=1.34.0",
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
    ],
)
