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
                bat 'docker-compose -f docker/docker-compose.yml up -d'
                powershell '''
                    $maxRetries = 20
                    $retries = 0
                    do {
                        try {
                            $response = Invoke-RestMethod -Uri "http://localhost:4444/wd/hub/status" -Method Get
                            if ($response.value.ready -eq $true) {
                                Write-Host "Selenium Grid is ready!"
                                exit 0
                            }
                        } catch {
                            Write-Host "Waiting for Selenium Grid..."
                        }
                        Start-Sleep -Seconds 3
                        $retries++
                    } while ($retries -lt $maxRetries)
                    Write-Host "Selenium Grid did not start in time!"
                    exit 1
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -n 3 --dist=loadscope --junitxml=reports/junit.xml --alluredir=allure-results'
            }
        }
        stage('Allure Report') {
         steps {
        powershell '''
            $port = 4040
            $allure = "C:\\Users\\Aashrith\\scoop\\shims\\allure.cmd"
            
            # Run allure serve in background so Jenkins does not hang
            Start-Process -FilePath $allure -ArgumentList "serve allure-results --port $port" -WindowStyle Hidden
            
            Start-Sleep -Seconds 5
            Write-Host "========================================="
            Write-Host "Allure Report is available at:"
            Write-Host "http://127.0.0.1:$port"
            Write-Host "========================================="
        '''
    }
}

    post {
        always {
            junit 'reports/junit.xml'
        }
    }
}
}
