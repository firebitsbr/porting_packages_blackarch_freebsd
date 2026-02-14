PORTNAME=	mqtt-pwn
DISTVERSION=	43.40368e5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A one-stop-shop for IoT Broker penetration-testing and security assessment operations.
WWW=		https://github.com/akamai-threat-research/mqtt-pwn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-blessings@${PY_FLAVOR} \
		??/py-cmd2@${PY_FLAVOR} \
		??/py-paho-mqtt@${PY_FLAVOR} \
		??/py-peewee@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
