pipeline {
   
   agent any //{label 'slave_linux'}
    stages {
        
    //stage('Checkout SCM')   {
        
      //  steps {
      //git ('https://github.com/arksinha93/python-flask-demo.git')
      //if (!fileExists("Dockerfile")) {
        // error('Dockerfile missing.')  

    stage('Build') {
       
       steps {       
          sh "sudo docker build -t my-flask-app ."
          
   }
   }

    stage('Test') {
       
       steps {
          sh "sudo docker rm --force my-flask-app"         
          sh "sudo docker run -p 5000:5000 --name my-flask-app -d my-flask-app"
   }      
   }
    stage('Dast') {
      steps {
         //sh 'source /path/to/venv/bin/activate && pip install flake8'
         //sh 'pip install flake8'
         sh 'export PATH="/home/ec2-user/venv/lib/python3.9";'
         sh 'python3 app.py'
      }
    }
    stage('Deploy') {
       
       steps {
          //sh "sudo docker rm --force my-flask-app"         
          //sh "sudo docker run -p 5000:5000 --name my-flask-app -d my-flask-app"
          sh "sudo docker ps" 
   }      
   }   
     }  // End of stages
 
} // End of pipeline
