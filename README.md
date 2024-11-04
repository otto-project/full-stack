# 사이즈 기반 의류 추천 사이트
- 우리는 옷을 살 때 항상 고민합니다. 온라인에서 사는 옷의 사이즈가 나에게 맞는지를
- 우리는 옷을 살 때 항상 걱정합니다. 사이즈가 맞지 않으면 환불, 교환 해야 하는 것을
- 우리는 이러한 고민과 걱정 속에서 시작했습니다. 사이즈 기반 의류 추천 사이트 “OTTO”
  
## 목표
사용자에게 키와 몸무게 데이터를 받아 의류 쇼핑몰의 순위권의 제품을 리뷰 기반으로 사이즈를 추천

## skills 
|**skill**|detail|
|--|--|
|**WEB**|Python (3.12), Django|
|**DATABASE TOOL**|Amazon RDS(PostgreSQL 16.3), Amazon Redshift, DBeaver|
|**DATA STORAGE**|Amazon S3|
|**WORKFLOW**|Apache Airflow (2.9.2)|
|**CLOUD**|AWS|
|**DOMAIN AND ssl**|Amazon Route 53, AWS Certificate Manager|
|**WEB SCRAPING**|Selenium (Chrome 127.0.6533.119)|
|**CI/CD**|github action, lambda|

## Infra Architecture
<img src="https://github.com/SpaceSurfer051/otto-web/blob/main/img/aws_infra.png" width="700" height="400"/> 

- ROUTE 53을 통해 도메인 등록
- ACM에서 인증서 등록하여 로드밸런서(ALB)를 통해 이름 기반으로 접속
- 보안을 위해 퍼블릭과 프라이빗으로 VPC를 분리
  - 프라이빗의 내부 접속은 퍼블릭의 bastion host를 통해서만 접속 가능

## Django Architecture
<img src="https://github.com/SpaceSurfer051/otto-web/blob/main/img/django.png" width="700" height="400"/> 

- 개발 환경과 프로덕션 환경을 분리해서 운영
- 편의성과 보안을 위해 로컬에서 ssh 터널링을 통해서만 RDS 접속 가능

## Airflow Architecture
<img src="https://github.com/SpaceSurfer051/otto-web/blob/main/img/airflow_inside.png" width="600" height="300"/> 
<img src="https://github.com/SpaceSurfer051/otto-web/blob/main/img/airflow_cicd.png" width="600" height="200"/> 

- webserver 와 worker 노드를 각각의 다른 EC2에 두어 분산 시스템 구현
- github action과 람다를 통해 CI/CD 환경 구축
- EC2 재시작시 airflow가 실행되도록 우분투의 서비스로 자동화
- glances를 이용한 실시간 부하 모니터링
 
## ML
### Model
<img src="https://github.com/SpaceSurfer051/otto-web/blob/main/img/ml_model.png" width="700" height="400"/> 

선정된 모델 : XGBoost

모델 후보군 : KNN, Logistic Regression, Naive Bayes, Keras ,Decision Tree
- 선정 이유
  - **속도**: 일일 업데이트에 적합하도록 빠르게 처리할 수 있는 모델 선택
  - **비선형성 학습**: 다양한 범위의 키와 몸무게에 대한 사이즈 추천 시, 비선형 관계를 잘 학습할 수 있는 XGBoost 활용
  - **주관적 데이터셋**: 의류 사이즈는 개인 차이가 크므로, 부스팅 기법을 사용해 예측이 어려운 샘플에 더 집중
  - **과적합 방지**: XGBoost는 정규화와 조기 종료 기능을 통해 과적합을 방지할 수 있는 기법을 제공

### Pipeline
<img src="https://github.com/SpaceSurfer051/otto-web/blob/main/img/ml_pipeline.png" width="700" height="400"/> 

- Django와 XGBoost 모델을 각각 다른 EC2 인스턴스에서 운영함으로써 서버 부하 최소화
- FastAPI를 사용하여 Django와 API 통신 환경 구축
- S3를 활용하여 데이터 백업과 유지 보수 
- 리눅스의 크론잡을 통해 주기적인 학습을 통해 모델 최신화








