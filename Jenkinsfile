pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SRCEM-AIM-Class-A/A-31_Cherry-Agarwal.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t agarwalcp/djangodockerproject:latest .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push agarwalcp/djangodockerproject:latest'
                }
            }
        }
    }
}