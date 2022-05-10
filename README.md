# myapp
## Prerequisites
This app uses different frameworks to be deployed:
- [Python 3.10.2](https://www.python.org/)
- [Docker Desktop 3.6.0 Mac with Apple chip](https://docs.docker.com/desktop/mac/release-notes/3.x/)


## Installation
### Docker Compose
1. To run this project you will need to clone a [frontend project](https://github.com/nabetse28/UC-FundamentosDevOps-FrontEnd) that uses React JS framework. Then, inside the project, change to the `python-flask-test` branch.

```bash
git clone https://github.com/nabetse28/UC-FundamentosDevOps-FrontEnd
```

```bash
cd /UC-FundamentosDevOps-FrontEnd
git checkout python-flask-test
```

2. You will need a `.env` file to run the project with `docker-compose`. Create the `.env` file as follows:

```bash
cd /python-flask-test
nano .env
```

Add these lines to your `.env` with your values:
```
MONGO_USER=<YOUR_USER>
MONGO_PASSWORD=<YOUR_PASSWORD>
MONGO_SERVER=mongo_db
```

3. Now, run the following command to run the entire project:

```bash
docker-compose up --build -d
```

### Kubernetes