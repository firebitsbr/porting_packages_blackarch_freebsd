PORTNAME=	nosqlattack
DISTVERSION=	98.a5b0329
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python tool to automate exploit MongoDB server IP on Internet anddisclose the database data by MongoDB default configuration weaknesses and injection attacks.
WWW=		https://github.com/youngyangyang04/NoSQLAttack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mongodb \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-ipcalc@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
