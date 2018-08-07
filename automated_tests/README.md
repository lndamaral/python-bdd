## Python BDD - Using Behave

### Setup

 1. Cloning the repository:

    ```shell
    git clone https://<your-username>@bitbucket.org/python-bdd.git
    ```

2. Installing all the dependencies:

    ```shell
    cd path/to/automated_testes

    pip install -r requirements.txt
    ```

### Python Naming Conventions

    http://visualgit.readthedocs.io/en/latest/pages/naming_convention.html

### Architecture

    /automated_tests:

        features/                       # Folder used to keep all feature files writen in Gherkin syntax
            <feature-name>.feature          
            <feature-name>.feature          

        helper/                         #Used to keep useful methods for common test operations
            <files>.py            
            <files>.py            

        model/                           #Folder where classes that implement models operations.
            <files>.py 
            <files>.py 
            <files>.py 

        steps/                           #Folder where classes that implement step definitions according to features.
            ..._step.py
            ..._step.py
            ..._step.py

### Test Execution

    cd path/to//automated_testes

    behave --no-captures
