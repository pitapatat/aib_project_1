

# 다음 분기에 어떤 게임을 설계해야 할까
:rocket: library: pandas, seaborn

### 1. 배경 및 목적
```
- 연도별 게임의 트렌드 분석
- 지역별 선호하는 게임의 특성 분석
- 게임 출고량을 높이기 위한 전략 수립
```

### 2. 데이터셋 소개
```
- 출처 : Kaggle datasets
- 구성 : 1980-2020년 4개 지역(북미, EU, 일본, 기타)의 게임 출고량(by Genre/Publisher/Platform)
- 16,598개 데이터셋 
```

### 3. 분석 과정
```
- 데이터 전처리 : 연도/단위/타입 변경, 결측치 보완
- 데이터 분석 : 연도별/지역별/장르별/플랫폼별 게임 출고량 특징 분석 및 시각화
- 가설검정 : "지역간 선호하는 장르가 다르지 않다"  
```

#### 3-1. 결측치 보완

|결측치 포함 column| 결측치 수 | 보완 방법
|:-:|:-:|-|
|**Year** | 271|  다른 feture('Platform', 'Genre')를 통해 연도 유추 가능 </br>  게임 데이터는 시간에 따라 사용하는 플랫폼도 변화하는 경향이 있음</br>  'Platform'을 기준으로 사용 연도의 평균을 계산하여 결측치 보완 
|**Publisher**| 58|  'unknown' 으로 변환해 별도의 카테고리로 분류

#### 3-2. 데이터 분석 


### 4. 분석 결과

:heavy_check_mark: 연도별 게임 트렌드 현황 및 추이 

<center><img width = '1000' height = '700' src="https://user-images.githubusercontent.com/83687942/163402190-aa18ac62-21e0-4cb3-a2b9-5969de9a3b13.jpg"></center>
   
:heavy_check_mark: 지역별 장르별 게임 출고량 
<center><img width="1000" height= '400' alt="month-top10" src="https://user-images.githubusercontent.com/83687942/163402311-81c99a6c-74f9-490b-b09b-0ed3f902e063.jpg"></center>

:heavy_check_mark: 지역별 출고량이 높은 게임 TOP10 
<center><img width="700" height= '200' src = 'https://user-images.githubusercontent.com/83687942/163402628-ee7a1505-0f1a-4dbf-aeb8-d82feddd2176.jpg'></center>
<center><img width="700" height= '200' src = 'https://user-images.githubusercontent.com/83687942/163403051-df311f69-0163-4ebe-a58a-a6726a1e0538.jpg'></center>

:heavy_check_mark: 전체 출고량 중 미국이 차지하는 비중이 크며 지역별로 선호하는 게임의 특성이 상이함 
     
:heavy_check_mark: 게임플랫폼의 변화와 지역별 특징을 함께 고려하여 판매 계획 수립해야 함 

### 5. 보완점
* 추가 변동사항(22.01~) - 동일 데이터(결측치 부분 상이)분석을 통한 데이터 시각화 보완 : [ver_2](https://github.com/pitapatat/Data_Analysis_Visualization/blob/main/%5BDA%5D_video_game_sales/%5BDA%5D_video_game_sales_ver_2.ipynb)
 
