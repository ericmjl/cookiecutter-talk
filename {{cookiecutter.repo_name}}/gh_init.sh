# This script will run the necessary git commands to point to GitHub 

git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
git push -u origin master
rm initialize_upload.sh