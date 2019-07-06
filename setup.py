import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='face_recognition',
     version='0.1',
     scripts=['face_recognition'],
     author="Dewald Abrie",
     author_email="dewaldabrie@gmail.com",
     description="light-weight face recognition",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dewaldabrie/face_recognition",
     packages=setuptools.find_packages(),
     package_data={'': ['models/facenet.tflite']},
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )