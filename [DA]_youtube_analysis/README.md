
# YOUTUBE 인기동영상 데이터 분석 및 호응도 지표개발



### 1. 배경 및 목적
```
- 카테고리/월별/주별 비디오 특징 시각화 
- 월별/주별 TOP10 채널 특성 분석
- 시청자의 호응도(engagement) 판단 지표 개발 
```

### 2. 데이터셋 소개
```
- YOUTUBE > 메인 > '탐색/인기' : 인기동영상으로 선택된 비디오 기준
- 2021.03-25 - 2021.07.29 데이터셋
```


### 3. 분석 과정
:rocket: library: pandas, seaborn, nltk
```
- 데이터 전처리 : 결측치 확인, 데이터 타입 변경, 텍스트 데이터 전처리
- 데이터 분석 : 카테고리별/월별/주별 상/하위 인기동영상의 특징 분석 및 시각화
- tag 키워드 빈도 분석 : 카테고리별/월별 tag 키워드 빈도수 분석 및 시각화
```
```
- 호응도 지표 분석 : 조회수, 영상길이, 구독자수 및 조회수와 변수 간 상관관계 분석
- 인기동영상 지표 개발 : 조회수 대비 (좋아요+싫어요)수, 구독자수 대비 조회수 외 관련 변수 가중치 부여
```

### 4. 분석 결과
#### 4-1. 인기동영상 채널 특징 

:heavy_check_mark: 인기 카테고리 : entertainment > people & blogs 순으로 나타나며 pets & animals 채널의 꾸준한 상승세가 두드러짐 

:heavy_check_mark: 월별 특이점 : 6,7월 sports 채널 상승세 두드러짐(카타르원드컵, euro2020, 도쿄올림픽 등 스포츠 시즌에 영향으로 추정) 
<center><img width="1000" height= '300' alt="month-flow" src="https://user-images.githubusercontent.com/83687942/163302783-5a119f01-23c9-4c6b-8069-6cde4d8b4a70.png"></center>
<center><img width="1000" height= '300' alt="month-cat" src="https://user-images.githubusercontent.com/83687942/163302876-ef211500-aafe-44ca-9d5d-99196b0e4fd3.png"></center>
   
:heavy_check_mark: 주별 특이점 : 주별 카테고리의 변동폭이 크나 구성비에는 큰 변화 없음. howto & style 채널이 상위권에 자주 랭크됨 

<center><img width="1000" height= '300' alt="week-flow" src="https://user-images.githubusercontent.com/83687942/163304127-bbc312f6-bb14-484d-837d-21ab6898ce25.png"></center>
<center><img width="1000" height= '300' alt="week-cat" src="https://user-images.githubusercontent.com/83687942/163304167-1f863741-fcc6-4fc9-b463-51fbb52a348f.png"></center>

:heavy_check_mark: 월별 TOP10 채널 
<center><img width="1000" height= '300' alt="month-top10" src="https://user-images.githubusercontent.com/83687942/163305727-8288615b-3b71-4096-b856-fa426cf76741.png"></center>

:heavy_check_mark: 월별 tag 키워드 : "먹방", "몰카", "일상", "브이로그"는 매월 공통으로 높은 빈도로 등장하며 유행어(예: 브레이브걸스, 올림픽 등)가 tag로 주로 사용됨 
<center><img width="1000" height= '300' alt="teg-4" src="https://user-images.githubusercontent.com/83687942/163306585-b47e6725-05fc-4383-80c5-7b71dd8d0e94.png"></center>

:heavy_check_mark: 카테고리별 tag 키워드 : 카테고리별 유명 인플루언서(또는 운동선수/연예인)의 빈도가 높으며 "음식", "먹방" tag는 카테고리별 영향을 덜 받는 편임 
<center><img width="1000" height= '300' alt="sports-tag" src="https://user-images.githubusercontent.com/83687942/163305901-308b9d49-bf3c-4b52-a3f8-73f9bac84d5e.png"></center>

#### 4-2. 인기 호응도 지표 분석 
:heavy_check_mark: 인기동영상의 특징 - 10-15분 길이의 영상/업로드 후 시간당 1만회 조회수 & 2일 내 인기동영상 진입 & 3일 내 유지

:heavy_check_mark: 조회수와 높은 상관관계 지표 : 좋아요수, 싫어요수, 댓글수, 구독자수

<center><img width="500" height= '400' alt="corr" src="https://user-images.githubusercontent.com/83687942/163309811-49066ee8-8e07-4199-840e-088930729664.png"></center>

#### 4-3. 인기 호응도 지표 개발
:heavy_check_mark: 조회수와 높은 상관관계를 보이는 지표들의 가중치 평균 및 가중치 조정값을 통해 인기 호응도 지표를 개발하고자 함

:heavy_check_mark: 하지만 '조회수(또는 좋아요수)'의 상관관계/ols 검정 결과 유의미한 선형 상관관계는 나타나지 않음


### 5. 한계점 및 보완점
```
- 가중치 부여를 통한 변수 변환이 너무 단순하게 이뤄졌음
- 해당 변수 외 다른 요인(시기적 이슈-선거, 올림픽, 김장, 음박 출시 등)을 고려하지 못함
- 채널(계정) 생성 시기 데이터도 추가적으로 고려하면 좋을 것 같음
- 향후 인기동영상의 tag, description의 긍/부정 분석을 추가하면 좋을듯 함
```
