pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Aashrith2004/test_framework.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Start Selenium Grid') {
            steps {
                // Start Hub + all 3 nodes in background
                bat 'docker-compose up -d'
                // Wait until Hub reports nodes are ready
                bat '''
                    @echo off
                    :WAIT
                    curl -s http://localhost:4444/wd/hub/status | findstr "ready" >nul 2>&1
                    if errorlevel 1 (
                        timeout /t 3 >nul
                        goto WAIT
                    )
                    echo Selenium Grid is ready!
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -n 3 --dist=loadscope --junitxml=reports/junit.xml --alluredir=allure-results'
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
            // Tear down all containers after build
            bat 'docker-compose down'
            junit 'reports/junit.xml'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
