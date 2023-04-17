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
		stage('Bandit') {
                    	steps {
                        
                            	sh 'docker run calculator:latest bandit -lll -r /usr/src/app/app.py'
		
	

			}	
		}	
		stage('test'){
			steps{
				sh 'docker run -d -p 5000:5000 calculator'
				sh 'sleep 30'
				sh 'curl -d "a=21&b=5&operator=/" -X POST http://localhost:5000/calculate'
				sh 'docker stop $(docker ps -q --filter ancestor=calculator)'
		    	}
		}
	}
}
