pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -n auto --alluredir=reports/allure-results'
            }
        }
        stage('Publish Reports') {
            steps {
                allure([
                    results: [[path: "reports/allure-results"]],
                    reportBuildPolicy: 'ALWAYS'
                ])
                archiveArtifacts artifacts: 'reports/videos/*.webm, reports/traces/*.zip', fingerprint: true
            }
        }
    }
}
