# Licensing
Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
See the LICENSE file for more information.

# library-version-wise-opinion-extration
Extract open source library’s version specific opinions from Stack Overflow


## Problem Statement
Stack Overflow contains hundreds of thousands of opinions regarding open source libraries that developers use in their everyday programming. However, there are two challenges for a developer to understand the gist of the opinions. First of all, because of the sheer number of posts, it becomes a non-trivial job to browse through useful opinions regarding a library. Secondly, in many cases, the version of the library is not mentioned in the post, and as a result, a reader cannot instantly understand which version has the problem or benefit being discussed in the post.

## Project Objective
The objective of the project would be to be able to collect and present release version specific opinions regarding an open source library from Stack Overflow.

## Project Scope
- The data would be collected from Stack Overflow data dump. Language of the library would be Python so that the version information can be collected from PyPI using REST API.
- The project will collect this library specific opinion about one or two sample library. Developing a generic any library data extraction would be outside of the scope of this project as there can be library or language specific challenges that may not be the primary interest in this Open Source Software course. However this can be extended as future expansion beyond this project scope.
- The project will contain minimum or no graphical user interface. Main target of the project would be prepare a backend data collection engine that will collect the opinions and map them with the version and can store the summary information in flat file or database storage as found appropriate during the project.

## Language and Tools
- Project will be implemented in Python language. GitHub is being used as repository.
- MySql will be used for data storage of Stack Overflow data dump.
- Python’s NLP related packages (e.g., Spacy) can be used for data extraction.

## Project Usage
In future, the outcome of this project may be used towards my other projects if it becomes relevant and useful. 

## License
- The project is licensed under MIT License (a permissive license with conditions only requiring preservation of copyright and license notices). 
- Licensed works, modifications, and larger works may be distributed under different terms and without source code.
- License link: https://github.com/minaoar/library-version-wise-opinion-extration/blob/main/LICENSE

## Contributing
We greatly appreciate any contribution to this project. Before creating a new issue or pull request, 

please read the contribution guidelines and policies in [CONTRIBUTING](https://github.com/minaoar/library-version-wise-opinion-extration/blob/main/CONTRIBUTING.md) file.



## How to Get Started
While you can try to build source code in your local machine, you can also use Docker to run the scripts.
Here is a simple way to start with the Docker:

1. Clone the repository of the project
2. Install docker desktop from [here](https://www.docker.com/get-started/) on your machine.
3. Go to the project directory you cloned. Then run the following command:
> docker build --no-cache -t library-opinion .
4. Now under Images tab of the installed Docker application, you can find the 'library-opinion' image.
5. Start the library-opinion image from the Docker application.
6. From the Containers tab of Docker application, you can see the library-opinion container is running.
7. You can enter in to CLI (command line interface) of the container. It will take you to the project directory inside the container.
8. In the CLI, you can go to 'source' folder and run script data_collection.py (python3 data_collection.py). 
9. It should give you an output similar to this (not exactly this and can change every time you run it):
> <img width="1435" alt="image" src="https://user-images.githubusercontent.com/5583535/198144309-71150b7f-fe75-489e-8ff3-4c040055553e.png">
