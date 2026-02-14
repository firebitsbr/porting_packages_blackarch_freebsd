PORTNAME=	flowinspect
DISTVERSION=	97.34759ed
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A network traffic inspection tool.
WWW=		https://github.com/7h3rAm/flowinspect

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-pylibemu@${PY_FLAVOR} \
		??/py-pynids@${PY_FLAVOR} \
		??/py-re2@${PY_FLAVOR} \
		??/py-yara@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
