#to install 
pip install -r requirements.txt

#to run server 
uvicorn main:app --reload

#git guide
- git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
- cd YOUR_REPO_NAME
- git checkout -b feature/some-feature-name
# make your code changes
- git add .
- git commit -m "Added new feature"
- git push origin feature/some-feature-name
#regularly run
- git checkout main
- git pull origin main
