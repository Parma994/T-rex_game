# Introduction
기존의 T-rex 에서 몇몇 기능을 추가했습니다.

# Upgrade

1. 일정 점수에 도달할 때마다 배경음악이 변경됩니다.
2. 일정 점수에 도달할 때마다 게임진행속도가 빨라집니다.
3. 게임 초기 화면에 1, 2, 3 등이 표기됩니다.
4. "물과 불" 게임처럼 키보드를 이용해 2명이서 함께할 수 있도록 제작하였습니다.
5. RSA보안을 이용하여 폴더의 파일을 통해 등수 조작을 하지 못하도록 제작하였습니다.

# How to play
## ~ Python 3.9
### Windows
```powershell
python.exe -m venv venv # 가상 환경 생성 (이미 생성된 경우는 통과)
.\venv\Scripts\activate # 가상 환경 활성화
pip install -r requirements.txt # requirements.txt 에 작성된 의존성 설치
```

### Mac & Linux
```zsh
python3 -m venv venv # 가상 환경 생성 (이미 생성된 경우는 통과)
source ./venv/bin/activate # 가상 환경 활성화
pip install -r requirements.txt # requirements.txt 에 작성된 의존성 설치
```

## Python 3.10
### 공통
* Gmpy2 는 Python 3.10을 공식적으로 지원하지 않기 때문에 RC(Release Candidate) 버전을 내려받아 수동 설치 해야 합니다.
* 라이브러리 설치를 위한 whl 파일은 [해당 링크](https://github.com/aleaxit/gmpy/releases/tag/gmpy2-2.1.0rc1) 에서 받으실 수 있습니다.
* Windows 64 비트 사용자는 gmpy2-2.1.0rc1-cp310-cp310-win_amd64.whl 를 다운받으면 됩니다. 
* Linux 32 비트 사용자는 gmpy2-2.1.0rc1-cp310-cp310-manylinux_2_12_i686.manylinux2010_i686.whl 를 다운받으면 됩니다. 
* Linux 64 비트 사용자는 gmpy2-2.1.0rc1-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl 를 다운받으면 됩니다. 
* MacOS(Intel) 사용자는 gmpy2-2.1.0rc1-cp310-cp310-macosx_10_9_x86_64.whl 를 다운받으면 됩니다. 
* MacOS(Apple Silicon) 사용자는 빌드된 라이브러리가 제공되지 않아 Source를 빌드하셔야 합니다.

### Windows
```powershell
python.exe -m venv venv # 가상 환경 생성 (이미 생성된 경우는 통과)
.\venv\Scripts\activate # 가상 환경 활성화
pip install pygame # Pygame 라이브러리 설치
pip install {다운받은 whl 경로} # Gmpy2 라이브러리 설치
```

### Mac & Linux
```zsh
python3 -m venv venv # 가상 환경 생성 (이미 생성된 경우는 통과)
source ./venv/bin/activate # 가상 환경 활성화
pip install pygame # Pygame 라이브러리 설치
pip install {다운받은 whl 경로} # Gmpy2 라이브러리 설치
```
     
          
# Game Display
![giphy](demonstration/running.gif)
