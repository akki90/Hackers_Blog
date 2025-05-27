pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building your project...'
                // insert your build command here, e.g., npm build or mvn package
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // insert your test command here, e.g., npm test or pytest
            }
        }

        stage('Snyk Scan') {
            steps {
                snykSecurityScan failOnIssues: true
            }
        }
    }
}
