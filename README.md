<div align="center">
  <img src="./assets/logo.png" alt="Logo" width="150"/>

  # Search Engine

  ![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Version 0.1](https://img.shields.io/badge/version-0.1-green.svg)
  ![Status: Stable](https://img.shields.io/badge/status-stable-brightgreen.svg)

  <p>
     A customized search engine built on top of <strong>SearxNG</strong>, designed to inspect and possibly re-rank search results by detecting <strong>biases</strong>, ensuring that users receive diverse information.
  </p>

</div>

## Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 as a base programming environment.

### Setup

#### 1. Clone the repository:

```bash
git clone https://github.com/ngi-indi/module-search.git
cd module-search
```

#### 2. Set up the virtual environment (optional but recommended):

  - On Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

  - On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Install dependencies:
Install the required Python packages by running:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

#### 1. Build the Docker image:
Run the following command to build the Docker image.

    docker build -t searchengine .

#### 2. Start the Searx server:
After the image is built, start the container with the following command

    docker run -d --name searchengine --network indi_network -p 8080:8080 searchengine

#### 3. Access the web interface:

   Open your browser and go to http://127.0.0.1:8080/.

## Contributing

### Reporting bugs and requesting features
- If you find a bug, please open an issue.
- To request a feature, feel free to open an issue as well.

### Developing a new feature

1. **Fork the repository** by clicking the "Fork" button at the top right of this page.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/ngi-indi/module-bias-manager.git
   ```
3. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature-branch
   ```
4. **Make your changes.** Please follow the existing code style and conventions.
5. **Commit your changes** with a descriptive commit message:
   ```bash
   git commit -m "Add new feature: explanation of bias model predictions"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature-branch
   ```
7. **Open a pull request** from your fork’s branch to the main branch of this repository.
- Describe the changes you’ve made in the pull request description.
- Ensure that your pull request references any relevant issues.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ngi-indi/module-search/blob/main/LICENSE.md) file for details.

## Contact
For any questions or support, please reach out to:
- University of Cagliari: bart@unica.it, diego.reforgiato@unica.it, ludovico.boratto@unica.it, mirko.marras@unica.it
- R2M Solution: giuseppe.scarpi@r2msolution.com
- Website: Coming soon!
