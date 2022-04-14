

# 다음 분기에 어떤 게임을 설계해야 할까

### 1. 배경 및 목적
```
- 연도별 게임의 트렌드 분석
- 지역별 선호하는 게임의 특성 분석
- 게임 출고량을 높이기 위한 전략 수립
```

### 2. 데이터셋 소개
```
- 기간 : 1980-2020년
- 대상 : 4개 지역(북미, EU, 일본, 기타)
- 내용 : 게임 출고량(by Genre/Publisher/Platform)
```

### 3. 분석 과정
:rocket: library: pandas, seaborn
```
- 데이터 전처리 : 연도/단위/타입 변경, 결측치 보완
- 데이터 분석 : 연도별/지역별/장르별/플랫폼별 게임 출고량 특징 분석 및 시각화
- 가설검정 : "지역간 선호하는 장르가 다르지 않다"  
```

### 4. 분석 결과

:heavy_check_mark: 연도별 게임 트렌드 
<center><img width = '600' height = '400' alt="month-cat" src="https://user-images.githubusercontent.com/83687942/163317294-be401a80-d0d9-4218-9e5d-97aa7895bc2c.png"></center>
   
:heavy_check_mark: 연도별 게임 장르별 출고량 
<center><img width="600" height= '400' alt="week-flow" src="https://user-images.githubusercontent.com/83687942/163317762-f0bfc114-9587-476c-bb42-47478e6baf3f.png"></center>

:heavy_check_mark: 지역별 장르별 게임 출고량 
<center><img width="600" height= '400' alt="month-top10" src="https://user-images.githubusercontent.com/83687942/163317849-3a266931-4b72-4463-85aa-4e28b4bc21af.png"></center>

:heavy_check_mark: 출고량이 높은 게임 TOP10 
<center><img width="500" height= '300' src = 'https://user-images.githubusercontent.com/83687942/163318431-ddad0068-c093-46a0-b234-43ab6b739eb2.PNG'></center>

:heavy_check_mark: 전체 출고량 중 미국이 차지하는 비중이 크며 지역별로 선호하는 게임의 특성이 상이함 
     
:heavy_check_mark: 게임플랫폼의 변화와 지역별 특징을 함께 고려하여 판매 계획 수립해야 함 

### 5. 보완점
* 추가 변동사항(22.01~) - 동일 데이터(결측치 부분 상이)분석을 통한 데이터 시각화 보완 : [ver_2](https://github.com/pitapatat/Data_Analysis_Visualization/blob/main/%5BDA%5D_video_game_sales/%5BDA%5D_video_game_sales_ver_2.ipynb)
 
