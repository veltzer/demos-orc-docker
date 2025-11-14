FROM gradle:jdk25-corretto AS build
WORKDIR /app
COPY build.gradle settings.gradle ./
RUN gradle dependencies --no-daemon
COPY src ./src
RUN gradle uberJar --no-daemon

FROM openjdk:25-ea-slim
WORKDIR /app
COPY --from=build /app/build/libs/myapp-1.0-uber.jar ./
ENTRYPOINT ["java", "-jar", "myapp-1.0-uber.jar"]
