from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Suchindra Kumar",
    author_email="suchindr057@gmail.com",
    description="End-to-end MCQ Generator using LangChain and OpenAI",
    packages=find_packages(where="src"),  # finds packages only inside src/
    package_dir={"": "src"},  # maps the src/ folder as root for packages
    python_requires=">=3.10",
    install_requires=[
        "langchain-core>=0.2.2,<0.3.0",
        "langchain-openai>=0.1.8",
        "langchain-community>=0.2.0",
        "streamlit>=1.32.0",
        "pandas>=2.2.0",
        "python-dotenv>=1.0.1",
        "PyPDF2>=3.0.1",
        "openai>=1.6.1"
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            #StreamlitAPP.py is at project root, provide the full path
            "mcq-app=StreamlitAPP:main"  # optional: if you define main() in StreamlitAPP.py
        ]
    },
)
