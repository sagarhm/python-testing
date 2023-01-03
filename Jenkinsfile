pipeline {
  agent any
  stages {
    stage('test case1') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('test case2') {
      steps {
        sh 'python3 test_gold.py'
      }
    }
  }
}
