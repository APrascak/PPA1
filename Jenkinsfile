pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7.4'
                }
            }
            steps {
                sh 'python -m py_compile ppa1.py'
            }
        }
        
    }
}