FROM node:22
WORKDIR /app
COPY server.js /app
COPY package.json package-lock.json /app/
RUN npm install
CMD ["server.js"]
