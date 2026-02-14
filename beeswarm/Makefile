PORTNAME=	beeswarm
DISTVERSION=	1183.db51ea0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Honeypot deployment made easy.
WWW=		https://github.com/honeynet/beeswarm/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-backports-os@${PY_FLAVOR} \
		??/py-cssselect@${PY_FLAVOR} \
		??/py-ecdsa@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-fs@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-ntplib@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pydes@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysendfile@${PY_FLAVOR} \
		??/py-pyzmq@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-telnetsrv@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
