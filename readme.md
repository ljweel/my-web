# my-web

정적 사이트 프로젝트

## 로컬에서 실행

### 1. Docker Compose 실행
`docker compose up -d`

### 2. 접속
브라우저에서 `http://localhost`로 접속

### 3. 중지
`docker compose down`


## 서버에서 실행

### 1. 원격저장소 pull 하기
`git pull`

### 2. docker 내리기
`docker compose --profile tunnel down`

[컨테이너, 이미지, 볼륨 삭제 관련 글](https://code-angie.tistory.com/173)

### 3. 환경 변수 설정
`.env` 파일에 Cloudflare Tunnel 토큰을 설정합니다:

`CLOUDFLARE_TUNNEL_TOKEN=your_token_here`

### 4. Docker Compose 실행 (tunnel 포함)
`docker compose --profile tunnel up -d`


### 5. 접속
- HTTPS: `https://ljweel.dev`
- HTTP: `http://ljweel.dev` (자동으로 HTTPS로 리다이렉트)

### 6. 중지
`docker compose --profile tunnel down`

## 주요 설정 파일

- `nginx/default.conf`: Nginx 설정 파일
- `docker-compose.yml`: Docker Compose 설정
- `public/`: 정적 파일 디렉토리

## 주의사항

- 로컬과 서버에서 실행할 때 nginx 설정을 변경해야 합니다
- 서버에서는 SSL 인증서 파일(`cert.pem`, `priv.key`)이 필요합니다
- Cloudflare Tunnel을 사용하려면 `.env` 파일에 토큰을 설정해야 합니다