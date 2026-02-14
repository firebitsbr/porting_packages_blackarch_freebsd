PORTNAME=	eaphammer
DISTVERSION=	v1.14.1.r0.g91e8956
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Targeted evil twin attacks against WPA2-Enterprise networks. Indirect wireless pivots using hostile portal attacks.
WWW=		https://github.com/s0lst1c3/eaphammer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/apache \
		??/dnsmasq \
		??/hcxdumptool \
		??/hcxtools \
		??/libnfnetlink \
		??/libnl \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask-socketio@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pem@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pywebcopy@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/responder \
		??/scapy \
		ftp/curl \
		lang/python \
		net/libpcap \
		security/openssl \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
