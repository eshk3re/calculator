pipeline{
	agent any
	
	stages {
		stage('clone'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/eshk3re/calculator']]])  //клонируем репозиторий
			}
			when {
                		branch 'main'
                		changeset "**"
			}
		}
	
		stage ('build'){
			steps{
				sh 'sudo docker build -t calculator:latest .'  //создание образа

                        
                    }
                }
		stage('Bandit') {
                    	steps {
                        
				sh 'sudo docker run calculator:latest bandit -lll -r app.py' //проверка кода бандитом внутри контейнера
		
	

			}	
		}	
		stage('test'){
			steps{
				sh 'sudo docker run -d -p 5000:5000 calculator' //запуск контейнера на 5000 порте
				sh 'sleep 30'
				sh 'curl -d "a=21&b=5&operator=/" -X POST http://localhost:5000/calculate' //отправляем пост запрос с указанными числами и оператором
				sh 'sudo docker stop $(docker ps -q --filter ancestor=calculator)' //остановка контейнера
		    	}
		}
	}
}

//на машине на которой развертывается сервер, должен быть установлен jenkins (у пользователя jenkins должен быть sudo докера). Авторизуемся через пользователя на сервере Jenkins и создаем pipeline, куда вставляем ссылку на этот github.
