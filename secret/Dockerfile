FROM ubuntu:latest

RUN apt update && \
    apt install -y openssh-server && \
    useradd -m dexter && \
    mkdir -p /home/dexter/.ssh

COPY id_rsa.pub /home/dexter/.ssh/authorized_keys

RUN chown -R dexter:dexter /home/dexter/.ssh && \
    chmod 700 /home/dexter/.ssh && \
    chmod 600 /home/dexter/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
