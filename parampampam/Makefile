PORTNAME=	parampampam
DISTVERSION=	45.9171018
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	This tool for brute discover GET and POST parameters.
WWW=		https://github.com/Bo0oM/ParamPamPam

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-esprima@${PY_FLAVOR} \
		??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-levenshtein@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
