# Super App
What is the our problem?
We download apps for our needs but why we download different app for different needs. I decided fix this problem.

### Deployment
```bash
git clone <repo>

cd <repo>

docker compose -f App/deploy/docker-compose.yml up --build -d

cd App/deploy

docker compose up
```

> Open the localhost at 5544 port.
>
>Click to [localhost](http://localhost:5544/)