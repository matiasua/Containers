# base image
FROM node:alpine

RUN mkdir -p /app-react/frontend

WORKDIR /app-react/frontend

RUN yarn install

COPY package.json /app-react/frontend


COPY . /app-react/frontend

CMD ["yarn", "run", "start"]