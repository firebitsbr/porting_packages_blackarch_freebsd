PORTNAME=	conpot
DISTVERSION=	0.6.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	ICS honeypot with the goal to collect intelligence about the motives and methods of adversaries targeting industrial control systems.
WWW=		https://pypi.org/project/Conpot/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-distribute@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python

RUN_DEPENDS=	??/hpfeeds \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-bottle@${PY_FLAVOR} \
		??/py-cpppo@${PY_FLAVOR} \
		??/py-crc16@${PY_FLAVOR} \
		??/py-crypto@${PY_FLAVOR} \
		??/py-cybox@${PY_FLAVOR} \
		??/py-enum-compat@${PY_FLAVOR} \
		??/py-freezegun@${PY_FLAVOR} \
		??/py-fs@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-libtaxii@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mixbox@${PY_FLAVOR} \
		??/py-modbus-tk@${PY_FLAVOR} \
		??/py-natsort@${PY_FLAVOR} \
		??/py-pyghmi@${PY_FLAVOR} \
		??/py-pysmi@${PY_FLAVOR} \
		??/py-pysnmp@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-slugify@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-stix-validator@${PY_FLAVOR} \
		??/py-stix@${PY_FLAVOR} \
		??/py-tftpy@${PY_FLAVOR} \
		??/py-tox@${PY_FLAVOR} \
		??/py-weakrefmethod@${PY_FLAVOR} \
		??/py-xlrd@${PY_FLAVOR} \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
