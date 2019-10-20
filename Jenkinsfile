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
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test -- verbose --junit-xml test-reports/results.xml test_bmi.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        
    }
}