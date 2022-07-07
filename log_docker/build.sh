docker build --tag huge-logger .
docker tag huge-logger:latest asia-northeast3-docker.pkg.dev/independent-ljh/docker-ljh/bulk-logger
docker push asia-northeast3-docker.pkg.dev/independent-ljh/docker-ljh/bulk-logger
