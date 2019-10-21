pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'pip install --no-cache-dir pymongo'
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
                sh 'py.test --verbose test_bmi.py test_email_verifier.py test_retirement.py test_shortest_distance.py test_split_the_tip.py'
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2'
                }
            }
            steps {
                sh 'pyinstaller --onefile ppa1.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/ppa1'
                }
            }
        }
    }
}