from setuptools import setup

if __name__ == "__main__":
    setup(
        package_data={
            # If any package contains *.txt or *.rst files, include them:
            "": ["*.md"],
        }
    )
