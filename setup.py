from setuptools import setup

setup(
        name="pythonwp",
        packages=["pythonwp"],
        include_package_data=True,
        install_requires=[
            "bcrypt",
            "flask",
            "flask-login",
            "flask-migrate",
            "mysql-python",
            "Flask-Session",
            "flask-sqlalchemy",
        ]
)
