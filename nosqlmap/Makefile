PORTNAME=	nosqlmap
DISTVERSION=	300.54d3fdb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated Mongo database and NoSQL web application exploitation tool
WWW=		https://github.com/tcstool/NoSQLMap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mongodb \
		??/py-couchdb@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-ipcalc@${PY_FLAVOR} \
		??/py-pbkdf2@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
