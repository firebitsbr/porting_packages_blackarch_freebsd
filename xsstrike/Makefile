PORTNAME=	xsstrike
DISTVERSION=	475.ab27955
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An advanced XSS detection and exploitation suite.
WWW=		https://github.com/UltimateHackers/XSStrike

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-levenshtein@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
