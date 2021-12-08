# Introduction
기존의 T-rex 에서 몇몇 기능을 추가했습니다.

# Upgrade

1. 일정 점수에 도달할 때마다 배경음악이 변경됩니다.
2. 일정 점수에 도달할 때마다 게임진행속도가 빨라집니다.
3. 게임 초기 화면에 1, 2, 3 등이 표기됩니다.
4. "물과 불" 게임처럼 키보드를 이용해 2명이서 함께할 수 있도록 제작하였습니다.
5. RSA보안을 이용하여 폴더의 파일을 통해 등수 조작을 하지 못하도록 제작하였습니다.

# How to play
### Windows
```powershell
python.exe -m venv venv # 가상 환경 생성 (이미 생성된 경우는 통과)
.\venv\Scripts\activate # 가상 환경 활성화
pip install pygame # Pygame 라이브러리 설치
```

### Mac & Linux
```zsh
python3 -m venv venv # 가상 환경 생성 (이미 생성된 경우는 통과)
source ./venv/bin/activate # 가상 환경 활성화
pip install pygame # Pygame 라이브러리 설치
```
      
* 스페이스바를 눌러 게임을 시작하세요.   
* 싱글모드를 플레이하려면 s키, 멀티모드(2명)를 플레이하려면 m키를 눌러주세요.   
* 싱글모드에서는 방향키로 조종합니다.
* 멀티모드에서 player 1은 방향키, player 2는 W, S 키로 조종합니다.   
     
          
# Game Display
![giphy](demonstration/running.gif)
