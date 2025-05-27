pipeline {
    agent any

    environment {
        SNYK_TOKEN = credentials('snyk-token') // Load Snyk token from Jenkins credentials
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-Personal-access-token', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test'
            }
        }

        stage('Snyk Scan') {
            steps {
                sh 'snyk auth $SNYK_TOKEN'
                sh 'snyk test'          // For scanning known vulnerabilities
                sh 'snyk code test || true'  // For static code analysis (optional)
            }
        }
    }
}
