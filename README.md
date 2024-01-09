# AirBnB clone - The console

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240109T092520Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1e7ee095fb79581e5c370561741911784111a17905b94acbe9b2c93b4a6567c0">

## Welcome to our AirBnB clone project in partial fulfillment of the requirements of alx
Please read the [AirBnB concept page](https://intranet.alxswe.com/concepts/66) to better understand what this project inetends to do

First step: A command interpreter to manage your AirBnB objects.
This is the first step towards building our first full web application: the AirBnB clone.<br>
This first step is very important because this is what we will use to build during this project<br>
with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to understand, below is a list of things to put in place:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and<br>
deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
