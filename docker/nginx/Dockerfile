FROM node:19 as build

WORKDIR /app/frontend
COPY ./frontend/ ./
RUN npm upgrade react-scripts
RUN npm ci --silent && npm run build

FROM nginx
COPY --from=build /app/frontend/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]