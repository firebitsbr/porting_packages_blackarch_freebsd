PORTNAME=	parameth
DISTVERSION=	56.8da6f27
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	This tool can be used to brute discover GET and POST parameters.
WWW=		https://github.com/mak-/parameth

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
