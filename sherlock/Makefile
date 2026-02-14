PORTNAME=	sherlock
DISTVERSION=	0.16.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find usernames across social networks.
WWW=		https://github.com/sherlock-project/sherlock

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-openpyxl@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-requests-futures@${PY_FLAVOR} \
		??/py-stem@${PY_FLAVOR} \
		??/py-torrequest@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
