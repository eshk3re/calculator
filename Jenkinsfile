pipeline{
	agent any
	
	stages {
		stage('clone'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/eshk3re/calculator']]]) 
			}
			when {
                		branch 'main'
                		changeset "**"
			}
		}
	
		stage ('build'){
			steps{
				sh 'docker build -t calculator:latest .'
			}
		}
	
		stage('test'){
			steps{
				sh 'docker run -d -p 8000:8000 calculator'
				sh 'curl -d "a=21&b=5&operator=/" -X POST http://localhost:8000/calculate'
				sh 'docker stop $(docker ps -q --filter ancestor=calculator)'
			}	
		}	
	}
}
