PORTNAME=	pythem
DISTVERSION=	454.e4fcb8a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python2 penetration testing framework.
WWW=		https://github.com/m4n3dw0lf/PytheM

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/espeak-ng \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-netfilterqueue@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-praw@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pygeoip@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		??/py-pyttsx@${PY_FLAVOR} \
		??/py-ropper@${PY_FLAVOR} \
		??/py-speechrecognition@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
