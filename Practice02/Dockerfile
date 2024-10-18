FROM ros:iron

ENV ROS_DISTRO=iron
ENV DEBIAN_FRONTEND=noninteractive

SHELL [ "/bin/bash", "-c" ]

RUN apt-get update
RUN apt install -y python3 python3-pip

WORKDIR /app

# COPY requirements.txt /app
# RUN pip3 install -r requirements.txt

COPY src /app/src

# RUN rosdep init
RUN rosdep update
RUN rosdep install -y --from-path ./src --rosdistro=${ROS_DISTRO}

RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon build

RUN echo "source /opt/ros/iron/setup.bash" >> ~/.bashrc
