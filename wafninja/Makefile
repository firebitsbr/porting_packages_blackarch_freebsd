PORTNAME=	wafninja
DISTVERSION=	25.379cd98
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool which contains two functions to attack Web Application Firewalls.
WWW=		https://github.com/khalilbijjou/WAFNinja

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-prettytable@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
