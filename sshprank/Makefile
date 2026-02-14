PORTNAME=	sshprank
DISTVERSION=	1.4.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A fast SSH mass-scanner, login cracker and banner grabber tool using the python-masscan and shodan module.
WWW=		https://nullsecurity.net/tools/cracker.html

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-masscan@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
