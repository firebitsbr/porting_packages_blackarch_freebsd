PORTNAME=	buttinsky
DISTVERSION=	138.1a2a1b2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Provide an open source framework for automated botnet monitoring.
WWW=		https://github.com/buttinsky/buttinsky

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-configobj@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-hpfeeds@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-validictory@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
