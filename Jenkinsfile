pipeline{
    agent any
    environment {
        PYTHON="C:\\Users\\sarfa\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
    }
    stages{
        stage("checkout code"){
            steps{
                checkout scm
            }
        }
        stage("show python version"){
            steps{
                bat "${env.PYTHON} --version"
            }
        }
        stage("run extractdata.py"){
            steps{
                bat "${env.PYTHON} extractdata.py"
            }
        }
    }
}
