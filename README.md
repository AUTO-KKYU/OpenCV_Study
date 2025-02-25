# OpenCV (Open Source Computer Vision)

## OpenCV(Open Source Computer Vision)
-  영상 처리에 사용할 수 있는 오픈 소스 라이브러리
-  컴퓨터가 사람의 눈처럼 인식할 수 있게 처리해주는 역할을 하기도 하며, 우리가 많이 사용하는 카메라 어플에서도 OpenCV가 사용하기도 한다.
-  카메라로 찍어서 할 수 있는 모든 일은 OpenCV로 처리할 수 있다
-  여기에 머신 러닝과 A.I를 활용해서 그 활용도를 더욱 넓혀가고 있는 중이다.

## Installation

1) Python 가상환경 설정
- macOS/Linux
```sh
$ source venv/opencv/bin/activate
```

2) OpenCV 설치
```sh
$ python -m pip install opencv-python
$ python -m pip install --upgrade pip
```

## example (이미지 파일 열기)

```ruby
import cv2

# 이미지 파일 열기
image = cv2.imread('image.jpg')
# 이미지를 화면에 표시
cv2.imshow('Image', image)

# 키 입력 대기
cv2.waitKey(0)
# 창 닫기
cv2.destroyAllWindows()
```

