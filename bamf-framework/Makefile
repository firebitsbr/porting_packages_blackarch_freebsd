PORTNAME=	bamf-framework
DISTVERSION=	35.30d2b4b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular framework designed to be a platform to launch attacks against botnets.
WWW=		https://github.com/bwall/BAMF

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pycurl@${PY_FLAVOR} \
		??/py-pygeoip@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-yara@${PY_FLAVOR} \
		??/yara \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
