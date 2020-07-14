FROM python:3.8
WORKDIR /vue-blog-backend
COPY flask_test .

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

EXPOSE 5000
CMD gunicorn -w 2 app:app