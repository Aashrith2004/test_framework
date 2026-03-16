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
                // Start Grid in background, redirect logs to file
                bat 'start /B java -jar selenium-server.jar standalone --port 4444 > selenium-grid.log 2>&1'
                // Wait for Grid to be ready
                bat '''
                    @echo off
                    :WAIT
                    curl -s http://localhost:4444/wd/hub/status | findstr "ready" >nul 2>&1
                    if errorlevel 1 (
                        timeout /t 2 >nul
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
            // Kill Selenium Grid after tests
            bat 'taskkill /F /IM java.exe /T >nul 2>&1 || exit /b 0'
            junit 'reports/junit.xml'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
