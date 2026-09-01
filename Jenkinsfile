pipeline {
    agent any
    stages {
        stage('Git') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    sh '''
                      echo "Hello World"
                    '''
                }
            }
        }
    }
}
