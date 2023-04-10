pipeline{
	agent any
	
	triggers{
		githubPush()
	}
	
	stages {
		stage('Checkout'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/eshk3re/calculator']]]) 
			}
		}
	
		stage ('build'){
			steps{
				sh 'docker build -t calculator:latest .'
			}
		}
	
		stage('test'){
			steps{
				sh 'docker run -d -p 5000:5000 calculator'
				sh 'sleep 60'
				sh 'curl -d "num1=12&num2=9" -X POST http://localhost:5000/multiply'
				sh 'docker stop $(docker ps -q --filter ancestor=calculator)'
			}	
		}	
	}
}
