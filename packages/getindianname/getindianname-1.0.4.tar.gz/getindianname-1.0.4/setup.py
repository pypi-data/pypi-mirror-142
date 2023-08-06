import setuptools

with open("README.md", "r",encoding="UTF8") as data:
    readme = data.read()

setuptools.setup(
	name="getindianname",
	version="1.0.4",
	author="Devesh Singh",
	author_email="connect.world12345@gmail.com",
	description="Generate names based on India. Generate more than 50K unique name within 5 seconds. Names Automaticaly added and updated. About 10+ names were added daily.",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/techux/getindianname",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License","Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
	 ],
	packages=["getindianname"],
	include_package_data=True,
	python_requires='>=2.0',

) 