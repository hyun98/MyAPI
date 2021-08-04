# Django + React + nginx + mariadb
### [demo page](http://3.35.43.53/)

## 1. api 사용
1. Kospi 상장기업 최근 1년간의 주가 제공
2. api/stockapi/company 를 통해서 kospi 상장기업 정보를 json으로 가져올 수 있다.
3. api/stockapi/data/{기업명} 을 통해서 해당 기업의 최근 500일 + @(주말, 공휴일 제외)간의 주가 정보를 json으로 받아올 수 있다.

> React나 기타 frontend framework를 공부할 때 api를 받아와서 데이터를 가공해서 보여주고 싶으신 분들은 편하게 사용해주세요 

> 오류 발생시.. 
