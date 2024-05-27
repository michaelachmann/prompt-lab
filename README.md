# Prompt-Lab

Welcome to the Prompt-Lab repository, a project developed by students of the M.A. Digital Humanities course in the "Übung Webtechnologien" class at the University of Regensburg.

## Project Overview

Prompt-Lab is a Django-based web application designed to help researchers and practitioners keep detailed lab notes while working with machine learning and prompts. The application allows users to save data on datasets, models, experiments, and prompts, providing a comprehensive and organized way to manage and document their machine learning workflows.

## Class Details

- **Instructor**: Michael Achmann-Denkler
  - [Profile](https://go.ur.de/michael-achmann)
- **Course**: Übung Webtechnologien
  - [Course Page](https://campusportal.uni-regensburg.de:443/qisserver/pages/startFlow.xhtml?_flowId=detailView-flow&unitId=52563&periodId=425&navigationPosition=hisinoneLehrorganisation,examEventOverviewOwn)
- **Semester**: Sommersemester 2024
- **University**: University of Regensburg

## Project Goals

- Learn and apply web development principles using Django.
- Develop practical skills in building and deploying web applications.
- Collaborate effectively in a team environment.
- Gain experience with version control using Git and GitHub.
- Create a functional application for documenting machine learning experiments, datasets, models, and prompts.

## Features

- **Dataset Management**: Store and manage details about datasets used in experiments.
- **Model Tracking**: Keep track of different machine learning models, including their configurations and performance metrics.
- **Experiment Documentation**: Document experiments with detailed notes on methodologies, results, and observations.
- **Prompt Tracking**: Manage and track prompts used with Large Language Models (LLMs), including prompt variations, results, and performance metrics.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/prompt-lab.git
    cd prompt-lab
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Contributing

We welcome contributions from all students. To contribute:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your fork.
5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or inquiries, please contact the course instructor:

- **Michael Achmann-Denkler**
  - [Profile](https://go.ur.de/michael-achmann)
  - University of Regensburg
