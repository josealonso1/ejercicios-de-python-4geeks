FROM gitpod/workspace-full:latest

RUN sudo apt-get update && sudo apt-get install -y python3-pip
RUN alias python=python3
USER gitpod

RUN npm jest@29.7.0 jest-environment-jsdom@29.7.0 -g
RUN npm i @learnpack/learnpack@5.0.29 -g && learnpack plugins:install @learnpack/node@1.1.15
