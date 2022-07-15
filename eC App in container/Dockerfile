FROM alpine:3.11
LABEL maintainer="alexander.fugmann@wago.com"
LABEL version="0.1.0"
LABEL description="WAGO Kontakttechnik Alpine image to use an e!C Application from Container"
RUN apk add openssh
COPY authorized_keys /root/.ssh/
RUN chmod 600 /root/.ssh/authorized_keys
COPY /home/codesys_root/eRUNTIME.cfg /root/
COPY /home/codesys_root/PlcLogic /root/
COPY do.sh /root/
RUN chmod 777 /root/do.sh

ENTRYPOINT ["/root/do.sh"]

