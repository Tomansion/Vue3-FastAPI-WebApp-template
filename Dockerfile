# Vue Frontend
FROM node:20 as build-stage
WORKDIR /frontend
COPY frontend/ .
RUN npm install
RUN npm run build

# Python Backend
FROM python:3.9
WORKDIR /backend
COPY backend/ .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY --from=build-stage /frontend/dist dist
CMD ["uvicorn", "websrv:app", "--host", "0.0.0.0", "--port", "3000"]