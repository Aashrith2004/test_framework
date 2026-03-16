pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/Aashrith2004/test_framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -n 3 --dist=loadscope'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
            }
        }

    }

    post {
        always {
            junit 'reports/junit.xml'
        }
    }
}
