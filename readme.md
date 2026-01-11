# my-web

정적 사이트 프로젝트

## 로컬에서 실행

### 1. nginx 설정 확인
`nginx/default.conf` 파일에서 두 번째 server 블록에 `server_name localhost;`가 설정되어 있어야 합니다.

server {
    listen 80;
    server_name localhost;  # 로컬에서는 활성화
    ...
}### 2. Docker Compose 실행h
docker-compose up -d
### 3. 접속
브라우저에서 `http://localhost`로 접속

### 4. 중지ash
docker-compose down## 서버에서 실행

### 1. nginx 설정 수정
`nginx/default.conf` 파일에서 두 번째 server 블록의 `server_name localhost;`를 주석 처리합니다:

server {
    listen 80;
    # server_name localhost;  # 서버에서는 주석 처리
    ...
}또는 `default_server`를 사용:

server {
    listen 80 default_server;
    # server_name localhost;
    ...
}### 2. 환경 변수 설정
`.env` 파일에 Cloudflare Tunnel 토큰을 설정합니다:

CLOUDFLARE_TUNNEL_TOKEN=your_token_here### 3. Docker Compose 실행 (tunnel 포함)
docker-compose --profile tunnel up -d또는 tunnel 없이 nginx만 실행:
h
docker-compose up -d### 4. 접속
- HTTPS: `https://ljweel.dev`
- HTTP: `http://ljweel.dev` (자동으로 HTTPS로 리다이렉트)

### 5. 중지sh
docker-compose --profile tunnel down## 주요 설정 파일

- `nginx/default.conf`: Nginx 설정 파일
- `docker-compose.yml`: Docker Compose 설정
- `public/`: 정적 파일 디렉토리

## 주의사항

- 로컬과 서버에서 실행할 때 nginx 설정을 변경해야 합니다
- 서버에서는 SSL 인증서 파일(`cert.pem`, `priv.key`)이 필요합니다
- Cloudflare Tunnel을 사용하려면 `.env` 파일에 토큰을 설정해야 합니다