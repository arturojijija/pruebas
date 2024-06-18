pipeline{
    agent any
    stages {
        stage('Build'){
            step{
                echo "ETAPA BUILDNO DISPONIBLE"
            }
        }
        stage('Tests'){
            echo "Etapa testno disponible"
        }

        stage('Deploy'){
            steps{
                sh "docker-compose down -v" 
                sh "docker-compose up -d --build"
            }
        }
    }
}