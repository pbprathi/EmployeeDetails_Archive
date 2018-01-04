 from setuptools import setup,find_packages
    setup(
    name = "employeeArchive",
    version = "2.0.0",
    author = "Bhageerath",
    author_email = "pbprathi@gmail.com",
    description = "Employee Details Archive",
    license = "prathi",
    keywords = "Test Application",
    include_package_data=True,
    url = "https://github.com/pbprathi/python_Subprocess";,
    #install_requires=['subprocess'],
    packages=find_packages(exclude=['docs']),
    classifiers=["Development Status :: 1 - Alpha"],
    entry_points={
    'console_scripts': ['sapp=Emp_Archive.empDetailsWrtFile.py','sapp=Emp_Archive.empDetailsReadFile.py']}
